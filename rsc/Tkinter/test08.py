from Tkinter import *



class C:

	def __init__( self, master ):
		self.frm = Frame( master, width=300, height=200 )
		self.frm.pack(  )

		self.pbtn = Button( self.frm, text="PRESS ME!", command=self.print_msg )
		self.pbtn.pack( side=LEFT )

		self.qbtn = Button( self.frm, text="RAGE QUIT!!!!", command=self.frm.quit )
		self.qbtn.pack( side=LEFT )

		self.clicks = 0


	def print_msg( self ):
		self.pbtn[ "text" ]="   -->    "
		self.clicks += 1

		if self.clicks > 10: self.pbtn[ "text" ]="WHATS CHA DOIN M8"
		if self.clicks > 20: self.pbtn[ "text" ]="STOP IT"





root = Tk(  )

c = C( root )




root.mainloop(  )