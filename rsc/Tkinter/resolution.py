from Tkinter import *
from subprocess import *
import os

def se( e ):
	global comm
	hit = e.widget[ "text" ]
	lbl[ "text" ] = hit
	comm = "xrandr --output " + display + " --mode " + hit
	os.system( comm )

def change_display( e ):
	global display
	display = e.widget[ "text" ]
	dlbl[ "text" ] = display
	update_reslist(  )

	


text = check_output( [ 'xvidtune', '-show' ] ).split( '"' )[ 1 ]

dlist = [  ]
xrand = check_output( [ 'xrandr' ] ).split( "\n" )
for line in xrand:
	if " connected" in line:
		#print line
		display = line.split( " " )[ 0 ]
		dlist.append( display )

w = 10
display = dlist[ -1 ]

reslist = [  ]
def update_reslist(  ):
	global reslist
	reslist = [  ]
	xrand = check_output( [ 'xrandr' ] ).split( "\n" )
	index = 0
	for n in range( len( xrand ) ):
		if display in xrand[ n ]: index = n

	for i in range( 1, 8 + 1 ):
		reslist.append( xrand[ index+i ].split( "   " )[ 1 ] )

	reslist.append( "1440x1080" )

update_reslist(  )
root = Tk()



f = Frame( root )
f.pack(  )


def poop( e ):
	top = Toplevel( relief=SUNKEN )
	top.title( "CHOOSE A DISPLAY" )
	for b in dlist:

		btn = Button( top, text=b, width=w // 2 )
		btn.pack( fill=X )
		btn.bind( "<Button-1>", change_display )


dlbl = Label( f, text=display, height=2, bd=1, relief=SUNKEN )
dlbl.pack( fill=X )
dlbl.bind( "<Button-1>", poop )

for b in reslist:

	btn = Button( f, text=b, width=w )
	btn.pack( fill=X )
	btn.bind( "<Button-1>", se )

lbl = Label( f, text=text, height=2, bd=1, relief=SUNKEN )
lbl.pack( fill=X )


root.mainloop()