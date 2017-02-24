from tkinter import *
from tooltip import ToolTip
from octoclient.octoclient.client import OctoClient
from pprint import *
import time, os

from utils import *
import frames

class PrinterBar3:

	def __init__(self):
		self.root = Tk()

		self._frames = frames.Frames(self)

		self.init()

	def init(self):
		f = open( os.path.join(os.path.expanduser('~'), "octoprint_config"), "r" )
		self.api = f.readline(  ).replace("\n","")
		self.url = f.readline(  ).replace("\n","")
		f.close(  )

		self.octoclient = OctoClient(url=self.url, apikey=self.api)

		self.current_frame = 'main'
		self.graph_temperature_multtime = 3
		self.graph_temperature_lastpos = (None, None)

		self.root.wm_title( "PB3" )
		self.root.call('wm', 'attributes', '.', '-topmost', '1')	# make the window stay on top

		self._update_interval = 500	# ms
		self.update_interval = self._update_interval

		for frame_name, frame_data in self._frames.frames.items():

			# create a frame in root
			self._frames.frames[frame_name]['frame'] = \
				Frame( self.root, **self._frames.frames[frame_name]['frameargs'] )		
			
			# grid the frame
			if 'gridargs' in self._frames.frames[frame_name].keys():
				self._frames.frames[frame_name]['frame'].grid\
					(**self._frames.frames[frame_name]['gridargs'])	

			else:
				self._frames.frames[frame_name]['frame'].pack\
					(**self._frames.frames[frame_name]['packargs'])	


			# create all elements/widgets inside that frame
			for element_type, elementlist in frame_data.items():		

				if element_type == 'labels':							
				# create all label elements

					# cycle through the list of elements
					for element in elementlist:							

						# make a label with arguments
						l = Label( self._frames.frames[frame_name]['frame'], **element['label'] )	

						# grid the label with arguments
						l.grid( **element['grid'] )													

						# add that label to the list of elements
						self._frames.frames[frame_name]['element_list'][element['id']] = l			

						if 'tooltip' in element.keys():
							ToolTip(l, **element['tooltip'])

				elif element_type == 'buttons':

					for element in elementlist:

						b = Button( self._frames.frames[frame_name]['frame'], **element['button'] )

						if 'pack' in element.keys():
							b.pack( **element['pack'] )
						else:
							b.grid( **element['grid'] )

						self._frames.frames[frame_name]['element_list'][element['id']] = b

						if 'tooltip' in element.keys():
							ToolTip(b, **element['tooltip'])
				
				elif element_type == 'canvases':

					for element in elementlist:

						c = Canvas( self._frames.frames[frame_name]['frame'], **element['canvas'] )

						c.grid( **element['grid'] )
						self._frames.frames[frame_name]['element_list'][element['id']] = c

						if 'tooltip' in element.keys():
							ToolTip(c, **element['tooltip'])

				if isinstance(elementlist, list):
					for elem in elementlist:
						if isinstance(elem, dict):
							if 'bind' in elem.keys():
								self._frames.frames[frame_name]['element_list'][elem['id']].bind( 
									elem['bind']['event'], elem['bind']['action'] )


		self.root.update()

		# set canvas width
		self._frames.frames['main']['element_list']['bar_progress'].width = \
			self._frames.frames['main']['frame'].winfo_width()-2

		self._frames.frames['main']['element_list']['bar_progress_time'].width = \
			self._frames.frames['main']['frame'].winfo_width()-2

		self._frames.frames['graph']['element_list']['graph_temperature']['width'] = \
				self._frames.frames['main']['frame'].winfo_width()-2

		##

		self.raise_frame(self.current_frame)

		self.update()
		self.root.mainloop()

	def update(self):

		_job = self.octoclient.job_info()
		if _job: job=_job
		else: job=None
		_tool = self.octoclient.tool()
		if _tool: tool=_tool
		else: tool=None
		_bed = self.octoclient.bed()
		if _bed: bed=_bed
		else: bed=None

		_tool_history=self.octoclient.tool(history=True, limit=800)
		if _tool_history: tool_history=_tool_history
		else: tool_history = None

		_bed_history=self.octoclient.bed(history=True, limit=800)
		if _bed_history: bed_history=_bed_history
		else: bed_history = None

		if self.current_frame == 'graph_temperature': self.update_interval=10
		else: self.update_interval=self._update_interval


		if job:
			self._frames.frames['status']['element_list']['print_name']['text'] = job['job']['file']['path'].split(".gcode")[0]
		else:
			self._frames.frames['status']['element_list']['print_name']['text'] = "-"

		if self.current_frame == 'main':

			# update tools

			if tool:
				self._frames.frames['main']['element_list']['temp_tool']['fg']=get_col(tool['tool0']['actual'], [100, 210])
				self._frames.frames['main']['element_list']['temp_tool']['text'] = "%sC / %sC" %\
					( tool['tool0']['actual'], tool['tool0']['target'] )
			else:
				self._frames.frames['main']['element_list']['temp_tool']['text'] = "-"


			if bed:
				self._frames.frames['main']['element_list']['temp_bed']['fg']=get_col(bed['bed']['actual'], [20, 60])
				self._frames.frames['main']['element_list']['temp_bed']['text'] = "%sC / %sC" %\
					( bed['bed']['actual'], bed['bed']['target'] )

			else:
				self._frames.frames['main']['element_list']['temp_bed']['text'] = "-"

			
			# update text

			if job:
				self._frames.frames['main']['element_list']['print_time_done']['text'] = \
					time.strftime("%Hh %Mm %Ss", time.gmtime(job['progress']['printTime']))

				self._frames.frames['main']['element_list']['print_time_left']['text'] = \
					time.strftime("%Hh %Mm %Ss", time.gmtime(job['progress']['printTimeLeft']))

				progress = job['progress']['completion']

				# draw the bar with colors

				if progress:
					draw_progress_bar( self._frames.frames['main']['element_list']['bar_progress'], progress/100.0 )
				else:
					draw_progress_bar( self._frames.frames['main']['element_list']['bar_progress'], 10**-10 )

				if job['progress']['printTimeLeft'] and job['progress']['printTime']:
					draw_progress_bar( self._frames.frames['main']['element_list']['bar_progress_time'],
						float( job['progress']['printTime'] ) / 
						( float( job['progress']['printTime'] )+float( job['progress']['printTimeLeft'] ) ), value=64 )
				else:
					draw_progress_bar( self._frames.frames['main']['element_list']['bar_progress_time'], 10**-10, value=64 )

			else:
				self._frames.frames['main']['element_list']['print_time_done']['text'] = "-"
				self._frames.frames['main']['element_list']['print_time_left']['text'] = "-"

		elif self.current_frame == 'graph':
			if tool_history and bed_history:

				draw_graph( self._frames.frames['graph']['element_list']['graph_temperature'],
					tool_history, bed_history, multtime=self.graph_temperature_multtime, lastpos=self.graph_temperature_lastpos )


		self.root.after(self.update_interval, self.update)

	def raise_frame(self, name):
		self.current_frame=name
		self._frames.frames[name]['frame'].tkraise()
		for f in self._frames.frames.keys():

			if f != name:
				self._frames.frames[f]['frame'].lower()

		for b in range(len(self._frames.frames['status']['buttons'])):

			if self._frames.frames['status']['buttons'][b]['id'] == 'btn_goto_' + name:
				self._frames.frames['status']['element_list']['btn_goto_' + name]['relief'] = SUNKEN

			else:
				self._frames.frames['status']['element_list']\
					[self._frames.frames['status']['buttons'][b]['id']]['relief'] = FLAT

	def zoom_graph_temperature(self, event):
		if event.num == 5:
			self.graph_temperature_multtime += 0.2
		elif event.num == 4:
			self.graph_temperature_multtime -= 0.2

		if self.graph_temperature_multtime < 0.6: self.graph_temperature_multtime = 0.6
		if self.graph_temperature_multtime > 8: self.graph_temperature_multtime = 8

		if event.num == 1:
			self.graph_temperature_lastpos=(event.x, event.y)

		if event.num == 3:
			self.graph_temperature_lastpos=(None, None)

if __name__ == '__main__':
	pb3 = PrinterBar3()