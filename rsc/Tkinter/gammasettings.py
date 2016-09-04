from Tkinter import *
import os

g=1.00
w=15

root = Tk()

f = Frame( root )
f.pack(  )

def add( e ):
	global g
	if e.num == 1: g += 0.1
	if e.num == 3: g += 0.01

	if e.num == 4: g += 0.01
	if e.num == 5: g -= 0.01

	lbl[ "text" ] = round( g, 2 )

def sub( e ):
	global g
	if e.num == 1: g -= 0.1
	if e.num == 3: g -= 0.01

	if e.num == 4: g += 0.01
	if e.num == 5: g -= 0.01

	lbl[ "text" ] = round( g, 2 )

def se( e ):
	global g
	os.system( "redshift -O 6200 -g " + str(g) )

def res( e ):
	global g
	g = 1.0
	lbl[ "text" ] = g
	os.system( "redshift -O 6200 -g 1" )

btn1 = Button( f, text="+", width=w )
btn2 = Button( f, text="-", width=w )
btn3 = Button( f, text="SET", width=w )
btn4 = Button( f, text="RESET", width=w )

lbl = Label( f, text=g, height=2, bd=1, relief=SUNKEN )

btn1.pack( fill=X )
btn2.pack( fill=X )
btn3.pack( fill=X )
btn4.pack( fill=X )

btn1.bind( "<Button>", add )
btn2.bind( "<Button>", sub )
btn3.bind( "<Button-1>", se )
btn4.bind( "<Button-1>", res )


lbl.pack( fill=X )


root.mainloop()