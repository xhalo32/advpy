import pygame as p
from random import *
from message import *



class Items:

	class Apple:

		def __init__( self, parent, vars="" ):

			self.parent = parent
			self.main = self.parent.main
			self.radius = 7
			
			self.pos = [ int( random(  ) * ( self.main.scr.get_width(  ) - 20 ) + 10 ), int( random(  ) * ( self.main.scr.get_height(  ) - 20 ) + 10 ) ]
			self.grid_index = self.main.get_gindex( self.pos )

			self.dead = 0

			for var in vars:
				try: setattr( self, var, vars[ var ] )
				except Exception as e: print e

		def update( self ):
			pass

		def draw( self ):

			p.draw.circle( self.main.scr, [ 255, 50, 50 ], self.pos, self.radius )


			
			if self.main.debug:
				msg(	self.main.scr, 
						str(self.grid_index[ 0 ]) + " " + str(self.grid_index[ 1 ]), 
						[ self.pos[ 0 ], self.pos[ 1 ] + 20], 
						( 0,0,0 ),
						15,
						centered=True 
				)



	class Speedcandy:

		def __init__( self, parent, vars="" ):

			self.parent = parent
			self.main = self.parent.main
			self.radius = 7

			self.addr = 1
			self.addg = 0
			self.addb = 0
			self.colourspeed = 40

			self.r = 0
			self.g = 255
			self.b = 255
			
			self.pos = [ int( random(  ) * ( self.main.scr.get_width(  ) - 20 ) + 10 ), int( random(  ) * ( self.main.scr.get_height(  ) - 20 ) + 10 ) ]
			self.grid_index = self.main.get_gindex( self.pos )

			self.dead = 0

			for var in vars:
				try: setattr( self, var, vars[ var ] )
				except Exception as e: print e

		def update( self ):


			if not self.addr: self.r -= self.colourspeed
			if not self.addg: self.g -= self.colourspeed
			if not self.addb: self.b -= self.colourspeed

			if self.addg: self.g += self.colourspeed
			if self.addr: self.r += self.colourspeed
			if self.addb: self.b += self.colourspeed

			if self.r > 255: self.r = 255
			if self.g > 255: self.g = 255
			if self.b > 255: self.b = 255

			if self.r < 0: self.r = 0
			if self.g < 0: self.g = 0
			if self.b < 0: self.b = 0


			if self.r <= 0 and self.g >= 255: self.addr = 1; self.addg = 0
			if self.g <= 0 and self.b >= 255: self.addg = 1; self.addb = 0
			if self.b <= 0 and self.r >= 255: self.addb = 1; self.addr = 0


		def draw( self ):

			p.draw.circle( self.main.scr, [self.r, self.g, self.b], self.pos, self.radius )


			
			if self.main.debug:
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
		self.appleamount = 10
		self.applespeed = 2

		self.speedcandylist = [  ]
		self.speedcandyamount = 5
		self.speedcandyspeed = 1



	def generate( self, t, *arguments ):

		try: getattr( self, t.lower(  ) + "list" ).append( getattr( self, t )( self, *arguments ) )
		except Exception as e: 	print e

	def clearall( self ):

		self.applelist = [  ]
		self.speedcandylist = [  ]

	def update( self ):

		tl = [  ]
		for a in self.applelist:
			a.update(  )
			if not a.dead: tl.append( a )
		self.applelist = tl


		tl = [  ]
		for a in self.speedcandylist:
			a.update(  )
			if not a.dead: tl.append( a )
		self.speedcandylist = tl

	def draw( self ):

		for a in self.applelist:
			a.draw(  )

		for a in self.speedcandylist:
			a.draw(  )