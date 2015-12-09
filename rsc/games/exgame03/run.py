import pygame as p
import threading
import time

from player import Player
from enemy import Enemy
from message import Messages
from stars import Stars
from projectile import Projectile
from pg_enhancements import Button, Slider, Decorations
from complex import complex

p.init()

class Run(  ):

	def __init__( self ):

		self.size = ( 1000, 800 )
		self.scr = p.display.set_mode( self.size )
		self.projectile = Projectile( self )
		self.player = Player( self )
		self.enemyC = Enemy( self )

		self.entitylist = [  ]

		self.bg = p.Color( "black" )
		self.active = True
		self.holdingSpace = False
		self.WFPS = 60
		self.FPSlist = [ self.WFPS ]

		self.events = [  ]

		self.b1 = Button( {
			"window" : self.scr,
			"pos" : [ 250, 250, 50, 30 ],
			"color" : ( 0, 255, 200 ),
			"clickcolor" : ( 0, 200, 150 ),
			"message" : "HEY",
			"font" : { "type" : "Arial", "size" : 25, "clicksize" : 10 },
			"action" : self._shoot,
			"args" : ( ( 255, 255, 255 ), 1, 4, .1 ),
			} )

		self.s1 = Slider( {
			"window" : self.scr,
			"pos" : [ 500, 500, 50, 30 ],
			"color" : ( 0, 255, 200 ),
			"color2" : ( 255, 0, 55 ),
			"colorindex" : 100,
			"steps" : { "startpoint" : 1, "endpoint" : 10 },
			"font" : { "size" : 15, "clicksize" : 20 }
			} )

		self.f1 = Decorations.Flag( {
			"window" : self.scr,
			"pos" : [ 400, 200, 40, 40 ],
			"color" : ( 255, 255, 255 ),
			"speed" : 1,
			"rotspeed" : 4,
			"direction" : 1,
			} )

	def _shoot( self, args ):

		self.player.shoot( args[ 0 ], args[ 1 ], args[ 2 ], args[ 3 ] )

	def eventListener( self ):

		if p.mouse.get_pressed(  ) == ( 1, 0, 0 ):
			self.player.shoot( ( 0, 200, 0), self.s1.sliderpos, 15, .1 )

		for e in self.events:
			if e.type == p.QUIT:
				self.active = False
				p.quit()
				quit()

			if e.type == p.KEYDOWN:
				if e.unicode == "d":
					self.player.vx = self.player.speed

				if e.unicode == "a":
					self.player.vx = -self.player.speed

				if e.unicode == "w":
					self.player.vy = -self.player.speed

				if e.unicode == "s":
					self.player.vy = self.player.speed

				if e.unicode == " ":
					self.holdingSpace = True

			if e.type == p.KEYUP:
				if e.key == p.K_d and self.player.vx > 0:
					self.player.vx = 0

				if e.key == p.K_SPACE:
					self.holdingSpace = False

				if e.key == p.K_a and self.player.vx < 0:
					self.player.vx = 0

				if e.key == p.K_s and self.player.vy > 0:
					self.player.vy = 0

				if e.key == p.K_w and self.player.vy < 0:
					self.player.vy = 0

	def restart( self ):

		self.__init__(  )

	def update( self ):

		self.entitylist = [ self.player ] + [ e for e in self.enemyC.opponentlist ]

		self.player.update(  )
		self.enemyC.update(  )
		self.projectile.udpate(  )

		if self.holdingSpace:
			self.player.shoot( ( 0, 255, 100 ), 2, 10, 1 )

		self.b1.pos[ 0 ] -= self.player.vx / 3.0
		self.b1.pos[ 1 ] -= self.player.vy / 3.0

		self.s1.pos[ 0 ] -= self.player.vx / 3.0
		self.s1.pos[ 1 ] -= self.player.vy / 3.0

		self.f1.pos[ 0 ] -= self.player.vx / 3.0
		self.f1.pos[ 1 ] -= self.player.vy / 3.0

		Stars.update( self )

		self.b1.getClicked(  )
		self.s1.update(  )

	def draw( self ):

		self.scr.fill( self.bg )
		Stars.draw(  )

		self.b1.draw(  )
		self.s1.draw(  )
		self.f1.draw(  )

		self.projectile.draw(  )
		self.player.draw(  )
		self.enemyC.draw(  )

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
r.loop()

p.quit(  )
quit(  )