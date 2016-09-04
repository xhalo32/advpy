import pygame as p
from snake import *
from items import *
from commandline import *
from random import *




class Handler:

	def __init__( self, main ):
		
		self.main = main
		self.cl = Commandline( self.main )


		self.Snake = Snake
		self.effects = Effect( self.main )
		self.items = Items( self.main )

		self.events = [  ]
		self.object_list = [  ]

		for i in range( 10 ):
			self.items.generate( "Apple", 
				[ int( random(  ) * ( self.main.scr.get_width(  ) - 20 ) + 10 ),
				 int( random(  ) * ( self.main.scr.get_height(  ) - 20 ) + 10 ) ] )


	def create( self, obj, *attributes ):
		
		self.object_list.append( getattr( self, obj )( self.main, *attributes ) )

	def handle_events( self ):

		self.events = p.event.get(  )

		for e in self.events:
			if e.type == p.QUIT: self.main.active = False
			elif e.type == p.KEYDOWN: 
				if e.key == p.K_r: self.main.reset(  )

			#if e.type == p.KEYDOWN:
			#	print e.key

		self.cl.update(  )

	def update( self ):

		self.items.update(  )
		self.effects.update(  )

		self.handle_events(  )


		aliveobjs = [  ]
		for obj in self.object_list:
			obj.update(  )
			if not obj.dead:aliveobjs.append(obj)
		self.object_list=aliveobjs


	def draw( self ):

		self.items.draw(  )
		self.effects.draw(  )

		for obj in self.object_list:
			obj.draw(  )

		if self.main.showfps:
			msg(	self.main.scr, 
					round( 1. / self.main.delta, self.main.showfps ), 
					[ 0, self.main.scr.get_height(  ) - 15 ], 
					( 0,0,0 ),
					15, 
			)