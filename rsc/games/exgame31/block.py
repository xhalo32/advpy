import pygame as p

class Blocks:
	class Block:
		def __init__( self, parent, c, x, y, w, h ):
			self.p = parent
			self.x = x
			self.y = y
			self.w = w
			self.h = h
			self.color = c

			self.dead = False
		def update( self ):
			pass
		def draw( self ):
			p.draw.rect( self.p.main.scr, self.color, [ self.x, self.y, self.w, self.h ] )

	def __init__( self, par ):
		self.main = par
		self.blocklist = [  ]
		for i in range( 10 ):
			self.blocklist.append( self.Block( self, ( 255, 255, 255 ), 60 * i, 450, 20, 20 ) )
		for i in range( 10 ):
			self.blocklist.append( self.Block( self, ( 255, 255, 255 ), 60 * i, 370, 20, 20 ) )
		self.main.objectlist += self.blocklist

	def update( self ):
		l = list( self.blocklist )
		for b in self.blocklist:
			b.update(  )
			if b.dead: l.remove( b )
		self.blocklist = l
	def draw( self ):
		for b in self.blocklist:
			b.draw(  )