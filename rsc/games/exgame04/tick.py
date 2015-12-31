import pygame as p
import sys, math, time, random
sys.path.append( "/home/toor/Desktop/advpy/rsc/" )
from acomplex import acomplex
from message import Messages
import fps

rad = 180.0 / math.pi

def teste( events, type, key ):

	if type == "D":
		type = "KEYDOWN"
	if type == "U":
		type = "KEYUP"

	try:
		for e in events:
			if e.type == getattr( p, type ) and e.key == getattr( p, key ):
				return True
	except:
		pass
	return False

class Tick:

	def init( self ):

		self.hold_lshift = 0

	def update( self ):
		self.updatelasttime = time.time(  )

		self.timer += 1
		if teste( self.events, "D", "K_ESCAPE" ): self.active = False

		if teste( self.events, "D", "K_d" ): self.vx = 5
		if teste( self.events, "D", "K_a" ): self.vx = -5
		if teste( self.events, "D", "K_w" ): self.vy = -5
		if teste( self.events, "D", "K_s" ): self.vy = 5

		if teste( self.events, "D", "K_LSHIFT" ):
			self.hold_lshift = True
		if teste( self.events, "U", "K_LSHIFT" ):
			self.hold_lshift = False

		if teste( self.events, "D", "K_F3" ) and self.hold_lshift: self.debugall *= -1; self.debug = 1
		elif teste( self.events, "D", "K_F3" ): self.debug *= -1; self.debugall = 1

		if teste( self.events, "U", "K_d" ) and self.vx > 0: self.vx = 0
		if teste( self.events, "U", "K_a" ) and self.vx < 0: self.vx = 0
		if teste( self.events, "U", "K_w" ) and self.vy < 0: self.vy = 0
		if teste( self.events, "U", "K_s" ) and self.vy > 0: self.vy = 0


		mpos = p.mouse.get_pos(  )
		try:
			self.rot = math.atan2( mpos[ 0 ] - self.x, mpos[ 1 ] - self.y ) * rad + 180
		except: pass

		self.x += self.vx
		self.y += self.vy

		self.updatenowtime = time.time(  )

	def draw( self ):

		self.drawlasttime = time.time(  )


		self.scr.fill( ( 255, 255, 255 ) )

		acomplex.atriangle( self.scr, ( 0, 255, 0 ), [ self.x, self.y ], 15,
			self.rot - 90, usecenter=1 )

		self.drawnowtime = time.time(  )
		self.loopnow = self.drawnowtime

		fps.calcfps( self )

		self.looplast = time.time(  )

		if self.debug - 1:
			fps.printfps( self )

		if self.debugall - 1:
			fps.printall( self )

		p.display.flip(  )