from Tkinter import *
root = Tk(  )


a = Label( root, text="A", bg="gray" )
a.pack(  )

b = Label( root, text="B", bg="gray" )
b.pack( fill=X )

c = Label( root, text="C", bg="gray" )
c.pack( fill=Y, side=LEFT )



root.mainloop(  )