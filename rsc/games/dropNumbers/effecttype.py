import random

class EffectTypes(object):

	class DIFFUSE(object):

		def __init__(self, effect):

			self.effect = effect
			self.randomness = 50, 100, 75.0

		def RemoveParticle(self, part):

			self.effect.particles.remove(part)

		def update(self):

			if self.effect.timer <= 0:

				self.effect.radius -= 0.1

			self.effect.drag += self.effect.dragindex
			self.effect.speed /= self.effect.drag

			if self.effect.radius <= 0:

				self.effect.dead = True

	class EXPAND(object):

		def __init__(self, effect):

			self.effect = effect
			self.randomness = 25, 125, 75.0

		def RemoveParticle(self, part):

			self.effect.particles.remove(part)

		def update(self):

			if self.effect.timer <= 0:

				self.effect.speed -= self.effect.drag / 4.0

				if self.effect.timer > -0.3:
					self.effect.radius += 0.3

				if self.effect.timer < -0.3:
					self.effect.radius -= 0.2

			else:
				self.effect.radius += 0.08

			self.effect.drag += self.effect.dragindex
			self.effect.speed /= self.effect.drag

			if self.effect.radius <= 0:

				self.effect.dead = True


class EffectSubTypes(object):

	class RAINBOW(object):

		def __init__(self, effect):

			self.effect = effect
			self.updated = 0

		def update(self):

			if not self.updated:

				self.updated = 1
				randCols = [0, 50, 200, 250]

				self.effect.particles[3] = [
					randCols[ random.randrange(0, 3) ],
					randCols[ random.randrange(0, 3) ],
					randCols[ random.randrange(0, 3) ]
				]