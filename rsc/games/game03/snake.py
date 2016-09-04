import pygame as p



class Snake:

	def __init__( self, main, vars ):

		self.main = main

		self.pos = [ self.main.scr.get_width(  ) // 2, self.main.scr.get_height(  ) // 2 ]
		self.speed = [ 0, 0 ]
		self.radius = 10
		self.spd = 2
		self.color = ( 0, 200, 100 )

		self.UP = p.K_w
		self.DN = p.K_s
		self.LT = p.K_a
		self.RT = p.K_d

		self.snakelist = [  ]
		self.lenght = 5

		for var in vars:
			try: setattr( self, var, vars[ var ] )
			except Exception as e: print e

	def update( self ):

		for e in self.main.handler.events:

			if e.type == p.KEYDOWN:

				if e.key == self.UP and self.speed[ 1 ] == 0: self.speed[ 1 ] = -self.spd	;self.speed[ 0 ] = 0
				if e.key == self.DN and self.speed[ 1 ] == 0: self.speed[ 1 ] =  self.spd	;self.speed[ 0 ] = 0
				if e.key == self.LT and self.speed[ 0 ] == 0: self.speed[ 0 ] = -self.spd	;self.speed[ 1 ] = 0
				if e.key == self.RT and self.speed[ 0 ] == 0: self.speed[ 0 ] =  self.spd	;self.speed[ 1 ] = 0

		for dim in range( 2 ):
			if self.pos[ dim ] <= 0: self.pos[ dim ] = self.main.scr.get_size(  )[ dim ] - 1
			elif self.pos[ dim ] >= self.main.scr.get_size(  )[ dim ]: self.pos[ dim ] = 1

		self.pos[ 0 ] += self.speed[ 0 ]
		self.pos[ 1 ] += self.speed[ 1 ]

		self.snakelist.append( list( self.pos ) )
		if len( self.snakelist ) > self.lenght: del self.snakelist[ 0 ]

	def draw( self ):

		#for part in self.snakelist:
		#	p.draw.circle( self.main.scr, ( 255, 0, 0 ), part, self.radius )


		for n in range(len(self.snakelist)):

			p.draw.circle( self.main.scr, self.color, self.snakelist[n], self.radius )