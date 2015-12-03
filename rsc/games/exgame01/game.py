import pygame as pg
import time

class Game:

	def __init__( self, scr, loop ):

		self.scr = scr

		from block import Block
		self.block = Block( scr )

		from message import Messages
		self.msg = Messages( self.scr )

		self.loop = loop

		self.FPS = 60

		self.block( self, self.loop )

		print self, 'INITIALIZED' 

	def update( self ):

		clock = pg.time.Clock(  )

		while self.loop.run:

			lasttime = time.time(  )

			self.block.update( self.FPS )

			self.FPS = 1.0 / ( time.time(  ) - lasttime )

			clock.tick( 60 )

	def draw( self ):

		scr = self.scr
		scr.fill( ( 35, 35, 35 ) )

		self.block.draw(  )
		self.msg.message( round( self.FPS, 1 ), ( 10, 10 ) )