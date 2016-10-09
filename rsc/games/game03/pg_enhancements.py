import pygame as p
import math, random


p.font.init(  )




class Msg( object ):

	@classmethod
	def blit( self, window, text, pos, color = ( 255,255,255 ), size = 25, font = "Ubuntu", bold = 0, italic = 0 ):
		font = p.font.SysFont( font, size, bold, italic )
		label = font.render( str( text ), 1, color )
		center = [ pos[ x ] - label.get_rect(  ).center[ x ] for x in range( 2 ) ]
		window.blit( label, center )

class ColorFuncts( object ):

	@classmethod
	def invert( self, color ):
		rcolor = [  ]
		for c in color:
			rcolor.append( ( 255 - c ) )
		return rcolor

	@classmethod
	def darken( self, color, index ):
		rcolor = [  ]
		for c in color:

			if c - index < 0: rcolor.append( 0 )
			elif c - index > 255: rcolor.append( 255 )

			else: rcolor.append( ( c - index ) )

		return rcolor








class Button( object ):

	def __init__( self, data ):

		self.data = data

		self.window = data[ "window" ]
		self.pos = data[ "pos" ]
		self.color = data[ "color" ]
		self.clickcolor = data[ "clickcolor" ]
		self.message = data[ "message" ]

		try: self.fontsize = data[ "font" ][ "size" ]
		except: self.fontsize = 25
		try: self.font = data[ "font" ][ "type" ]
		except: self.font = "Ubuntu Mono"

		try: self.clickfontsize = data[ "font" ][ "clicksize" ]
		except: self.clickfontsize = 20
		try: self.clickfont = data[ "font" ][ "clicktype" ]
		except: self.clickfont = "Ubuntu Mono"

		try: self.type = data[ "type" ]( self )
		except: self.type = None

		try: self.action = data[ "action" ]; self.actionargs = data[ "args" ]; print self.action, self.actionargs
		except: self.action = "NORMAL"

		self.clicked = False
		self.center = int(self.pos[ 0 ] + self.pos[ 2 ] / 2.), \
			int(self.pos[ 1 ] + self.pos[ 3 ] / 2.)

	def getClicked( self ):

		self.update(  )

		if self.action == "NORMAL":
			return self.clicked

		elif self.clicked:
			return self.action( self.actionargs )

		else:
			return False

	def update( self ):

		self.center = int(self.pos[ 0 ] + self.pos[ 2 ] / 2.), \
			int(self.pos[ 1 ] + self.pos[ 3 ] / 2.)

		if self.type != None:
			self.type.update(  )

		else:
			mpos = p.mouse.get_pos(  )

			if p.mouse.get_pressed(  )[ 0 ] == 1 or p.mouse.get_pressed(  )[ 2 ] == 1:
				if mpos[ 0 ] > self.pos[ 0 ] and mpos[ 0 ] < self.pos[ 0 ] + self.pos[ 2 ] and \
					mpos[ 1 ] > self.pos[ 1 ] and mpos[ 1 ] < self.pos[ 1 ] + self.pos[ 3 ]:
					self.clicked = True

				else:
					self.clicked = False
			else:
				self.clicked = False

	def draw( self ):

		if self.type != None:
			self.type.draw(  )

		else:
			if self.clicked:
				p.draw.ellipse( self.window, self.clickcolor, self.pos )
				Msg.blit( self.window, self.message, self.center, ColorFuncts.invert( self.clickcolor ), self.clickfontsize , self.clickfont )

			else:
				p.draw.ellipse( self.window, self.color, self.pos )
				Msg.blit( self.window, self.message, self.center, ColorFuncts.invert( self.color ), self.fontsize, self.font )








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
					