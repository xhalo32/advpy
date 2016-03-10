import pygame as p
from time import time
import game

p.init(  )

class run:

	def __init__( self ):

		self.lt = time(  )

		self.scr = p.display.set_mode( ( 1920, 1080 ), p.FULLSCREEN ) # p.NOFRAME
		self.game = game.Game( self )

		self.start(  )

	def start( self ):

		self.running = True
		self.starttime = time(  )
		clock = p.time.Clock(  )
		self.lt = time(  )

		while self.running:

			self.tick(  )
			self.draw(  )

			clock.tick( 60 )
			self.lt = time(  )

	def tick( self ):

		self.events = p.event.get(  )

		for e in self.events:
			if e.type == p.QUIT: self.running = False; print "QUIT"

		self.game.tick(  )

	def draw( self ):

		self.scr.fill( ( 0,0,0 ) )

		self.game.draw(  )

		p.display.flip(  )