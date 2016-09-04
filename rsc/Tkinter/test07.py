from Tkinter import *
root = Tk(  )

def lc( e ): print "LEFT"
def mc( e ): print "MIDDLE"
def rc( e ): print "RIGHT"


F = Frame( root, width=300, height=200, bg=(  ) )


F.bind( "<Button-1>", lc )
F.bind( "<Button-2>", mc )
F.bind( "<Button-3>", rc )


F.pack( side=TOP )


root.mainloop(  )