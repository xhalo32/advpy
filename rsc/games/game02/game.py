import pygame as p
from projectile import Projectiles
import player
import stars


class Game:

	def __init__( self, main ):

		self.main = main
		self.player = player.Player( self )
		self.projectiles = Projectiles( self )
		self.stars = stars.Stars( self )
		self.speed = 2

	def tick( self ):

		self.player.update(  )
		self.projectiles.update(  )
		self.stars.move( self.speed )
		self.stars.tick(  )

	def draw( self ):
		
		self.stars.draw(  )
		self.projectiles.draw(  )
		self.player.draw(  )