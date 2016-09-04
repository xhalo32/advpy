from Tkinter import *
root = Tk(  )


def p(  ): print "NIGGGGA"

btn1 = Button( root, text="PRESS ME!", command=p )
btn1.pack( fill=X )


def p2( event ): 
	print "SPACECAT"

btn1 = Button( root, text="PRESS ME!" )
btn1.bind( "<Button-3>", p2 )
btn1.pack( fill=X )



root.mainloop(  )