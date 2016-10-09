import pygame as p
from message import *


class Points:

	def __init__( self, main ):

		self.main = main
		self.color = ( 100, 100, 100 )
		self.wincolor = ( 100, 200, 100 )

	def update( self ):

		pass

	def draw( self ):
		winner = None
		for i in range( len( self.main.handler.object_list ) ):

			if i > 0: 
				if self.main.handler.object_list[i].lenght > self.main.handler.object_list[i-1].lenght: winner = self.main.handler.object_list[i]
			elif self.main.handler.object_list[i].lenght > self.main.handler.object_list[-1].lenght: winner = self.main.handler.object_list[i]

		for obj in self.main.handler.object_list:
			pos = [ obj.snakelist[ -1 ][ 0 ], obj.snakelist[ -1 ][ 1 ] ]
			drawpos = [ pos[ 0 ], pos[ 1 ] + 30 ]

			while drawpos[ 1 ] + 10 > self.main.scr.get_height(  ): drawpos[ 1 ] -= 1


			if winner == obj:
				msg( self.main.scr, obj.lenght, drawpos, self.wincolor, 20, bold=1, centered=1 )
				
			if winner != obj:
				msg( self.main.scr, obj.lenght, drawpos, self.color, 15, bold=1, centered=1 )

