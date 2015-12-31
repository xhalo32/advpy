import pygame as p
from pygame.locals import *



class Main:

	def __init__( self ):
		self.size = ( 640, 480 )
		self.scr = p.display.set_mode( self.size )
		self.reset(  )

	def reset( self ):
		self.objectlist = [  ]
		from player import Player
		from block import Blocks
		from enemy import Enemies
		self.player = Player( self )
		self.playerlist = [ self.player ]
		self.blocks = Blocks( self )
		self.enemies = Enemies( self )

		self.active = True

	def update( self ):
		self.player.update(  )
		self.enemies.update(  )
		self.blocks.update(  )

	def draw( self ):
		self.scr.fill( ( 31, 31, 31 ) )

		self.blocks.draw(  )
		self.player.draw(  )
		self.enemies.draw(  )

		p.display.flip(  )

	def loop( self ):
		c = p.time.Clock(  )
		while self.active:

			self.events = p.event.get(  )

			self.update(   )
			self.draw(  )

			c.tick( 60 )


m = Main(  )
m.loop(  )