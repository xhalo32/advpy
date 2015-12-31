import pygame as p
from message import Messages

def init( self ):
	self.updatelasttime = self.updatenowtime = 0
	self.drawlasttime = self.drawnowtime = 0
	self.loopnow = self.looplast = 0
	self.updatefpslist = [  ]
	self.drawfpslist = [  ]
	self.totalfpslist = [  ]
	self.loopfpslist = [  ]
	self.debug = 1
	self.debugall = 1
	self.updatefps = 0
	self.drawfps = 0
	self.totalfps = 0
	self.loopfps = 0

def calcfps( self ):

	try:
		fps = self.loopnow - self.looplast
		self.loopfpslist.append( 1.0 / fps )

		loopfps = 0
		for i in self.loopfpslist:
			loopfps += i	
			self.loopfps = loopfps
		if len( self.loopfpslist ) > 64:
			del self.loopfpslist[ 0 ]
	except:
		pass

def calcupdatefps( self ):

	try:
		fps = self.updatenowtime - self.updatelasttime
		self.updatefpslist.append( 1.0 / fps )

		updatefps = 0
		for i in self.updatefpslist:
			updatefps += i	
			self.updatefps = updatefps
		if len( self.updatefpslist ) > 64:
			del self.updatefpslist[ 0 ]
	except:
		pass

def printfps( self ):

	if self.timer % 60 == 0:
		loopfps = 0
		for i in self.loopfpslist:
			loopfps += i	
		self.loopfps = loopfps

	try: Messages.message( self.s, round( self.loopfps / len( self.loopfpslist ), 1 ), [ 10, 30 ], ( 200, 0, 0 ) )
	except: pass

	try: Messages.message( self.s, round( self.updatefps / len( self.updatefpslist ), 1 ), [ 10, 10 ], ( 0, 255, 0 ) )
	except: pass

def printall( self ):

	printfps( self )

	if self.timer % 30 == 0:
		updatefps = 0
		for i in self.updatefpslist:
			updatefps += i
		self.updatefps = updatefps

	if self.timer % 30 == 0:
		drawfps = 0
		for i in self.drawfpslist:
			drawfps += i
		self.drawfps = drawfps

	if self.timer % 30 == 0:
		totalfps = 0
		for i in self.totalfpslist:
			totalfps += i	
		self.totalfps = totalfps

	try: Messages.message( self.scr, round( self.updatefps / len( self.updatefpslist ), 1 ), [ 10, 10 ], ( 0, 0, 0 ) )
	except: pass

	try: Messages.message( self.scr, round( self.drawfps / len( self.drawfpslist ), 1 ), [ 10, 30 ], ( 0, 0, 0 ) )
	except: pass
	
	try: Messages.message( self.scr, round( self.totalfps / len( self.totalfpslist ), 1 ), [ 10, 50 ], ( 0, 0, 0 ) )
	except: pass

	try: Messages.message( self.scr, 1.0 / ( self.updatefps / len( self.updatefpslist ) ) * 1000, [ 120, 10 ], ( 0, 0, 0 ) )
	except: pass

	try: Messages.message( self.scr, 1.0 / ( self.drawfps / len( self.drawfpslist ) ) * 1000, [ 120, 30 ], ( 0, 0, 0 ) )
	except: pass

	try: Messages.message( self.scr, 1.0 / ( self.totalfps / len( self.totalfpslist ) ) * 1000, [ 120, 50 ], ( 0, 0, 0 ) )
	except: pass