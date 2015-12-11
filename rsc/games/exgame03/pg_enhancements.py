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
		except: self.font = "Ubuntu"

		try: self.clickfontsize = data[ "font" ][ "clicksize" ]
		except: self.clickfontsize = 20
		try: self.clickfont = data[ "font" ][ "clicktype" ]
		except: self.clickfont = "Ubuntu"

		try: self.type = data[ "type" ]( self )
		except: self.type = None

		try: self.click = data[ "click" ]
		except: self.click = ( 1, 0, 0 )

		try: self.action = data[ "action" ]; self.actionargs = data[ "args" ]
		except: self.action = "NORMAL"

		self.clicked = False
		self.center = int(self.pos[ 0 ] + self.pos[ 2 ] / 2.0), \
			int(self.pos[ 1 ] + self.pos[ 3 ] / 2.0)

	def getClicked( self ):

		self.update(  )

		if self.action == "NORMAL":
			return self.clicked

		elif self.clicked:
			return self.action( self.actionargs )

		else:
			return False

	def update( self ):

		self.center = int(self.pos[ 0 ] + self.pos[ 2 ] / 2.0), \
			int(self.pos[ 1 ] + self.pos[ 3 ] / 2.0)

		if self.type != None:
			self.type.update(  )

		else:
			mpos = p.mouse.get_pos(  )

			if p.mouse.get_pressed(  ) == self.click:
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
				p.draw.rect( self.window, self.clickcolor, self.pos )
				Msg.blit( self.window, self.message, self.center, ColorFuncts.invert( self.clickcolor ), self.clickfontsize , self.clickfont )

			else:
				p.draw.rect( self.window, self.color, self.pos )
				Msg.blit( self.window, self.message, self.center, ColorFuncts.invert( self.color ), self.fontsize, self.font )

class Slider( object ):

	def __init__( self, data ):

		self.data = data
		self.window = data[ "window" ]
		self.pos = data[ "pos" ]
		self.color = data[ "color" ]
		self.color2 = data[ "color2" ]
		self.colorindex = data[ "colorindex" ]
		self.startpoint = data[ "steps" ][ "startpoint" ]
		self.endpoint = data[ "steps" ][ "endpoint" ]

		self.steps = self.endpoint - self.startpoint

		try: self.stepsize = data[ "steps" ][ "size" ]
		except: self.stepsize = 1

		try: self.fontsize = data[ "font" ][ "size" ]
		except: self.fontsize = 20
		try: self.font = data[ "font" ][ "type" ]
		except: self.font = "Ubuntu"

		try: self.clickfontsize = data[ "font" ][ "clicksize" ]
		except: self.clickfontsize = 25
		try: self.clickfont = data[ "font" ][ "clicktype" ]
		except: self.clickfont = "Ubuntu"

		try: self.click = data[ "click" ]
		except: self.click = ( 1, 0, 0 )

		try: self.type = data[ "type" ]( self )
		except: self.type = None

		self.startpoint /= self.stepsize
		self.endpoint /= self.stepsize

		self.clicked = False
		self.sliderpos = self.startpoint * self.stepsize
		self.steplen = self.pos[ 2 ] / float( self.steps )
		self.buttonpos = [ int( self.pos[ 0 ] + ( self.sliderpos - self.startpoint * self.stepsize ) * self.steplen ),
						   	 	int( self.pos[ 1 ] + self.pos[ 3 ] / 2.0 ) ]

	def update( self ):

		if self.type != None:
			self.type.update(  )

		else:
			mpos = p.mouse.get_pos(  )

			if p.mouse.get_pressed(  ) == self.click:
				if mpos[ 0 ] > self.pos[ 0 ] and mpos[ 0 ] < self.pos[ 0 ] + self.pos[ 2 ] and \
					mpos[ 1 ] > self.pos[ 1 ] and mpos[ 1 ] < self.pos[ 1 ] + self.pos[ 3 ]:
					self.clicked = True
			else:
				self.clicked = False

		if self.clicked:

			for i in range( self.steps / self.stepsize ):

				if mpos[ 0 ] + self.steplen / 2.0 >= self.pos[ 0 ] + float( i * self.steplen * self.stepsize ) and \
				   mpos[ 0 ] + self.steplen / 2.0 <= self.pos[ 0 ] + float( ( i + 1 ) * self.steplen * self.stepsize ):

					self.sliderpos = self.startpoint * self.stepsize + i * self.stepsize

			if mpos[ 0 ] > self.pos[ 0 ] + self.pos[ 2 ]:
				self.sliderpos = self.endpoint * self.stepsize

			if mpos[ 0 ] < self.pos[ 0 ]:
				self.sliderpos = self.startpoint * self.stepsize

		self.buttonpos = [ int( self.pos[ 0 ] + ( self.sliderpos - self.startpoint * self.stepsize ) * self.steplen ),
						    	int( self.pos[ 1 ] + self.pos[ 3 ] / 2.0 ) ]

	def draw( self ):

		if self.type != None:
			self.type.draw(  )

		elif self.clicked:
			p.draw.rect( self.window, ColorFuncts.darken( self.color, self.colorindex ), self.pos )

			p.draw.circle( self.window, ColorFuncts.darken( self.color2, self.colorindex ),
								self.buttonpos,
								int( self.pos[ 3 ] / 1.8 ) )

			Msg.blit( self.window, self.sliderpos,
				self.buttonpos,
				self.color, self.clickfontsize, self.clickfont )

		else:
			p.draw.rect( self.window, self.color, self.pos )

			p.draw.circle( self.window, self.color2,
								self.buttonpos,
								int( self.pos[ 3 ] / 2.2 ) )

			Msg.blit( self.window, self.sliderpos,
				self.buttonpos,
				self.color, self.fontsize, self.font )

class Effect( object ):

	class Particle( object ):

		def __init__( self, scr, color, pos, radius, angle, speed, drag, world ):

			self.scr = scr
			self.color = color
			self.radius = radius
			self.angle = angle
			self.speed = speed
			self.drag = drag
			self.pos = pos
			self.world = world
			[ self.vwsx, self.vwsy ] = world.vwsx / 3.0, world.vwsy / 3.0

		def update( self ):

			[ self.vwsx, self.vwsy ] = self.world.vwsx / 3.0, self.world.vwsy / 3.0

			self.speed /= self.drag
			rad = 180.0 / math.pi
			self.pos[ 0 ] += self.speed * math.cos( self.angle / rad ) - self.vwsx
			self.pos[ 1 ] += self.speed * math.sin( self.angle / rad ) - self.vwsy

		def draw( self ):

			p.draw.circle( 
			self.scr, self.color, [ int( self.pos[ 0 ] ), int( self.pos[ 1 ] ) ], int( self.radius ) )

			## --- ##

	class Explode( object ):

		def __init__( self, parent, color, size, speed, amount, lifetime, pos ):

			self.parent = parent
			self.size = size
			self.speed = speed
			self.color = color
			self.pos = pos
			self.scr = parent.scr
			self.borders = parent.size
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
						[ self.color[ 0 ] - random.randint( 0, 100 ),
						  self.color[ 1 ],
						  self.color[ 2 ], ],
						[ x, y ],
						self.size * random.randint( 1, 4 ),
						i * angle,
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

			for i in self.particles:
				i.draw(  )

	class Explode2( object ):

		def __init__( self, parent, color, size, speed, amount, lifetime, pos, angle ):

			self.parent = parent
			self.size = size
			self.speed = speed
			self.color = color
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
						[ self.color[ 0 ] - random.randint( 0, 30 ),
						  self.color[ 1 ] - random.randint( 0, 200 ),
						  self.color[ 2 ], ],
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

			for i in self.particles:
				i.draw(  )

		## --- ##

	def __init__( self, parent ):

		self.parent = parent
		self.scr = parent.scr
		self.size = parent.size
		self.effects = [  ]

	def mkExplosion( self, color, size, speed, amount, lifetime, pos ):

		self.effects.append( self.Explode( self, color, size, speed, amount, lifetime, pos ) )

	def mkExplosion2( self, color, size, speed, amount, lifetime, pos, angle ):

		self.effects.append( self.Explode2( self, color, size, speed, amount, lifetime, pos, angle ) )

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
						self.pos[ 1 ] + int( self.pos[ 3 ] / 4 * math.sin( self.rotspeed * ( i + self.index ) / rad ) * i / self.pos[ 2 ] ),
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

			for i in range( self.bars ):
				self.barlist.append( [ self.maxbarhealth, healthcolor ] )

		def draw( self, center, health ):

			self.bars = len( self.barlist )

			for b in self.barlist:
				b[ 1 ] = [ 0, 255, 0 ]

			self.barlist[ -1 ][ 0 ] = health - ( self.bars - 1 ) * self.maxbarhealth

			if self.barlist[ -1 ][ 0 ] <= 0:
				del self.barlist[ -1 ]

			self.barlist[ -1 ][ 1 ] = [ int( 255 - self.barindex * self.barlist[ -1 ][ 0 ] ), 
								        int( self.barindex * self.barlist[ -1 ][ 0 ] ),
								        0 ]
			d = 0
			for b in self.barlist:
				p.draw.rect( self.scr, b[ 1 ], [ center[ 0 ] - self.barlenght / 2 * b[ 0 ],
											     center[ 1 ] + 11 * ( d + 2 ), self.barlenght * b[ 0 ], 8] )
				d += 1
