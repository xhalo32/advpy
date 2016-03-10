import pygame as pg
import threading as thd
import time
import message

pg.init()
colour = pg.Color

clock = pg.time.Clock(  ) 

class Loop:

	def __init__( self ):

		from game import Game
		self.scr = pg.display.set_mode( ( 800, 600 ), pg.RESIZABLE )
		self.WFPS = 50

		self.game = Game( self.scr, self )
		self.run = True
		self.toreset = 0
		self.msg = message.Messages( self.scr )

	def gameloop( self ):

		self.keepmoving = 0
		
		try:
			while self.run:

				for e in pg.event.get():
					if e.type == pg.QUIT:
						self.run = False
					if e.type == pg.KEYDOWN and e.key == pg.K_r:
						self.toreset = 1
					if e.type == pg.KEYDOWN and e.key == pg.K_ESCAPE:
						self.run = 0

				self.game.update(  )

				if pg.mouse.get_pressed()[ 0 ]: self.game.block.move(  )
				if not pg.mouse.get_pressed()[ 0 ]: self.game.block.release(  )
				if pg.mouse.get_pressed()[ 2 ]: self.game.block.create_unit(  )

				self.game.draw(  )

				pg.display.flip(  )

				clock.tick( self.WFPS )

				if self.toreset:
					self.init( self.scr )
		except:
			self.run = False

loop = Loop(  )

loop.gameloop(  )

pg.quit(  )
quit(  )