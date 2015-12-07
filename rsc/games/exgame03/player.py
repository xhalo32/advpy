import pygame as p
import math

from complex import complex

rad = (180.0 / math.pi)

class Player():

	class Projectile(object):

		class Unit(object):

			def __init__(self, parent, color, angle, radius, speed, pos):

				self.parent = parent
				self.player = parent.parent
				self.scr = parent.scr
				self.color = color
				self.angle = angle
				self.radius = radius
				self.speed = speed
				self.pos = [ int(pos[0]), int(pos[1]) ]
				self.dead = False

			def update(self):

				if self.pos[0] > self.scr.get_width() or \
					self.pos[0] < 0 or \
					self.pos[1] < 0 or \
					self.pos[1] > self.scr.get_width():

					self.dead = True

				self.pos[0] += self.speed * math.cos( ( 90 - self.angle ) / rad ) + self.player.vx / 3.0
				self.pos[1] += self.speed * math.sin( ( 90 - self.angle ) / rad ) + self.player.vy / 3.0

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

		def mkUnit(self, color, angle, radius, speed, pos):

			self.projectiles.append(
					self.Unit( self, color, angle, radius, speed, pos )
				)



	def __init__(self, parent):

		self.parent = parent
		self.scr = parent.scr
		self.size = parent.size

		self.pos = [self.x, self.y] = 120, 120
		self.vx = self.vy = 0.0
		self.speed = 3
		self.rotation = 0

		self.projectile = self.Projectile(self)

	def shoot(self, color, radius, speed):

		self.projectile.mkUnit( color, self.rotation, radius, speed, self.pos )

	def update(self):

		mpos = p.mouse.get_pos()

		try:
			self.rotation = math.atan2( mpos[0] - self.x, mpos[1] - self.y ) * rad
		except:
			pass

		self.x += self.vx
		self.y += self.vy

		self.pos = [self.x, self.y]

		self.projectile.udpate()

	def draw(self):

		self.projectile.draw()
		
		complex.triangle( self.scr, (255, 20, 255), self.pos, 15, int( self.rotation ) - 30, usecenter=True )