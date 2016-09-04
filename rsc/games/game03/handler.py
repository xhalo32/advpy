import pygame as p
from snake import *
from commandline import *




class Handler:

	def __init__( self, main ):
		
		self.main = main
		self.cl = Commandline( self.main )


		self.Snake = Snake

		self.events = [  ]
		self.object_list = [  ]


	def create( self, obj, *attributes ):
		
		self.object_list.append( getattr( self, obj )( self.main, *attributes ) )

	def handle_events( self ):

		self.events = p.event.get(  )

		for e in self.events:
			if e.type == p.QUIT: self.main.active = False

			#if e.type == p.KEYDOWN:
			#	print e.key

		self.cl.update(  )

	def update( self ):

		self.handle_events(  )

		for obj in self.object_list:
			obj.update(  )

	def draw( self ):

		for obj in self.object_list:
			obj.draw(  )