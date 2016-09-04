from Tkinter import *
root = Tk(  )


def p( event ): 
	print "SPACECAT"

def p2( event ): 
	print "SPACECAT2222222"
	print event

btn1 = Button( root, text="PRESS ME!" )


btn1.bind( "<Button-1>", p )
btn1.bind( "<Button-3>", p2 )


btn1.pack( fill=X )



root.mainloop(  )