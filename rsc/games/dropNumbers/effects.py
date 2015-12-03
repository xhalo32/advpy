import pygame as pg; import random
import complex
import math

class Effect():

	class FireWork(object):

		def __init__(self, parent, data):

			self.parent = parent
			self.pos = data["pos"]
			self.size = data["size"]
			self.timer = data["timer"]
			self.color = data["color"]
			self.speed = data["speed"]
			self.radius = data["radius"]
			self.dragindex = data["dragindex"]
			self.type = data["type"](self)

			self.subtypes = []

			try:
				for sub in data["subtypes"]:

					sub = sub(self)
					
					self.subtypes.append(sub)
			except:
				pass

			self.drag = 1
			self.dead = False
			self.scr = self.parent.parent.scr

			self.particles = []
			for i in range( self.size ):

				angle = 360.0 / self.size

				x = self.pos[0]
				y = self.pos[1]

				self.particles.append( [ x, y, angle * i, self.color ] )

		def update(self):

			self.timer -= 1.0 / self.parent.parent.FPS

			self.type.update()

			for sub in self.subtypes:
				sub.update()

			totrm = []

			for part in self.particles:

				rad = 180 / math.pi

				r = random.randrange( self.type.randomness[0], self.type.randomness[1] ) / self.type.randomness[2]

				part[0] += ( self.speed / r * math.cos( part[2] / rad ) )
				part[1] += ( self.speed / r * math.sin( part[2] / rad ) )

				if part[0] > self.parent.parent.scr.get_width() or \
					part[0] < 0 or \
					part[1] < 0 or \
					part[1] > self.parent.parent.scr.get_width():

					totrm.append(part)

			for part in totrm:

				self.type.RemoveParticle(part)

		def draw(self):

			for part in self.particles:

				if not self.dead:

					pg.draw.circle(self.scr, part[ 3 ], (int(part[0]), int(part[1])), int(self.radius))


	def __init__(self, parent):

		self.parent = parent
		self.fireworks = []

	def fireWork(self, data):

		self.fireworks.append( self.FireWork( self, data ) )

	def update(self):

		delf = []

		for f in self.fireworks:

			f.update()

			if f.dead:
					
				self.fireworks.remove(f)

	def draw(self):

		for f in self.fireworks:

			f.draw()