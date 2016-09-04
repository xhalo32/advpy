from Tkinter import *

def nothin(  ):
	print "VODKA!"

def addvodka(  ):
	print "TEQUILA"


i = 0


def oneup( e ):
	global i
	status[ "text" ] = "PREPARE FO NOTHIN!!!!    " + str( i )
	i += 1


root = Tk(  )

status = Label( root, text="PREPARE FO NOTHIN!!!!", bd=1, relief=SUNKEN, anchor=W )
status.pack( side=BOTTOM, fill=X )

status.bind( "<Button-1>", oneup )


root.mainloop(  )