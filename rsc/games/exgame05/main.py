import pygame as p
import fps
from entity import Entities
from message import Messages
import time, threading
from random import *
from math import *



def teste( events, type, key ):

	if type == "D":
		type = "KEYDOWN"
	if type == "U":
		type = "KEYUP"

	try:
		for e in events:
			if e.type == getattr( p, type ) and e.key == getattr( p, key ):
				return True
	except:
		pass
	return False



class Main( Entities ):

	def init( self ):

		#self.size = ( 1900, 1000 )
		self.size = ( 800, 600 )
		self.s = p.display.set_mode( self.size )
		self.screenlock = threading.Lock(  )		

		self.timer = 0
		
		fps.init( self )
		self.e_init(  )
		self.events = [  ]

		self.player = self.e_mkEntity(
				{
				"parent" : self,
				"type" : "JUMPABLE_SHADE_POLYGON_PARTICLE",
				"color" : ( 0, 200, 142 ),
				"pos" : [ 100, 100, 20 ],
				"gon" : 5,
				"addtime" : 3,
				"rotspeed" : 2.2,
				"lenght" : 10,
				"vector" :
					{
					"speed" : 3.4,
					},
				}
			)

	def update( self ):

		c = p.time.Clock(  )

		while self.active:

			self.timer += 1

			self.events = p.event.get(  )

			self.mpos = p.mouse.get_pos(  )
			self.mpos_angle = \
			270 - atan2( self.player.type.x - self.mpos[ 0 ],
						 self.player.type.y - self.mpos[ 1 ] ) * ( 180.0 / pi )

			if teste( self.events, "D", "K_LSHIFT" ):
				self.player.type.sprint = 3, 10

			for e in self.entitylist:
				e.type.update(  )

			for e in [ e for e in self.entitylist if e.type.dead ]:
				self.entitylist.remove( e )

			if teste( self.events, "D", "K_ESCAPE" ):
				self.active = False

			if teste( self.events, "D", "K_SPACE" ):
				self.e_mkEntity(
						{
						"parent" : self,
						"type" : "SHADE_PARTICLE",
						"color" : ( 0, 255, 0 ),
						"pos" : [ self.player.type.x,
								  self.player.type.y, 5, 5 ],
						"addtime" : 5,
						"lenght" : 5,
						"vector" :
							{
							"speed" : 5,
							"angle" : self.mpos_angle
							},
						}
					)

			if p.mouse.get_pressed(  )[ 0 ] and self.timer % 1 == 0:
				self.e_mkEntity(
						{
						"parent" : self,
						"type" : "SHADE_PARTICLE",
						"color" : ( 0, 0, 255 ),
						"pos" : [ self.player.type.x,
								  self.player.type.y, 3, 3 ],
						"addtime" : 1,
						"lenght" : 10,
						"vector" :
							{
							"speed" : 4,
							"angle" : self.mpos_angle
							},
						}
					)

			self.updatenowtime = time.time(  )
			fps.calcupdatefps( self )
			self.updatelasttime = time.time(  )
			c.tick( 40 )

	def draw( self ):

		self.s.fill( ( 0, 42, 32 ) )

		for e in [ e for e in self.entitylist if e != self.player ]:
			e.type.draw(  )

		self.player.type.draw(  )
		
		Messages.message( self.s, len( self.entitylist ), [ 10, 50 ], ( 200, 200, 0 ) )

		self.loopnow = time.time(  )
		fps.calcfps( self )
		fps.printfps( self )
		self.looplast = time.time(  )

		with self.screenlock:
			p.display.flip(  )