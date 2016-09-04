from Tkinter import *

root = Tk(  )


photo = PhotoImage( file="check.png" )
photo = photo.subsample( 10 )

lbl = Label( root, image=photo )
lbl.pack(  )


root.mainloop(  )