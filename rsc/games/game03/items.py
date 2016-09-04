import pygame as p
from random import *
from message import *



class Items:

	class Apple:

		def __init__( self, parent, pos ):

			self.parent = parent
			self.main = self.parent.main
			self.pos = pos
			self.radius = 10
			self.grid_index = self.main.get_gindex( self.pos )
			print self.grid_index

			self.dead = 0

		def update( self ):
			pass

		def draw( self ):

			p.draw.circle( self.main.scr, [ 255, 50, 50 ], self.pos, 10 )

			msg(	self.main.scr, 
					str(self.grid_index[ 0 ]) + " " + str(self.grid_index[ 1 ]), 
					[ self.pos[ 0 ], self.pos[ 1 ] + 20], 
					( 0,0,0 ),
					15,
					centered=True 
			)





	def __init__( self, main ):

		self.main = main

		self.applelist = [  ]



	def generate( self, t, *arguments ):

		try: 		getattr( self, t.lower(  ) + "list" ).append( getattr( self, t )( self, *arguments ) )
		except Exception as e: 	print e

	def update( self ):

		tl = [  ]
		for a in self.applelist:
			a.update(  )
			if not a.dead: tl.append( a )
		self.applelist = tl

	def draw( self ):

		for a in self.applelist:
			a.draw(  )