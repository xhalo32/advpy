import pygame as p

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

		self.b1 = Button( {
			"window" : self.scr,
			"pos" : [ 250, 250, 50, 30 ],
			"color" : ( 0, 255, 200 ),
			"clickcolor" : ( 0, 200, 150 ),
			"message" : "HEY",
			"font" : { "type" : "Arial", "size" : 25, "clicksize" : 10 },
			"action" : self.main._shoot,
			"args" : ( ( 255, 255, 255 ), 1, 4, .1 ),
			} )

		self.s1 = Slider( {
			"window" : self.scr,
			"pos" : [ 500, 500, 50, 30 ],
			"color" : ( 0, 255, 200 ),
			"color2" : ( 255, 0, 55 ),
			"colorindex" : 100,
			"steps" : { "startpoint" : 1, "endpoint" : 10 },
			"font" : { "size" : 15, "clicksize" : 20 }
			} )

		self.f1 = Decorations.Flag( {
			"window" : self.scr,
			"pos" : [ 400, 200, 40, 40 ],
			"color" : ( 255, 255, 255 ),
			"speed" : 1,
			"rotspeed" : 4,
			"direction" : 1,
			} )

	def restart( self ):

		self.__init__( self.main )

	def shiftworld( self ):

		self.b1.pos[ 0 ] -= self.vwsx / 3.0
		self.b1.pos[ 1 ] -= self.vwsy / 3.0

		self.s1.pos[ 0 ] -= self.vwsx / 3.0
		self.s1.pos[ 1 ] -= self.vwsy / 3.0

		self.f1.pos[ 0 ] -= self.vwsx / 3.0
		self.f1.pos[ 1 ] -= self.vwsy / 3.0

	def update( self ):

		self.vwsx = self.player.vx
		self.vwsy = self.player.vy

		self.wsx += self.vwsx
		self.wsy += self.vwsy

		self.entitylist = [ self.player ] + [ e for e in self.enemyC.opponentlist ]

		if self.main.holdingSpace:
			self.player.shoot( ( 0, 255, 100 ), 2, 10, 1 )

		self.player.update(  )
		self.enemyC.update(  )
		self.effectC.update(  )
		self.projectile.udpate(  )

		self.shiftworld(  )

		Stars.update( self )

		self.b1.getClicked(  )
		self.s1.update(  )

	def draw( self ):

		self.scr.fill( self.bg )
		Stars.draw(  )

		self.b1.draw(  )
		self.s1.draw(  )
		self.f1.draw(  )

		self.projectile.draw(  )
		self.player.draw(  )
		self.enemyC.draw(  )
		self.effectC.draw(  )

		Messages.message( self.scr, str( self.wsx ) + " " + str( self.wsy ), ( 10, 40 ), p.Color( 'magenta' ) )
		Messages.message( self.scr, len( self.projectile.projectiles ), ( 10, 70 ), p.Color( 'magenta' ) )