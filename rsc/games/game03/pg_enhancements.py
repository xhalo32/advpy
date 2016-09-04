import pygame as p
import math, random






class Effect( object ):

	class Particle( object ):

		'''
		USE ALPHA IN EXPLOSIONS
		'''
		MAX_GRAPHICS = 0

		def __init__( self, scr, color, pos, radius, angle, speed, drag, world ):

			self.scr = scr
			self.color = color
			self.radius = radius
			self.angle = angle
			self.speed = speed
			self.drag = drag
			self.pos = pos
			self.world = world
			#[ self.vwsx, self.vwsy ] = world.vwsx / 3.0, world.vwsy / 3.0

		def update( self ):

			#[ self.vwsx, self.vwsy ] = self.world.vwsx / 3.0, self.world.vwsy / 3.0

			self.speed /= self.drag
			rad = 180.0 / math.pi
			self.pos[ 0 ] += self.speed * math.cos( self.angle / rad ) # - self.vwsx
			self.pos[ 1 ] += self.speed * math.sin( self.angle / rad ) # - self.vwsy

		def draw( self ):
	
			size = self.scr.get_size( )

			if self.MAX_GRAPHICS:
				s = p.Surface( size, p.SRCALPHA )

				p.draw.circle( 
				s, self.color, [ int( self.pos[ 0 ] ), int( self.pos[ 1 ] ) ],
				int( self.radius ) ) 

				self.scr.blit( s, [ 0, 0 ] )
			else:
				p.draw.circle( 
				self.scr, self.color, [ int( self.pos[ 0 ] ), int( self.pos[ 1 ] ) ],
				int( self.radius ) ) 


			## --- ##

	class Explode( object ):

		def __init__( self, parent, color, color2, size, speed, amount, lifetime, pos, opacity=255 ):

			self.parent = parent
			self.size = size
			self.speed = speed
			self.color = color
			self.color2 = color2
			self.pos = pos
			self.opacity = opacity
			self.scr = 			parent.scr
			self.borders = 		parent.size
			self.amount = amount

			self.particles = [  ]
			self.dead = False
			self.timer = lifetime

			for i in range( self.amount ):

				angle = 360.0 / self.amount

				x = self.pos[0]
				y = self.pos[1]

				self.particles.append( 

					self.parent.Particle( 
						self.scr,
						[ random.random() * ( self.color[ 0 ] - self.color2[ 0 ] ) + self.color2[ 0 ],
						  random.random() * ( self.color[ 1 ] - self.color2[ 1 ] ) + self.color2[ 1 ],
						  random.random() * ( self.color[ 2 ] - self.color2[ 2 ] ) + self.color2[ 2 ],
						  self.opacity, ],
						[ x, y ],
						self.size * random.randint( 1, 4 ),
						i * angle,
						self.speed + random.randint( -20, 20 ) / 4.0,
						1.03 + random.randint( 0, 10 ) / 100.0,
						self.parent.parent	) )

		def update( self ):

			self.timer -= 1
			if self.timer <= 0:
				self.dead = True

			for i in self.particles:
				i.update(  )

				if self.timer < 20 and i.radius > 0:
					i.radius -= .3

		def draw( self ):

			size = self.scr.get_size(  )

			for i in self.particles:
				i.draw(  )

	class Explode2( object ):

		def __init__( self, parent, color, colorindex, size, speed, amount, lifetime, pos, angle ):

			self.parent = parent
			self.size = size
			self.speed = speed
			self.color = color
			self.colorindex = colorindex
			self.pos = pos
			self.scr = parent.scr
			self.borders = parent.size
			self.amount = amount
			self.angle = angle

			self.particles = [  ]
			self.dead = False
			self.timer = lifetime

			for i in range( self.amount ):

				x = self.pos[ 0 ]
				y = self.pos[ 1 ]

				self.particles.append( 

					self.parent.Particle( 
						self.scr,
						[ self.color[ 0 ] - random.randint( 0, self.colorindex[ 0 ] ),
						  self.color[ 1 ] - random.randint( 0, self.colorindex[ 1 ] ),
						  self.color[ 2 ] - random.randint( 0, self.colorindex[ 2 ] ), 
						  self.color[ 3 ], ],
						[ x, y ],
						self.size * random.randint( 1, 4 ),
						90 - self.angle + random.randint( -25, 25 ),
						self.speed + random.randint( -20, 20 ) / 10.0,
						1.01 + random.randint( 0, 10 ) / 100.0,
						self.parent.parent	) )

		def update( self ):

			self.timer -= 1
			if self.timer <= 0:
				self.dead = True

			for i in self.particles:
				i.update(  )

				if self.timer < 20 and i.radius > 0:
					i.radius -= .3

		def draw( self ):

			size = self.scr.get_size(  )
			
			for i in self.particles:
				i.draw(  )

		## --- ##

	def __init__( self, parent ):

		self.parent = parent
		self.scr = parent.scr
		self.size = parent.size
		self.effects = [  ]

	def mkExplosion( self, color, color2, size, speed, amount, lifetime, pos, opacity=255 ):

		self.effects.append( self.Explode( self, color, color2, size, speed, amount, lifetime, pos, opacity ) )

	def mkExplosion2( self, color, colorindex, size, speed, amount, lifetime, pos, angle ):

		self.effects.append( self.Explode2( self, color, colorindex, size, speed, amount, lifetime, pos, angle ) )

	def update( self ):

		tt = [  ]
		for e in self.effects:

			e.update(  )

			if e.dead:

				tt.append( e )

		for e in tt:
			self.effects.remove( e )

	def draw( self ):

		for e in self.effects:

			e.draw(  )










class Decorations( object ):

	class Flag( object ):

		def __init__( self, data ):

			self.window = data[ "window" ]
			self.pos = data[ "pos" ]
			self.color = data[ "color" ]
			self.indexspeed = data[ "speed" ]
			self.rotspeed = data[ "rotspeed" ]
			self.direction = data[ "direction" ]

			try: self.type = data[ "type" ]( self )
			except: self.type = None

			self.index = 0

		def draw( self ):

			rad = 180.0 / math.pi
			self.index += self.indexspeed * self.direction

			if self.type != None:
				self.type.draw(  )

			else:

				for i in range( self.pos[ 2 ] ):

					p.draw.rect( self.window, self.color, [ 
						self.pos[ 0 ] + i,
						self.pos[ 1 ] + int( self.pos[ 3 ] / 4 * \
							math.sin( self.rotspeed * ( i + self.index ) / rad ) * i / self.pos[ 2 ] ),
						1,
						self.pos[ 3 ] ] )

	class Wave( object ):

		def __init__( self, data ):

			self.window = data[ "window" ]
			self.pos = data[ "pos" ]
			self.color = data[ "color" ]
			self.indexspeed = data[ "speed" ]
			self.rotspeed = data[ "rotspeed" ]
			self.direction = data[ "direction" ]

			try: self.type = data[ "type" ]( self )
			except: self.type = None

			self.index = 0

		def draw( self ):

			rad = 180.0 / math.pi
			self.index += self.indexspeed * self.direction

			if self.type != None:
				self.type.draw(  )

			else:

				for i in range( self.pos[ 2 ] ):

					p.draw.rect( self.window, self.color, [ 
						self.pos[ 0 ] + i,
						self.pos[ 1 ] + int( self.pos[ 3 ] / 4 * math.sin( self.rotspeed * ( i + self.index ) / rad ) ),
						1,
						self.pos[ 3 ] ] )
					
					

class Bars( object ):
	
	class HealthBar( object ):

		def __init__( self, scr, maxhealth, barlenght, bars=-1 ):

			self.scr = scr
			self.bars = bars
			self.maxhealth = maxhealth
			self.barlenght = barlenght
			if barlenght > maxhealth:
				self.barlenght = maxhealth

			self.index = 255.0 / self.maxhealth

			self.healthcolor = [ 0, 0, 0 ]

			if self.bars <= 0:
				self.bars = maxhealth / float( self.barlenght )

		def draw( self, center, health ):

			self.healthcolor = [ int( 255 - self.index * health ), 
							     int( self.index * health ),
							     0 ]

			for b in range( int( math.floor( self.bars ) ) ):

				p.draw.rect( self.scr, self.healthcolor,
					[ center[ 0 ] - self.barlenght * health / 2 / self.bars,
					  center[ 1 ] + 11 * ( b + 2 ),
					  self.barlenght * health / self.bars,
					  8 ]
				)

	class DynamicHealthBar( object ):

		def __init__( self, scr, maxhealth, barlenght = 10, bars=-1 ):

			self.scr = scr
			self.size = scr.get_width(  ), scr.get_height(  )
			self.bars = bars
			self.maxhealth = maxhealth
			self.barlenght = barlenght
			if barlenght > maxhealth:
				self.barlenght = maxhealth

			if self.bars <= 0:
				self.bars = maxhealth // self.barlenght

			self.maxbarhealth = maxhealth / self.bars
			self.index = 255.0 / self.maxhealth
			self.barindex = 255.0 / self.maxbarhealth

			healthcolor = [ 0, 0, 0 ]
			self.barlist = [  ]

			for i in range( int( math.floor( self.bars ) ) ):
				self.barlist.append( [ self.maxbarhealth, healthcolor ] )

		def draw( self, cent, health ):

			self.bars = len( self.barlist )
			center = [ cent[ 0 ], cent[ 1 ] ]

			for b in self.barlist:
				b[ 1 ] = [ 0, 255, 0 ]

			self.barlist[ -1 ][ 0 ] = health - ( self.bars - 1 ) * self.maxbarhealth

			try:
				if self.barlist[ -1 ][ 0 ] <= 0:
					del self.barlist[ -1 ]
			except: pass

			self.barlist[ -1 ][ 1 ] = [ abs( int( 255 - self.barindex * self.barlist[ -1 ][ 0 ] ) ), 
								        abs( int( self.barindex * self.barlist[ -1 ][ 0 ] ) ),
								        0 ]

			if center[ 1 ] + 8 * ( len( self.barlist ) + 3 ) + 2 * 6 >= self.size[ 1 ]:
				center[ 1 ] = self.size[ 1 ] - ( 8 * ( len( self.barlist ) + 3 ) + 2 * 6 )

			elif center[ 1 ] <= 0:
				center[ 1 ] = 0

			try:
				if center[ 0 ] + int( 7 * self.barlist[ 0 ][ 0 ] ) >= self.size[ 0 ]:
					center[ 0 ] = self.size[ 0 ] - int( 7 * self.barlist[ 0 ][ 0 ] )

				elif center[ 0 ] - int( 7 * self.barlist[ 0 ][ 0 ] ) <= 0:
					center[ 0 ] = int( 7 * self.barlist[ 0 ][ 0 ] )
			except: pass

			d = 0
			for b in self.barlist:
				try:
					p.draw.rect( self.scr, b[ 1 ], 
						[ center[ 0 ] - self.barlenght / 2 * b[ 0 ],
						  center[ 1 ] + 8 * ( d + 3 ), self.barlenght * b[ 0 ], 6] )
				except:
					pass
				d += 1

	class ProtBar( object ):

		@classmethod
		def draw( self, scr, cent, prot, depth=-1 ):

			if depth < 0:
				depth = prot / 10.0

			if depth >= 25.5:
				depth = 25.5
			try:
				prot /= depth
			except: pass

			size = scr.get_width(  ), scr.get_height(  )

			center = [ cent[ 0 ], cent[ 1 ] ]

			if center[ 1 ] + 8 * 5 + 2 * 6 >= size[ 1 ]:
				center[ 1 ] = size[ 1 ] - 8 * 1 + 3 + 2 * 6

			elif center[ 1 ] <= 0:
				center[ 1 ] = 0

			try:
				if center[ 0 ] + int( 7 * prot ) >= size[ 0 ]:
					center[ 0 ] = size[ 0 ] - int( 7 * prot )

				elif center[ 0 ] - int( 7 * prot ) <= 0:
					center[ 0 ] = int( 7 * prot )
			except: pass

			prot = int( math.floor( prot ) )

			for i in range( int( prot // depth ) ):

				p.draw.rect( scr, ( 255 - 10 * depth, 255 - 10 * depth, 255 - 10 * depth ), [ 
					center[ 0 ] - 3,
					center[ 1 ] + 10 * ( i + 3 ),
					6,
					6 ] )