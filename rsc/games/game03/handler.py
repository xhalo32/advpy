import pygame as p
from random import *
from math import *

from snake import *
from items import *
from menu import *
from commandline import *
from points import *




class Handler:

	def __init__( self, main ):
		
		self.main = main
		self.cl = Commandline( self.main )

		get_units( self.main.scr.get_height(  ) )

		self.Snake = Snake
		self.effects = Effect( self.main )
		self.items = Items( self.main )
		self.menu = Menu( self.main )
		self.points = Points( self.main )

		self.events = [  ]
		self.object_list = [  ]

	def reset( self ):

		self.object_list = [  ]
		self.items.clearall(  )

		for i in range( self.items.appleamount ):
			self.items.generate( "Apple" )

		for i in range( self.items.speedcandyamount ):
			self.items.generate( "Speedcandy" )


	def create( self, obj, *attributes ):
		
		self.object_list.append( getattr( self, obj )( self.main, *attributes ) )

	def handle_events( self ):

		self.events = p.event.get(  )

		for e in self.events:
			if e.type == p.QUIT: self.main.active = False
			elif e.type == p.KEYDOWN: 
				if e.key == p.K_r: self.main.reset(  )
				if e.key == p.K_ESCAPE: self.menu.activate_menu( "Pause" )

			#if e.type == p.KEYDOWN:
			#	print e.key

		self.cl.get_events(  )

	def update( self ):

		self.items.update(  )
		self.effects.update(  )

		self.handle_events(  )
		self.points.update(  )


		aliveobjs = [  ]
		for obj in self.object_list:
			obj.update(  )
			if not obj.dead:aliveobjs.append(obj)
		self.object_list=aliveobjs


	def draw( self ):

		if self.main.drawgrid:
			g = self.main.gridsize
			gridunit = self.main.scr.get_width(  ) / float( g[ 0 ] ), self.main.scr.get_height(  ) / float( g[ 1 ] )

			for x in range( g[ 0 ] ):
				for y in range( g[ 1 ] ):
					if ( x+y ) % 2 == 1 and self.main.drawgrid == 2:
						p.draw.rect( self.main.scr, ( 0,0,0 ), [ x * gridunit[0], y * gridunit[1], gridunit[0], gridunit[1] ] )
					elif self.main.drawgrid == 1:
						p.draw.rect( self.main.scr, ( 0,0,0 ), [ x * gridunit[0], y * gridunit[1], gridunit[0], gridunit[1] ], 1 )
					elif ( x+y ) % 2 == 1 and self.main.drawgrid == 3:
						p.draw.rect( self.main.scr, ( 0,0,0 ), [ x * gridunit[0], y * gridunit[1], gridunit[0], gridunit[1] ], 1 )
				

		self.items.draw(  )
		self.effects.draw(  )

		for obj in self.object_list:
			obj.draw(  )

		self.points.draw(  )


		if self.main.showfps and self.main.delta != 0:
			msg(	self.main.scr, 
					round( 1. / self.main.delta, self.main.showfps ), 
					[ 0, self.main.scr.get_height(  ) - 15 ], 
					( 0,0,0 ),
					15, 
			)