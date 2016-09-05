import pygame as p
from pg_enhancements import *
from message import *
from math import *




class Snake:

	def __init__( self, main, vars ):

		self.main = main

		self.pos = [ self.main.scr.get_width(  ) // 2, self.main.scr.get_height(  ) // 2 ]
		self.speed = [ 0, 0 ]
		self.radius = 10
		self.hitradius = 5
		self.spd = 2
		self.color = [ 0, 200, 100 ]
		self.color2 = [ 200, 100, 200 ]
		self.fade = 1
		self.cooldown = 0

		self.UP = p.K_w
		self.DN = p.K_s
		self.LT = p.K_a
		self.RT = p.K_d

		self.snakelist = [  ]
		self.lenght = 100
		self.grid_index = self.main.get_gindex( self.pos )


		self.dead = 0

		for var in vars:
			try: setattr( self, var, vars[ var ] )
			except Exception as e: print e

	def update( self ):

		if self.cooldown>0: self.cooldown -= 1
		self.grid_index = self.main.get_gindex( self.pos )



		for e in self.main.handler.events:

			if e.type == p.KEYDOWN and self.cooldown <= 0:

				if e.key == self.UP and self.speed[1] == 0: self.speed[1] = -self.spd;self.speed[0] = 0; self.cooldown = self.hitradius / float(self.spd) * 2
				if e.key == self.DN and self.speed[1] == 0: self.speed[1] =  self.spd;self.speed[0] = 0; self.cooldown = self.hitradius / float(self.spd) * 2
				if e.key == self.LT and self.speed[0] == 0: self.speed[0] = -self.spd;self.speed[1] = 0; self.cooldown = self.hitradius / float(self.spd) * 2
				if e.key == self.RT and self.speed[0] == 0: self.speed[0] =  self.spd;self.speed[1] = 0; self.cooldown = self.hitradius / float(self.spd) * 2

		for dim in range( 2 ):
			if self.pos[ dim ] <= 0: self.pos[ dim ] = self.main.scr.get_size(  )[ dim ] - 1
			elif self.pos[ dim ] >= self.main.scr.get_size(  )[ dim ]: self.pos[ dim ] = 1

		self.pos[ 0 ] += self.speed[ 0 ]
		self.pos[ 1 ] += self.speed[ 1 ]




		self.snakelist.append( list( self.pos ) )
		if len( self.snakelist ) > self.lenght: del self.snakelist[ 0 ]


		for part in self.snakelist[: - 2 * self.hitradius]:
			if self.pos[ 0 ] - 2 * self.hitradius < part[ 0 ] < self.pos[ 0 ] + 2 * self.hitradius:
				if self.pos[ 1 ] - 2 * self.hitradius < part[ 1 ] < self.pos[ 1 ] + 2 * self.hitradius:
					self.dead = 1

		for a in self.main.handler.items.applelist:
			if 	a.grid_index ==   self.grid_index 									   or \
				a.grid_index == [ self.grid_index[ 0 ] - 1, self.grid_index[ 1 ] 	 ] or  \
				a.grid_index == [ self.grid_index[ 0 ] + 1, self.grid_index[ 1 ] 	 ] or   \
				a.grid_index == [ self.grid_index[ 0 ]	  , self.grid_index[ 1 ] - 1 ] or    \
				a.grid_index == [ self.grid_index[ 0 ]	  , self.grid_index[ 1 ] + 1 ]:

				if self.pos[ 0 ] - self.hitradius < a.pos[ 0 ] + a.radius and self.pos[ 0 ] + self.hitradius > a.pos[ 0 ] - a.radius:
					if self.pos[ 1 ] - self.hitradius < a.pos[ 1 ] + a.radius and self.pos[ 1 ] + self.hitradius > a.pos[ 1 ] - a.radius:
						a.dead = 1

						self.lenght += a.radius

		for s in self.main.handler.object_list:
			if type( s ) == type( self ) and s != self:

				delta = floor( len( s.snakelist ) / float( self.radius ) ) * s.spd
				print delta


				for i in range( int( delta ) ):

					index = int( i * self.radius / float( s.spd ) )

					if self.grid_index == self.main.get_gindex( s.snakelist[ index ] ):

						if self.pos[ 0 ] - self.hitradius < s.snakelist[ index ][ 0 ] + s.hitradius and \
						self.pos[ 0 ] + self.hitradius > s.snakelist[ index ][ 0 ] - s.hitradius:

							if self.pos[ 1 ] - self.hitradius < s.snakelist[ index ][ 1 ] + s.hitradius and \
							self.pos[ 1 ] + self.hitradius > s.snakelist[ index ][ 1 ] - s.hitradius:

								
								self.dead = 1

								s.lenght += self.lenght // 2



		if self.dead:
			self.main.handler.effects.mkExplosion( self.color, [a/2. for a in self.color], self.radius / 6., self.spd, 50, 120, self.pos )



	def draw( self ):

		#for part in self.snakelist:
		#	p.draw.circle( self.main.scr, ( 255, 0, 0 ), part, self.radius )


		for n in range(len(self.snakelist)):

			if self.fade:
				c = [ 
					( float( n ) / len( self.snakelist ) ) * ( self.color[ 0 ] - self.color2[ 0 ] ) + self.color2[ 0 ],
					( float( n ) / len( self.snakelist ) ) * ( self.color[ 1 ] - self.color2[ 1 ] ) + self.color2[ 1 ],
					( float( n ) / len( self.snakelist ) ) * ( self.color[ 2 ] - self.color2[ 2 ] ) + self.color2[ 2 ],
				 ]

				p.draw.circle( self.main.scr, c, self.snakelist[n], self.radius )

			elif not self.fade:
				c = self.color
				p.draw.circle( self.main.scr, c, self.snakelist[n], self.radius )

		msg(	self.main.scr, 
				str(self.grid_index[ 0 ]) + " " + str(self.grid_index[ 1 ]), 
				[ self.pos[ 0 ], self.pos[ 1 ] + 20], 
				( 0,0,0 ),
				15,
				centered=True 
		)