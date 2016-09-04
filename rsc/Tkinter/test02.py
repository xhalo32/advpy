from Tkinter import *
root = Tk(  )



tF = Frame( root )
tF.pack( side=TOP )

bF = Frame( root )
bF.pack( side=BOTTOM )

btn1 = Button( tF, text="--A--", fg="red", bg="blue" )
btn2 = Button( tF, text="--B--", fg="blue", bg="red" )
btn3 = Button( tF, text="--C--", fg="magenta" )
btn4 = Button( bF, text="--D--", fg="green" )

btn1.pack( side=LEFT )
btn2.pack( side=LEFT )
btn3.pack( side=LEFT )
btn4.pack( side=BOTTOM )


root.mainloop(  )