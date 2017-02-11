from Tkinter import *
import Tkinter
import urllib, json, time

class ToolTip:
	def __init__(self, master, text='Your text here', delay=1500, **opts):
		self.master = master
		self._opts = {'anchor':'center', 'bd':1, 'bg':'lightyellow', 'delay':delay, 'fg':'black',\
					  'follow_mouse':0, 'font':None, 'justify':'left', 'padx':4, 'pady':2,\
					  'relief':'solid', 'state':'normal', 'text':text, 'textvariable':None,\
					  'width':0, 'wraplength':150}
		self.configure(**opts)
		self._tipwindow = None
		self._id = None
		self._id1 = self.master.bind("<Enter>", self.enter, '+')
		self._id2 = self.master.bind("<Leave>", self.leave, '+')
		self._id3 = self.master.bind("<ButtonPress>", self.leave, '+')
		self._follow_mouse = 0
		if self._opts['follow_mouse']:
			self._id4 = self.master.bind("<Motion>", self.motion, '+')
			self._follow_mouse = 1
	
	def configure(self, **opts):
		for key in opts:
			if self._opts.has_key(key):
				self._opts[key] = opts[key]
			else:
				KeyError = 'KeyError: Unknown option: "%s"' %key
				raise KeyError
	
	##----these methods handle the callbacks on "<Enter>", "<Leave>" and "<Motion>"---------------##
	##----events on the parent widget; override them if you want to change the widget's behavior--##
	
	def enter(self, event=None):
		self._schedule()
		
	def leave(self, event=None):
		self._unschedule()
		self._hide()
	
	def motion(self, event=None):
		if self._tipwindow and self._follow_mouse:
			x, y = self.coords()
			self._tipwindow.wm_geometry("+%d+%d" % (x, y))
	
	##------the methods that do the work:---------------------------------------------------------##
	
	def _schedule(self):
		self._unschedule()
		if self._opts['state'] == 'disabled':
			return
		self._id = self.master.after(self._opts['delay'], self._show)

	def _unschedule(self):
		id = self._id
		self._id = None
		if id:
			self.master.after_cancel(id)

	def _show(self):
		if self._opts['state'] == 'disabled':
			self._unschedule()
			return
		if not self._tipwindow:
			self._tipwindow = tw = Tkinter.Toplevel(self.master)
			# hide the window until we know the geometry
			tw.withdraw()
			tw.wm_overrideredirect(1)

			#if tw.tk.call("tk", "windowingsystem") == 'aqua':
			#	tw.tk.call("::tk::unsupported::MacWindowStyle", "style", tw._w, "help", "none")

			self.create_contents()
			tw.update_idletasks()
			x, y = self.coords()
			tw.wm_geometry("+%d+%d" % (x, y))
			tw.deiconify()
	
	def _hide(self):
		tw = self._tipwindow
		self._tipwindow = None
		if tw:
			tw.destroy()
				
	##----these methods might be overridden in derived classes:----------------------------------##
	
	def coords(self):
		# The tip window must be completely outside the master widget;
		# otherwise when the mouse enters the tip window we get
		# a leave event and it disappears, and then we get an enter
		# event and it reappears, and so on forever :-(
		# or we take care that the mouse pointer is always outside the tipwindow :-)
		tw = self._tipwindow
		twx, twy = tw.winfo_reqwidth(), tw.winfo_reqheight()
		w, h = tw.winfo_screenwidth(), tw.winfo_screenheight()
		# calculate the y coordinate:
		if self._follow_mouse:
			y = tw.winfo_pointery() + 20
			# make sure the tipwindow is never outside the screen:
			if y + twy > h:
				y = y - twy - 30
		else:
			y = self.master.winfo_rooty() + self.master.winfo_height() + 3
			if y + twy > h:
				y = self.master.winfo_rooty() - twy - 3
		# we can use the same x coord in both cases:
		x = tw.winfo_pointerx() - twx / 2
		if x < 0:
			x = 0
		elif x + twx > w:
			x = w - twx
		return x, y

	def create_contents(self):
		opts = self._opts.copy()
		del opts[ "follow_mouse" ]
		for opt in ('delay', 'state'):
			del opts[opt]
		label = Tkinter.Label(self._tipwindow, **opts)
		label.pack()



	## MAIN ##

import os

f = open( os.path.join(os.path.expanduser('~'), "octoprint_config"), "r" )
apikey = f.readline(  )
printer_address = f.readline(  )
f.close(  )

print apikey, printer_address

body = progress = printer = temperature = None


def get_body(  ):
	try:
		return json.loads(urllib.urlopen(printer_address + '/api/job?apikey=' + apikey).read())
	except: 
		return None

def get_printer(  ):
	try:
		return json.loads(urllib.urlopen(printer_address + '/api/printer?apikey=' + apikey).read())
	except: 
		return None

def convert( rgb ):
	rgb = [ int( c ) for c in rgb ]
	color = "#"
	for c in rgb:
		h = format( hex( c ).split( 'x' )[ 1 ] )
		if c < 16: h = "0"+h
		color += h

	if len( color ) != 7: print "VALUES MUST BE IN RANGE 0-255";return None
	return color

def human( seconds ):
	if seconds == None: return ""
	seconds = int( seconds )

	secs = seconds % 60
	mins = ( seconds // 60 ) % 60
	hours = ( seconds // 3600 ) % 3600

	r = ""

	if hours != 0: r += str(hours) + "h "
	if mins != 0: r += str(mins) + "min "
	r += str(secs) + "s"
	return r


root = Tk()
root.wm_title( "PrinterBar" )

f = Frame( root )
f.pack(  )

'''
lbl2 = Label( f, text=human( progress[ "printTime" ] ), height=2, 		width=15, bd=1, relief=SUNKEN )
lbl3 = Label( f, text=human( progress[ "printTimeLeft" ] ), height=2, 	width=15, bd=1, relief=SUNKEN )
lbl4 = Label( f, text= "%.2f" %
	( 100*float( progress[ "printTime" ] ) / ( float( progress[ "printTimeLeft" ] ) + float( progress[ "printTime" ] ) ) ) + "%",
	height=0, width=15, bd=1, relief=SUNKEN )
'''

lbl1 = Label( f, text="NO DATA", height=1, width=15, bd=1, relief=SUNKEN )
lbl2 = Label( f, text="NO DATA", height=2, width=15, bd=1, relief=SUNKEN )
lbl3 = Label( f, text="NO DATA", height=2, width=15, bd=1, relief=SUNKEN )
lbl4 = Label( f, text="NO DATA", height=0, width=15, bd=1, relief=SUNKEN )

lbl1.grid( row=0, columnspan=2, sticky="nesw" )

lbl4.grid( column=1, rowspan=3, sticky="nesw" )
lbl2.grid( row=1 )
lbl3.grid( row=2 )

lbl_temp0 = Label( f, text="NO DATA", height=0, width=15, bd=1, relief=SOLID ) #flat, groove, raised, ridge, solid, or sunken
lbl_temp0.grid( row=4, column=0 )

lbl_temp1 = Label( f, text="NO DATA", height=0, width=15, bd=1, relief=SOLID )
lbl_temp1.grid( row=4, column=1 )

cnv = Canvas( root, width=0, height=20 )


'''
lbl4.pack( fill="both", side=RIGHT )

lbl2.pack( fill=X, side=TOP )
lbl3.pack( fill=X, side=TOP )

lbl_temp0.pack( fill=X, side=BOTTOM )
lbl_temp1.pack( fill=X, side=BOTTOM )
'''




ToolTip(lbl1, follow_mouse=1, text="Print job file name", delay=500)
ToolTip(lbl2, follow_mouse=1, text="Print time gone by", delay=500)
ToolTip(lbl3, follow_mouse=1, text="Print time left", delay=500)
ToolTip(lbl4, follow_mouse=1, text="Print time percentage gone by", delay=500)

ToolTip(lbl_temp0, follow_mouse=1, text="Printhead temperature", delay=500)
ToolTip(lbl_temp1, follow_mouse=1, text="Bed temperature", delay=500)

ToolTip(cnv, follow_mouse=1, text="Print completion", delay=500)

cnv.pack( fill=X )

root.update(  )

width = cnv.winfo_width(  )
'''
cnv.create_rectangle( 0, 0, width*float( progress["completion"] ) / 100, 20, 
	fill=convert( [ 255-2.55*progress["completion"], 2.55*progress["completion"], 0 ] ) )
cnv.create_text( width/2, 10, text="%.2f" % float( progress[ "completion" ] ) + "%" )
'''

def task():
	global cnv, lbl, body, printer

	cnv.delete( ALL )

	try:

		body = get_body(  )
		progress = body[ "progress" ]

		printer = get_printer(  )
		temperature = printer[ "temperature" ]

		lbl1["text"]=body[ "job" ][ "file" ][ "name" ].split( ".gcode" )[ 0 ]

		lbl_temp0["text"]= str( temperature[ "tool0" ][ "actual" ] ) + "C / " + str( temperature[ "tool0" ][ "target" ] ) + "C"
		lbl_temp1["text"]= str( temperature[ "bed" ][ "actual" ] ) + "C / " + str( temperature[ "bed" ][ "target" ] ) + "C"

		lbl2["text"]=human( progress[ "printTime" ] )
		if progress["printTimeLeft"]:
			lbl3["text"]=human( progress[ "printTimeLeft" ] )
			lbl4["text"]="%.2f" % ( 100*float( progress[ "printTime" ] ) / ( float( progress[ "printTimeLeft" ] ) + float( progress[ "printTime" ] ) ) ) + "%"
		else:
			lbl3["text"]="No estimate"
			lbl4["text"]="No estimate"


		cnv.create_rectangle( 0, 0, width*float( progress["completion"] ) / 100, 20, 
			fill=convert( [ 255-2.55*progress["completion"], 2.55*progress["completion"], 0 ] ) )

		cnv.create_text( width/2, 10, text="%.2f" % float( progress[ "completion" ] ) + "%" )

		root.after(1500, task)

	except Exception as e:
		print e
		root.after(3000, task)


root.after(100, task)

root.lift(  )
root.call('wm', 'attributes', '.', '-topmost', '1')
root.mainloop(  )