import pygame as p
from math import *

from message import *



def curve(window, color, center, radius, startangle, endangle, points=-1, lnwidth = 3, antialiased=False):
		
		if points < 0:
			points = radius

		pointlist = []
		angleindex = - (endangle - startangle)

		#while angleindex < 0:
		#	angleindex = 360 - angleindex

		try: pointlen = angleindex / float(points)
		except: raise TypeError( "Radius can not be 0 or less" )

		rad = 180.0 / pi

		for i in range(points + 1):

			pointlist.append(
				[ center[0] + radius * cos( ( - startangle + i * pointlen ) / rad ),
				  center[1] + radius * sin( ( - startangle + i * pointlen ) / rad ) ]
			)

		for i in range(len(pointlist)):
			try: 
				if antialiased:
					p.draw.aaline(window, color, pointlist[i], pointlist[i+1], lnwidth )
				else:
					p.draw.line(window, color, pointlist[i], pointlist[i+1], lnwidth )
			except: pass







class Menu:

	class Main:

		@classmethod
		def init( self, parent ):

			self.parent = parent
			self.main = self.parent.main
			self.dead = 0
			self.hold_space = 0
			self.holding_space = 0
			self.hold_space_time = 30

		@classmethod
		def update( self ):

			self.events = p.event.get(  )
			self.main.handler.events = self.events

			for e in self.events:
				if e.type == p.QUIT: p.quit(  ); quit(  )

				if e.type == p.KEYDOWN:
					if e.key == p.K_SPACE:
						self.holding_space = 1

						
				if e.type == p.KEYUP:
					if e.key == p.K_SPACE:
						self.holding_space = 0

			if self.holding_space: self.hold_space += 1
			elif not self.holding_space: self.hold_space -= 3
			if self.hold_space < 0: self.hold_space = 0

			if self.hold_space > self.hold_space_time: self.dead = 1; self.main.reset(  )

			self.main.cl.get_events(  )

		@classmethod
		def draw( self ):

			self.main.scr.fill( ( 233,233,233 ) )

			size = self.main.scr.get_size(  )

			msg( self.main.scr, "PLAY", [ size[ 0 ] / 2., size[ 1 ] / 2. ], ( 80,80,80 ), bold=1, centered=1 )
			msg( self.main.scr, "[SPACE]", [ size[ 0 ] / 2., size[ 1 ] / 2. + 25 ], ( 150,150,150 ), centered=1 )

			if self.hold_space > 0: curve( self.main.scr, ( 100,220,100 ), [ size[ 0 ] / 2., size[ 1 ] / 2. + 12 ], 
											size[ 1 ] // 6, 
											float( self.hold_space ) / self.hold_space_time * 180 + 90,
											float( self.hold_space ) / self.hold_space_time * - 180 + 90,
											)

			p.display.update(  )



	class Pause:

		@classmethod
		def init( self, parent ):

			self.parent = parent
			self.main = self.parent.main
			self.dead = 0
			self.once = 1

		@classmethod
		def update( self ):

			self.events = p.event.get(  )
			self.main.handler.events = self.events

			for e in self.events:
				if e.type == p.QUIT: p.quit(  ); quit(  )

				if e.type == p.KEYDOWN:
					if e.key == p.K_SPACE: self.dead = 1
					elif e.key == p.K_ESCAPE: self.dead = 1; self.parent.replace_menu( "Main" )

			self.main.cl.get_events(  )

		@classmethod
		def draw( self ):

			if self.once:
				size = self.main.scr.get_size(  )

				msg( self.main.scr, "CONTINUE", [ size[ 0 ] / 2. - 1, 	size[ 1 ] / 2. - 50 - 1 	], ( 40,100,40 ), bold=1, centered=1 )
				msg( self.main.scr, "CONTINUE", [ size[ 0 ] / 2., 		size[ 1 ] / 2. - 50 		], ( 80,200,80 ), bold=1, centered=1 )

				msg( self.main.scr, "[SPACE]", [ size[ 0 ] / 2. - 1, 	size[ 1 ] / 2. - 25 - 1 	], ( 100,100,100 ), centered=1 )
				msg( self.main.scr, "[SPACE]", [ size[ 0 ] / 2., 		size[ 1 ] / 2. - 25 		], ( 150,150,150 ), centered=1 )


				msg( self.main.scr, "MAIN MENU", [ size[ 0 ] / 2. - 1, 	size[ 1 ] / 2. + 25 - 1 	], ( 40,40,100 ), bold=1, centered=1 )
				msg( self.main.scr, "MAIN MENU", [ size[ 0 ] / 2., 		size[ 1 ] / 2. + 25 		], ( 80,80,200 ), bold=1, centered=1 )

				msg( self.main.scr, "[ESCAPE]", [ size[ 0 ] / 2. - 1, 	size[ 1 ] / 2. + 50 - 1 	], ( 100,100,100 ), centered=1 )
				msg( self.main.scr, "[ESCAPE]", [ size[ 0 ] / 2., 		size[ 1 ] / 2. + 50 		], ( 150,150,150 ), centered=1 )

				p.display.update(  )
				self.once = 0



	## --- ##



	def __init__( self, main ):

		self.main = main

		self.active_menus = [  ]

	def get_menu( self, name ):

		return getattr( self, name )

	def replace_menu( self, name ):

		if len(self.active_menus) > 0:
			self.active_menus[ -1 ] = self.get_menu( name )
			self.active_menus[ -1 ].init( self )
		else: self.active_menus.append( self.get_menu( name ) )


	def activate_menu( self, name ):

		now = self.get_menu( name )
		now.init( self )
		
		self.active_menus.append( now )


		clock = p.time.Clock(  )
		while len( self.active_menus ) > 0:

			self.active_menus[ -1 ].update(  )
			self.active_menus[ -1 ].draw(  )

			if self.active_menus[ -1 ].dead: del self.active_menus[ -1 ];

			clock.tick( 60 )