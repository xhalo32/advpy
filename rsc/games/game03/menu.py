import pygame as p
from math import *
from time import *

from message import *
from pg_enhancements import *


u50 = 0
u5 = 0
u1 = 0

def get_units( width ):
	global u50, u5, u1
	u50 = width / 8.
	u5 = width / 80.
	u1 = width / 400.


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

			self.hold_s = 0
			self.holding_s = 0
			self.hold_s_time = 30

		@classmethod
		def update( self ):

			self.events = p.event.get(  )
			self.main.handler.events = self.events

			for e in self.events:
				if e.type == p.QUIT: p.quit(  ); quit(  )

				if e.type == p.KEYDOWN:
					if e.key == p.K_SPACE:
						self.holding_space = 1
					if e.key == p.K_s:
						self.holding_s = 1

						
				if e.type == p.KEYUP:
					if e.key == p.K_SPACE:
						self.holding_space = 0
					if e.key == p.K_s:
						self.holding_s = 0


			if self.holding_space: self.hold_space += 1
			elif not self.holding_space: self.hold_space -= 3
			if self.hold_space < 0: self.hold_space = 0

			if self.holding_s: self.hold_s += 1
			elif not self.holding_s: self.hold_s -= 3
			if self.hold_s < 0: self.hold_s = 0

			if self.hold_space > self.hold_space_time: self.dead = 1; self.main.reset(  )
			if self.hold_s > self.hold_s_time: self.parent.add_menu( "Main_settings" ); self.hold_s = 0; self.holding_s = 0

			self.main.cl.get_events(  )

		@classmethod
		def draw( self ):

			self.main.scr.fill( ( 233,233,233 ) )

			size = self.main.scr.get_size(  )
			
			u50 = size[ 1 ] / 8.

			msg( self.main.scr, "PLAY",    [ size[ 0 ] / 2., size[ 1 ] / 2. - u50 / 4 ], ( 80,80,80 ), 	  size[ 1 ] / 14., bold=1, centered=1 )
			msg( self.main.scr, "[SPACE]", [ size[ 0 ] / 2., size[ 1 ] / 2. + u50 / 4 ], ( 150,150,150 ), size[ 1 ] / 14., centered=1 )

			msg( self.main.scr, "SETTINGS",    [ size[ 0 ] / 2., 5*size[ 1 ] / 6. - u50 / 8 ], ( 80,80,80 ), 	  size[ 1 ] / 26., bold=1, centered=1 )
			msg( self.main.scr, "[S]", [ size[ 0 ] / 2., 5*size[ 1 ] / 6. + u50 / 8 ], ( 150,150,150 ), size[ 1 ] / 26., centered=1 )


			if self.hold_space > 0: curve( self.main.scr, ( 100,220,100 ), [ size[ 0 ] / 2., size[ 1 ] / 2. ], 
											size[ 1 ] // 6, 
											float( self.hold_space ) / self.hold_space_time * 180 + 90,
											float( self.hold_space ) / self.hold_space_time * - 180 + 90)


			if self.hold_s > 0: curve( self.main.scr, ( 220,100,100 ), [ size[ 0 ] / 2., 5*size[ 1 ] / 6. ], 
											size[ 1 ] // 10, 
											float( self.hold_s ) / self.hold_s_time * 180 + 90,
											float( self.hold_s ) / self.hold_s_time * - 180 + 90)

			p.display.update(  )



	class Main_settings:

		@classmethod
		def init( self, parent ):

			self.parent = parent
			self.main = self.parent.main
			self.dead = 0
			self.hold_space = 0
			self.holding_space = 0
			self.hold_space_time = 50

			self.buttonlist = [  ]

			self.buttonlist.append( Button( {
					"window" : self.main.scr,
					"pos" : ( u50,len(self.buttonlist)*u50,u50,u50 ),
					"color" : (220,220,220),
					"clickcolor" : (200,200,200),
					"message" : self.main.handler.items.appleamount,
				} ) )

			self.btn2_r = 0
			self.buttonlist.append( Button( {
					"window" : self.main.scr,
					"pos" : ( u50,len(self.buttonlist)*u50,u50,u50 ),
					"color" : (220,220,220),
					"clickcolor" : (200,200,200),
					"message" : self.main.handler.items.applespeed,
				} ) )

			self.fade = 0
			self.fade_timer = 0
			self.fade_time = 20
			self.color = ( 100,220,100 )


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


			for b in self.buttonlist:
				b.update(  )
			
			if self.buttonlist[0].clicked: 
				if p.mouse.get_pressed(  )[ 0 ] == 1 and self.main.handler.items.appleamount < 999:
					self.main.handler.items.appleamount += 1

				if p.mouse.get_pressed(  )[ 2 ] == 1 and self.main.handler.items.appleamount > 0:
					self.main.handler.items.appleamount -= 1

			
			if self.buttonlist[1].clicked: 
				if p.mouse.get_pressed(  )[ 0 ] == 1 and self.main.handler.items.applespeed < 5 and self.btn2_r == 0:
					self.main.handler.items.applespeed += 1
					self.btn2_r = 1

				if p.mouse.get_pressed(  )[ 2 ] == 1 and self.main.handler.items.applespeed > 0 and self.btn2_r == 0:
					self.main.handler.items.applespeed -= 1
					self.btn2_r = 1

			else: self.btn2_r = 0


			self.buttonlist[0].message = self.main.handler.items.appleamount
			self.buttonlist[1].message = self.main.handler.items.applespeed



			if self.hold_space > self.hold_space_time - 20: self.holding_space = 1

			if self.holding_space: self.hold_space += 1
			elif not self.holding_space: self.hold_space -= 3
			if self.hold_space < 0: self.hold_space = 0

			if self.hold_space > self.hold_space_time: self.fade = 1

			self.main.cl.get_events(  )

		@classmethod
		def draw( self ):

			if not self.fade:

				self.main.scr.fill( ( 233,233,233 ) )

				size = self.main.scr.get_size(  )


				for b in self.buttonlist:
					b.draw(  )

				msg( self.main.scr, "APPLES",    [ 3 * u50, u50 - u50 / 2 ], 
					( 130 + 125 * (self.main.handler.items.appleamount / 999.),
					130 - 130 * (self.main.handler.items.appleamount / 999.),
					130 - 130 * (self.main.handler.items.appleamount / 999.) ),
					size[ 1 ] / 16., bold=1, centered=1 )

				msg( self.main.scr, "+= APPLES",    [ 3 * u50 + 4 * u5, 2 * u50 - u50 / 2 ], 
					( 130, 130 + 70 * (self.main.handler.items.applespeed / 5.), 130 ),
					size[ 1 ] / 16., bold=1, centered=1 )


				msg( self.main.scr, "RETURN",    [ size[ 0 ] / 2., 5*size[ 1 ] / 6. - u50 / 8 ], ( 80,80,80 ), 	  size[ 1 ] / 26., bold=1, centered=1 )
				msg( self.main.scr, "[SPACE]", [ size[ 0 ] / 2., 5*size[ 1 ] / 6. + u50 / 8 ], ( 150,150,150 ), size[ 1 ] / 26., centered=1 )

				if self.hold_space > 0: 
					p.draw.circle( self.main.scr, self.color, [ size[ 0 ] // 2, 5*size[ 1 ] // 6 ], 
						int( 1.5 * (float(self.hold_space) / self.hold_space_time) * size[1] ) )

				p.display.update(  )



			if self.fade:

				#sleep( 0.2 )

				self.fade_timer += 1

				c = [ 
					self.color[ 0 ] + ( self.fade_timer / float(self.fade_time) ) * ( 233 - self.color[ 0 ] ),
					self.color[ 1 ] + ( self.fade_timer / float(self.fade_time) ) * ( 233 - self.color[ 1 ] ),
					self.color[ 2 ] + ( self.fade_timer / float(self.fade_time) ) * ( 233 - self.color[ 2 ] ),
				]

				self.main.scr.fill( c )
				p.display.update(  )

				if self.fade_timer >= self.fade_time: self.dead = 1  #; self.parent.replace_menu( "Main" )



	class Pause:

		@classmethod
		def init( self, parent ):

			self.parent = parent
			self.main = self.parent.main
			self.dead = 0
			self.once = 1

			self.hold_space = 0
			self.holding_space = 0
			self.hold_space_time = 10

			self.hold_esc = 0
			self.holding_esc = 0
			self.hold_esc_time = 20

		@classmethod
		def update( self ):

			self.events = p.event.get(  )
			self.main.handler.events = self.events

			for e in self.events:
				if e.type == p.QUIT: p.quit(  ); quit(  )

				if e.type == p.KEYDOWN:
					if e.key == p.K_SPACE: self.holding_space = 1
					elif e.key == p.K_ESCAPE: self.holding_esc = 1
				if e.type == p.KEYUP:
					if e.key == p.K_SPACE: self.holding_space = 0
					elif e.key == p.K_ESCAPE: self.holding_esc = 0



			if self.holding_space: self.hold_space += 1
			if self.hold_space < 0: self.hold_space = 0

			if self.hold_space > self.hold_space_time: self.dead = 1

			if self.holding_esc: self.hold_esc += 1
			if self.hold_esc < 0: self.hold_esc = 0

			if self.hold_esc > self.hold_esc_time: self.dead = 1; self.parent.replace_menu( "Main" )



			self.main.cl.get_events(  )

		@classmethod
		def draw( self ):

			size = self.main.scr.get_size(  )
			if self.once:

				

				msg( self.main.scr, "CONTINUE", [ size[ 0 ] / 2. - u1, 	size[ 1 ] / 2. - u50 - u1 	], ( 40,100,40 ), size[ 1 ] / 16., bold=1, centered=1 )
				msg( self.main.scr, "CONTINUE", [ size[ 0 ] / 2., 		size[ 1 ] / 2. - u50 		], ( 80,200,80 ), size[ 1 ] / 16., bold=1, centered=1 )

				msg( self.main.scr, "[SPACE]", [ size[ 0 ] / 2. -u1, 	size[ 1 ] / 2. - u50 / 2 -u1], ( 100,100,100 ), size[ 1 ] / 16., centered=1 )
				msg( self.main.scr, "[SPACE]", [ size[ 0 ] / 2., 		size[ 1 ] / 2. - u50 / 2 	], ( 150,150,150 ), size[ 1 ] / 16., centered=1 )


				msg( self.main.scr, "MAIN MENU", [ size[ 0 ] / 2. -u1, 	size[ 1 ] / 2. + u50 / 2 -u1], ( 40,40,100 ), size[ 1 ] / 16., bold=1, centered=1 )
				msg( self.main.scr, "MAIN MENU", [ size[ 0 ] / 2., 		size[ 1 ] / 2. + u50 / 2 	], ( 80,80,200 ), size[ 1 ] / 16., bold=1, centered=1 )

				msg( self.main.scr, "[ESCAPE]", [ size[ 0 ] / 2. - u1, 	size[ 1 ] / 2. + u50 - u1 	], ( 100,100,100 ), size[ 1 ] / 16.,centered=1 )
				msg( self.main.scr, "[ESCAPE]", [ size[ 0 ] / 2., 		size[ 1 ] / 2. + u50 		], ( 150,150,150 ), size[ 1 ] / 16., centered=1 )

				self.once = 0

			if (float(self.hold_space) / self.hold_space_time) > 0:
				pos = [ size[ 0 ]/2. - (float(self.hold_space) / self.hold_space_time) * u50,
					size[ 1 ]/2. - u50 / 2 - (u50 / 20) + size[ 1 ] / 24.,
					(float(self.hold_space) / self.hold_space_time) * 2 * u50,
					u50 / 10 ]

				p.draw.rect( self.main.scr, ( 40,100,40 ), [ pos[ 0 ]-u1, pos[ 1 ]-u1, pos[ 2 ], pos[ 3 ] ] )
				p.draw.rect( self.main.scr, ( 80,200,80 ), pos )

			if (float(self.hold_esc) / self.hold_esc_time) > 0:
				pos = [ size[ 0 ]/2. - (float(self.hold_esc) / self.hold_esc_time) * u50,
					size[ 1 ]/2. + u50 - (u50 / 20) + size[ 1 ] / 24.,
					(float(self.hold_esc) / self.hold_esc_time) * 2 * u50,
					u50 / 10 ]

				p.draw.rect( self.main.scr, ( 40,40,100 ), [ pos[ 0 ]-u1, pos[ 1 ]-u1, pos[ 2 ], pos[ 3 ] ] )
				p.draw.rect( self.main.scr, ( 80,80,200 ), pos )

			p.display.update(  )




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

	def add_menu( self, name ):

		self.active_menus.append( self.get_menu( name ) )
		self.active_menus[ -1 ].init( self )


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
