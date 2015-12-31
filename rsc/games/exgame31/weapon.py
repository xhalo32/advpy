import pygame as p

class SHOT:
	def __init__( self, main, par, pos, direction ):
		self.par = par
		self.main = main
		self.x = pos[ 0 ]
		self.y = pos[ 1 ]
		self.direction = direction
		self.dead = False
	def update( self ):
		self.x += self.direction * self.par.shotspeed
		self.y += .35
		for e in self.main.enemies.elist:
			if e.x - self.par.shotradius < self.x < e.x + e.w + self.par.shotradius and \
				e.y - self.par.shotradius < self.y < e.y + e.h + self.par.shotradius:
				e.dead = True
				self.dead = True

	def draw( self ):
		p.draw.circle( self.main.scr, self.par.shotcolor,
			[ int( self.x ), int( self.y ) ], self.par.shotradius )

class Weapons:

	class PISTOL:
		def __init__( self, main, holder ):
			self.main = main
			self.holder = holder
			self.direction = 1
			self.shotspeed = 10
			self.shotradius = 4
			self.shotcolor = ( 255, 200, 0 )
			self.shotlist = [  ]
		def update( self ):
			l = list( self.shotlist )
			for s in self.shotlist:
				s.update(  )
				if s.dead: l.remove( s )
			self.shotlist = l

			from player import teste
			try: self.direction = \
					( self.holder.x - self.holder.lx ) / abs( self.holder.x - self.holder.lx )
			except:pass

			if teste( self.main.events, "D", "K_SPACE" ): self.shoot(  )
		def shoot( self ):
			self.shotlist.append( 
			SHOT( self.main, self, 
				[ self.holder.x + self.holder.w / 2 \
				+ self.direction * self.holder.w,
				self.holder.y - .7 * self.holder.h ],
				self.direction ) )
		def draw( self ):
			for s in self.shotlist:
				s.draw(  )
			if self.direction == 1:
				p.draw.rect( self.main.scr, ( 0, 0, 0 ), 
					[ int( self.holder.x + 0.7 * self.holder.w ),
					int( self.holder.y - .75 * self.holder.h ),
					18, 6 ] )
			elif self.direction == -1:
				p.draw.rect( self.main.scr, ( 0, 0, 0 ), 
					[ int( self.holder.x + 0.3 * self.holder.w - 18 ),
					int( self.holder.y - .75 * self.holder.h ),
					18, 6 ] )