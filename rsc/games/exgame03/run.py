import pygame as p
from pygame.locals import *
import time

from world import World
from message import Messages

p.init(  )
p.display.init(  )
debug = False

class Run(  ):

	def __init__( self ):

		if debug:
			self.size = ( 900, 700 )
			self.scr = p.display.set_mode( self.size )
		else:
			self.size = ( 1920, 1080 )
			self.scr = p.display.set_mode( self.size, FULLSCREEN )

		strings = ( 
			"      ....      ",
			"     .xxxx.     ",
			"     .xxxx.     ",
			"    .xx  xx.    ",
			"    .xx  xx.    ",
			"   .xx    xx.   ",
			"   .xx    xx.   ",
			"  .xx      xx.  ",
			"  .xx      xx.  ",
			" .xx        xx. ",
			" .xx        xx. ",
			".xx          xx.",
			".xx          xx.",
			".xxxxxxxxxxxxxx.",
			" .xxxxxxxxxxxx. ",
			" .............. ",
			)

		data, mask = p.cursors.compile( strings, 'x', '.', 'o' )
		p.mouse.set_cursor( ( 16, 16 ), ( 0, 0 ), data, mask )
		#p.mouse.set_cursor( *p.cursors.ball )

		self.world = World( self )

		self.active = True
		self.holdingSpace = False
		self.WFPS = 60
		self.FPSlist = [ self.WFPS ]

		self.events = [  ]

	def eventListener( self ):

		if p.mouse.get_pressed(  ) == ( 1, 0, 0 ) and self.world.player.shoot_timer < 0:
			self.world.player.shoot( {
			"dad" : self.world.player,
			"color" : ( 250, 250, 0 ),
			"colorindex" : ( 20, 100, 0 ),
			"angle" : self.world.player.rotation,
			"radius" : self.world.s1.sliderpos,
			"speed" : 7,
			"damage" : 3,
			"lifetime" : 90,
			"pos" : self.world.player.pos,
			}  )
			self.world.player.shoot_timer = 2

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