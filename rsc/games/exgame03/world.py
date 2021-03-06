import pygame as p
import sys
sys.path.append( "/home/toor/Desktop/advpy/rsc/" )

from player import Player
from enemy import Enemy
from stars import Stars
from projectile import Projectile
from pg_enhancements import Button, Slider, Decorations, Effect
from message import Messages
from complex import complex

class World( object ):

	def __init__( self, main ):

		self.main = main
		self.scr = self.main.scr
		self.size = self.main.size

		self.wsx = self.wsy = 0
		self.vwsx = self.vwsy = 0

		self.projectile = Projectile( self )
		self.player = Player( self )
		self.enemyC = Enemy( self )
		self.effectC = Effect( self )

		self.entitylist = [  ]
		self.bg = p.Color( "black" )

		self.s1 = Slider( {
			"window" : self.scr,
			"pos" : [ 500, 500, 50, 30 ],
			"color" : ( 0, 255, 200 ),
			"color2" : ( 255, 0, 55 ),
			"colorindex" : 100,
			"steps" : { "startpoint" : 1, "endpoint" : 10 },
			"font" : { "size" : 15, "clicksize" : 20 }
			} )

	def restart( self ):

		self.__init__( self.main )

	def shiftworld( self ):
		
		self.s1.pos[ 0 ] -= self.vwsx / 3.0
		self.s1.pos[ 1 ] -= self.vwsy / 3.0

	def update( self ):

		self.scr.fill( self.bg )
		
		self.vwsx = self.player.vx
		self.vwsy = self.player.vy

		self.wsx += self.vwsx
		self.wsy += self.vwsy

		self.entitylist = [ self.player ] + [ e for e in self.enemyC.opponentlist ]

		if self.main.holdingSpace:
			self.player.shoot( {
			"dad" : self.player,
			"color" : ( 0, 250, 100 ),
			"colorindex" : ( 0, 100, 50 ),
			"angle" : self.player.rotation,
			"radius" : 2,
			"speed" : 16,
			"damage" : 1.5,
			"lifetime" : 90,
			"pos" : self.player.pos,
			}  )

		self.player.update(  )
		self.enemyC.update(  )
		self.effectC.update(  )
		self.projectile.udpate(  )

		self.shiftworld(  )

		Stars.update( self )

		self.s1.update(  )

	def draw( self ):

		Stars.draw(  )

		self.s1.draw(  )

		self.effectC.draw(  )
		self.projectile.draw(  )
		self.enemyC.draw(  )
		self.player.draw(  )

		Messages.message( self.scr, str( self.wsx ) + " " + str( self.wsy ), ( 10, 40 ), p.Color( 'magenta' ) )
		Messages.message( self.scr, len( self.projectile.projectiles ), ( 10, 70 ), p.Color( 'magenta' ) )
		Messages.message( self.scr, self.enemyC.totaldied, ( 10, 100 ), p.Color( 'green' ) )