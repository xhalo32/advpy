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

		self.root.wm_title( "PB3" )
		self.root.call('wm', 'attributes', '.', '-topmost', '1')	# make the window stay on top

		self.update_interval = 1000	# ms

		for frame_name, frame_data in self._frames.frames.items():

			# create a frame in root
			self._frames.frames[frame_name]['frame'] = \
				Frame( self.root, **self._frames.frames[frame_name]['frameargs'] )		
			
			# pack the frame
			self._frames.frames[frame_name]['frame'].grid\
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


		self.root.update()

		# set canvas width
		self._frames.frames['main']['element_list']['bar_progress'].width = \
			self._frames.frames['main']['frame'].winfo_width()

		self._frames.frames['main']['element_list']['bar_progress_time'].width = \
			self._frames.frames['main']['frame'].winfo_width()

		#print(self._frames.frames['main']['element_list']['bar_progress'].width) # 32 : 264


		self.raise_frame(self.current_frame)

		self.update()
		self.root.mainloop()

	def update(self):
		job = self.octoclient.job_info()

		self._frames.frames['status']['element_list']['print_name']['text'] = job['job']['file']['path'].split(".gcode")[0]

		if self.current_frame == 'main':

			if job['progress']['printTime']:
				self._frames.frames['main']['element_list']['print_time_done']['text'] = \
					time.strftime("%Hh %Mm %Ss", time.gmtime(job['progress']['printTime']))

				self._frames.frames['main']['element_list']['print_time_left']['text'] = \
					time.strftime("%Hh %Mm %Ss", time.gmtime(job['progress']['printTimeLeft']))

				progress = job['progress']['completion']

				# draw the bar with colors
				draw_progress_bar( self._frames.frames['main']['element_list']['bar_progress'], progress/100.0 )
				draw_progress_bar( self._frames.frames['main']['element_list']['bar_progress_time'],
					float( job['progress']['printTime'] ) / 
					( float( job['progress']['printTime'] )+float( job['progress']['printTimeLeft'] ) ) )

		self.root.after(self.update_interval, self.update)

	def raise_frame(self, name):
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


def main():
	pb3 = PrinterBar3()

if __name__ == '__main__':
	main()