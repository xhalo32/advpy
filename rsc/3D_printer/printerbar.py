from tkinter import *
import json, time
from urllib.request import urlopen
from tooltip import ToolTip

	## MAIN ##

import os

f = open( os.path.join(os.path.expanduser('~'), "octoprint_config"), "r" )
apikey = f.readline(  )
printer_address = "".join( f.readline(  ).split("\n") )
f.close(  )

print(apikey, printer_address)

body = progress = printer = temperature = None


def get_body(  ):
	return json.loads(str(urlopen(printer_address + '/api/job?apikey=' + apikey).read()))
	
def get_printer(  ):
	return json.loads(str(urlopen(printer_address + '/api/printer?apikey=' + apikey).read()))

def convert( rgb ):
	rgb = [ int( c ) for c in rgb ]
	color = "#"
	for c in rgb:
		h = format( hex( c ).split( 'x' )[ 1 ] )
		if c < 16: h = "0"+h
		color += h

	if len( color ) != 7:return None
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

lbl1 = Label( f, text="NO DATA", height=1, width=15, bd=1, relief=RAISED )
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




ToolTip(lbl1, follow_mouse=1, text="Print name", delay=500)
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
	global cnv, lbl, body, printer,width

	cnv.delete( ALL )
	width = cnv.winfo_width(  )

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

	root.after(500, task)

root.after(1000, task)

root.lift(  )
root.call('wm', 'attributes', '.', '-topmost', '1')
root.mainloop(  )