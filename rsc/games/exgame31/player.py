import pygame as p

def teste( events, t, key ):
	if t == "D":
		t = "KEYDOWN"
	if t == "U":
		t = "KEYUP"

	try:
		for e in events:
			if e.type == getattr( p, t ) and e.key == getattr( p, key ):
				return True
	except:
		return False

class Player:

	def __init__( self, parent ):
		self.p = parent
		self.x = self.p.scr.get_width(  ) / 2
		self.y = self.p.scr.get_height(  )
		self.vx = self.vy = 0
		self.lx = 0
		self.w = 20
		self.h = 40
		self.color = [ 0, 10, 255 ]
		self.stay = False	
		import weapon
		self.weapon = weapon.Weapons.PISTOL( self.p, self )

	def update( self ):
		for e in self.p.events: 
			if e.type == p.QUIT: p.quit(  ); quit(  )
		if teste( self.p.events, "D", "K_UP" ) and self.stay: self.vy = -8
		if teste( self.p.events, "D", "K_RIGHT" ): self.vx = 5
		if teste( self.p.events, "D", "K_LEFT" ): self.vx = -5

		if teste( self.p.events, "U", "K_RIGHT" ) and self.vx > 0: self.vx = 0
		if teste( self.p.events, "U", "K_LEFT" ) and self. vx < 0: self.vx = 0

		self.x, self.y = self.x + self.vx, self.y + self.vy
		if self.y < self.p.scr.get_height(  ):
			self.vy += .35
			self.stay = False
		else: 
			self.vy = 1
			self.stay = True
			self.y = self.p.scr.get_height(  )
		for b in self.p.objectlist:
			if b.y < self.y < b.y + b.h + self.h:
				if b.x + b.w + self.vx <= self.x < b.x + b.w:
					self.x -= self.vx
				if b.x + self.vx >= self.x + self.w > b.x:
					self.x -= self.vx
			if b.x - self.w < self.x < b.x + b.w:
				if b.y <= self.y < b.y + self.vy:
					self.y = b.y
					self.vy = 0
					self.stay = True
				if b.y + b.h > self.y - self.h >= b.y + b.h + self.vy - 1:
					self.vy = 0
					self.y = b.y + b.h + self.h
		self.weapon.update(  )
		self.lx = self.x
	def draw( self ):
		p.draw.rect( self.p.scr, self.color,
			[ int( self.x ), int( self.y - self.h ), int( self.w ), int( self.h ) ] )
		self.weapon.draw(  )