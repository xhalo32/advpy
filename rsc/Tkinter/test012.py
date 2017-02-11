	from Tkinter import *

root = Tk(  )

cnv = Canvas( root, width=300, height=200 )
cnv.pack(  )


cnv.create_line( 0, 0, cnv["width"], cnv["height"] )
cnv.create_line( 0, 100, cnv["width"], cnv["height"], fill="red" )
cnv.create_line( 0, 150, cnv["width"], cnv["height"], fill="cyan" )



cnv.create_rectangle( 30, 40, 100, 100, fill="chartreuse" )

	# ORDER OF OBJECT 
cnv.delete( 2 )


root.mainloop(  )