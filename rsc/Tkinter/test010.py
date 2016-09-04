from Tkinter import *

def nothin(  ):
	print "VODKA!"

def addvodka(  ):
	printputin = Button( toolbar, text="ruski", command=nothin )
	printputin.pack( side=LEFT, padx=2, pady=2 )


root = Tk(  )

toolbar = Frame( root )

insertputin = Button( toolbar, text="???", command=nothin )
insertputin.pack( side=LEFT, padx=2, pady=2 )

printputin = Button( toolbar, text="print???", command=addvodka )
printputin.pack( side=LEFT, padx=2, pady=2 )

toolbar.pack( side=TOP, fill=X )


root.mainloop(  )