import pygame as p
import time

from world import World
from message import Messages

p.init()

class Run(  ):

	def __init__( self ):

		self.size = ( 1024, 768 )
		self.scr = p.display.set_mode( self.size )
		self.world = World( self )

		self.active = True
		self.holdingSpace = False
		self.WFPS = 60
		self.FPSlist = [ self.WFPS ]

		self.events = [  ]

	def _shoot( self, args ):

		self.world.player.shoot( args[ 0 ], args[ 1 ], args[ 2 ], args[ 3 ] )

	def eventListener( self ):

		if p.mouse.get_pressed(  ) == ( 1, 0, 0 ):
			self.world.player.shoot( ( 0, 200, 0), self.world.s1.sliderpos, 15, self.world.s1.sliderpos )

		if p.mouse.get_pressed(  ) == ( 0, 0, 1 ) and self.world.player.rocketshoot_timer <= 0:
			self.world.player.rocketshoot(  )

		for e in self.events:
			if e.type == p.QUIT:
				self.active = False
				p.quit()
				quit()

			if e.type == p.KEYDOWN:
				if e.unicode == "d":
					self.world.player.vx = self.world.player.speed

				if e.unicode == "a":
					self.world.player.vx = -self.world.player.speed

				if e.unicode == "w":
					self.world.player.vy = -self.world.player.speed

				if e.unicode == "s":
					self.world.player.vy = self.world.player.speed

				if e.unicode == " ":
					self.holdingSpace = True

				if e.key == p.K_ESCAPE:
					self.active = False

			if e.type == p.KEYUP:
				if e.key == p.K_d and self.world.player.vx > 0:
					self.world.player.vx = 0

				if e.key == p.K_SPACE:
					self.holdingSpace = False

				if e.key == p.K_a and self.world.player.vx < 0:
					self.world.player.vx = 0

				if e.key == p.K_s and self.world.player.vy > 0:
					self.world.player.vy = 0

				if e.key == p.K_w and self.world.player.vy < 0:
					self.world.player.vy = 0

	def update( self ):

		self.world.update(  )

	def draw( self ):

		self.world.draw(  )

	def loop( self ):

		clk = p.time.Clock(  )

		while self.active:
			lasttime = time.time(  )

			self.events = p.event.get(  )

			self.eventListener(  )
			self.update(  )
			self.draw(  )

			FPS = 0
			for x in self.FPSlist:
				FPS += x

			Messages.message( self.scr, round( FPS / len( self.FPSlist ), 1 ), ( 10, 10 ), p.Color( 'magenta' ) )

			p.display.update(  )

			now = time.time(  )
			self.FPSlist.append( round( 1.0 / ( now - lasttime ), 0 ) )
			if len( self.FPSlist ) > 100: del self.FPSlist[ 0 ]

			clk.tick( self.WFPS )

r = Run()
try:pass
except: print "Exception"
r.loop()
	
p.quit(  )
quit(  )