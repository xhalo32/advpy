import pygame as p
import math

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
				Msg.blit( self.window, self.message, self.center, ColorFuncts.invert( self.clickcolor ), self.fontsize - 2, self.font )

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
					
					