import pygame as p
import math

from complex import complex

rad = (180.0 / math.pi)

class Player():

	def __init__(self, parent):

		self.parent = parent
		self.scr = parent.scr
		self.size = parent.size

		self.projectile = parent.projectile

		self.pos = [self.x, self.y] = [ s / 2.0 for s in self.size ]

		self.vx = self.vy = self.svx = self.svy = 0.0
		self.speed = 3
		self.radius = 15
		self.rotation = 0
		self.damage = 0
		self.dead = False

		self.maxhealth = 10
		self.health = self.maxhealth
		self.healthcolor = [ 0, 0, 0 ]

	def shoot(self, color, radius, speed, damage):

		self.projectile.mkUnit( self, color, self.rotation, radius, speed, damage, self.pos )

	def update(self):

		mpos = p.mouse.get_pos()

		try:
			self.rotation = math.atan2( mpos[0] - self.x, mpos[1] - self.y ) * rad
		except:
			pass

		self.svx = self.vx / 2.0
		self.svy = self.vy / 2.0

		self.x += self.svx
		self.y += self.svy

		self.pos = [self.x, self.y]

		if self.damage > 0 and self.health > 0:
			self.health -= self.damage
			self.damage = 0

		if self.health <= 0:
			self.health = 0
			self.dead = 1

		if self.dead:
			self.parent.restart(  )

		index = 255.0 / self.maxhealth
		self.healthcolor = [ int( 255 - index * self.health ), 
						     int( index * self.health ),
						     0 ]

	def draw(self):
		
		complex.triangle( self.scr, (255, 20, 255), self.pos, self.radius, int( self.rotation ) - 30, usecenter=True )

		p.draw.rect( self.scr, self.healthcolor, [ self.pos[ 0 ] - 5*self.health,
												    self.pos[ 1 ] + self.radius, 10*self.health, 8] )