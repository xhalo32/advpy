import pygame as p
import math
from complex import complex

rad = (180.0 / math.pi)



class Projectile(object):

	class Unit(object):

		def __init__(self, parent, dad, color, angle, radius, speed, damage, pos):

			self.parent = parent
			self.vwsx = self.parent.parent.vwsx
			self.vwsy = self.parent.parent.vwsy
			self.scr = parent.scr
			self.color = color
			self.angle = angle
			self.radius = radius
			self.speed = speed
			self.pos = [ int(pos[0]), int(pos[1]) ]
			self.dead = False
			self.damage = damage

			self.dad = dad

		def update(self):

			if  self.pos[0] > self.scr.get_width() or \
				self.pos[0] < 0 or \
				self.pos[1] < 0 or \
				self.pos[1] > self.scr.get_width():

				self.dead = True

			self.pos[0] += self.speed * math.cos( ( 90 - self.angle ) / rad ) - self.vwsx / 2.0
			self.pos[1] += self.speed * math.sin( ( 90 - self.angle ) / rad ) - self.vwsy / 2.0

			p = self.pos

			for e in self.parent.parent.entitylist:
				
				if e != self.dad:

					if p[ 0 ] - self.radius < e.pos[ 0 ] + e.radius and p[ 0 ] + self.radius > e.pos[ 0 ] - e.radius and \
					   p[ 0 ] + self.radius > e.pos[ 0 ] - e.radius and p[ 0 ] - self.radius < e.pos[ 0 ] + e.radius and \
					   p[ 1 ] - self.radius < e.pos[ 1 ] + e.radius and p[ 1 ] + self.radius > e.pos[ 1 ] - e.radius and \
					   p[ 1 ] + self.radius > e.pos[ 1 ] - e.radius and p[ 1 ] - self.radius < e.pos[ 1 ] + e.radius:

					   self.dead = True
					   e.damage = self.damage

		def draw(self):

			complex.vector( self.scr, self.color, self.pos, self.angle - 90, 2 * self.speed, self.radius )

	def __init__(self, parent):

		self.parent = parent
		self.scr = parent.scr

		self.projectiles = []

	def udpate(self):

		tt = []

		for u in self.projectiles:

			u.update()

			if u.dead:
				tt.append(u)

		for t in tt:
			self.projectiles.remove(t)

	def draw(self):
		
		for u in self.projectiles:

			u.draw()

	def mkUnit(self, parent, color, angle, radius, speed, damage, pos):

		self.projectiles.append(
				self.Unit( self, parent, color, angle, radius, speed, damage, pos )
			)
