import pygame as p


import time
from random import *
from handler import *
from math import *

from message import *

import utils


p.init(  )
p.font.init(  )


class Main:

	def __init__( self ):

		self.size = ( 800, 600 )
		self.scr = p.display.set_mode( self.size )#, p.FULLSCREEN )
		self.active = 1

		self.reset(  )

		self.loop(  )

	def reset( self ):
		# wasd = 119 97 115 100
		# uldr = 273 276 274 275

		self.handler = Handler( self )
		
		self.handler.create_player( pos=[ 400, 500 ], color=( 100, 200, 50 ), ULDR=( 119,97,115,100 ) )

		#self.handler.create_arrow( pos=[ 400, 0 ], color=( 20, 25, 255 ), button="U", owner=self.handler.playerlist[ 0 ] )

	def loop( self ):

		clk = p.time.Clock(  )

		while self.active:

			self.handler.update(  )

			self.scr.fill( [ x + 121 for x in ( 0,0,0 ) ] )

			self.handler.draw(  )

			clk.tick( 60 )
			

			p.display.update(  )