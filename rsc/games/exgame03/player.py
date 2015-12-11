import pygame as p
import math, random

from pg_enhancements import Bars
from complex import complex

rad = (180.0 / math.pi)

class Player():

	def __init__(self, parent):

		self.parent = parent
		self.scr = parent.scr
		self.size = parent.size

		self.projectile = parent.projectile

		self.pos = [self.x, self.y] = [ s / 2 for s in self.size ]

		self.vx = self.vy = self.svx = self.svy = 0.0
		self.speed = 5
		self.radius = 15
		self.rotation = 0
		self.damage = 0
		self.dead = False

		self.maxhealth = 10
		self.health = self.maxhealth
		self.hpbar = Bars.DynamicHealthBar( self.scr, self.maxhealth )
		self.rocketshoot_timer = 0

	def shoot( self, color, radius, speed, damage ):

		self.projectile.mkUnit( self, color, self.rotation, radius, speed, damage, self.pos )

	def rocketshoot( self ):

		self.rocketshoot_timer = 3
		self.projectile.mkRPG( self, ( 250, 250, 0 ),
			self.rotation + random.randint( -10, 10 ), 6, 8, 2.5, self.pos )

		#self.projectile.mkUnit( self, ( 250, 250, 100 ),
		#	self.rotation, self.parent.s1.sliderpos, 8, self.parent.s1.sliderpos, self.pos )

		#self.projectile.mkUnit( self, ( 250, 250, 100 ),
		#	self.rotation + 45, self.parent.s1.sliderpos, 8, self.parent.s1.sliderpos, self.pos )

	def update( self ):

		self.rocketshoot_timer -= 1
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

	def draw(self):
		
		complex.triangle( self.scr, (255, 20, 255), self.pos, self.radius, int( self.rotation ) - 30, usecenter=True )

		self.hpbar.draw( self.pos, self.health )