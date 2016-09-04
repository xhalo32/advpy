# -*- encoding:utf-8 -*-

import pygame as p
from message import *

import time



class Commandline:

	def __init__( self, main ):

		self.main = main
		self.string = [  ]
		self.memory = [  ]
		self.returns = [  ]

		self.memorysize = 5
		self.returnsize = 4
		self.memindex = -1

		self.execute = 0
		self.active = 0

		self.shift = 0
		self.ctrl = 0
		self.fontsize = 18
		self.blinkpersec = 3


	def add( self, string ):
		self.string.append( string )


	def event_to_text( self ):

		events = p.event.get(  )
		
		if len( self.memory ) > self.memorysize:
			del self.memory[ 0 ]

		for e in events:
			if e.type == p.QUIT:
				p.quit(  )
				quit(  )

			if e.type == p.KEYDOWN:

				if self.ctrl == 0:
					if e.key == p.K_BACKSPACE and len( self.string ) > 0:
						del self.string[ -1 ]

				if self.ctrl == 1:
					if e.key == p.K_BACKSPACE and len( self.string ) > 0:

						while len(self.string) > 0 and self.string[ -1 ] == " ":
							del self.string[ -1 ]

						while len(self.string) > 0 and self.string[ -1 ] != " ":
							del self.string[ -1 ]
					

				elif e.key == p.K_RETURN:

					if len( self.string ) != 0:
						try: 
							ans = self.main.exec_command( "".join( self.string ) )

							if issubclass( type(ans), Exception ):
								self.returns.append( [ ans, "".join( self.string ), ( 220,120,120 ) ] )
							else:
								self.returns.append( [ ans, "".join( self.string ), ( 120,220,120 ) ] )

							if not (self.string in self.memory): self.memory.append( self.string )

						except Exception as e: 
							print e
							self.active = 0
						self.string = [  ]; self.memindex = -1


				elif e.key == p.K_ESCAPE:
					self.active = 0

				elif e.key == p.K_TAB:
					self.add( "\t" )

				if self.shift == 0:

					if 97 <= e.key <= 122 or e.key == 32 or 48 <= e.key <= 57:
						self.add( e.unicode )

					elif e.key == 45: 		self.add( '-' )
					elif e.key == 43:		self.add( '+' )
					elif e.key == 39:		self.add( "'" )
					elif e.key == 60:		self.add( '<' )
					elif e.key == 44:		self.add( ',' )
					elif e.key == 46:		self.add( '.' )
				
				elif self.shift == 1:

					if 97 <= e.key <= 122 or e.key == 32: 	self.add( e.unicode.upper(  ) )

					elif e.key == 49: 		self.add( '!' )
					elif e.key == 50: 		self.add( '"' )
					elif e.key == 51: 		self.add( '#' )
					elif e.key == 52: 		self.add( '¤' )
					elif e.key == 53: 		self.add( '%' )
					elif e.key == 54: 		self.add( '&' )
					elif e.key == 55: 		self.add( '/' )
					elif e.key == 56: 		self.add( '(' )
					elif e.key == 57: 		self.add( ')' )
					elif e.key == 48: 		self.add( '=' )

					elif e.key == 43:		self.add( '?' )
					elif e.key == 39:		self.add( "*" )
					elif e.key == 60:		self.add( '>' )
					elif e.key == 44:		self.add( ';' )
					elif e.key == 46:		self.add( ':' )
					elif e.key == 45: 		self.add( '_' )

			## =======CTRL-SHIFT=======

			if e.type == p.KEYDOWN:
				if e.key == p.K_LSHIFT or e.key == p.K_RSHIFT: self.shift = 1
				elif e.key == p.K_LCTRL or e.key == p.K_RCTRL: self.ctrl = 1

				elif e.key == p.K_UP: self.cycle_commands( 1 )
				elif e.key == p.K_DOWN: self.cycle_commands( 0 )


			if e.type == p.KEYUP:
				if e.key == p.K_LSHIFT or e.key == p.K_RSHIFT: self.shift = 0
				elif e.key == p.K_LCTRL or e.key == p.K_RCTRL: self.ctrl = 0





		if self.memindex != -1: self.string = self.memory[ self.memindex ]

		if not (self.string in self.memory): self.memindex = -1


		## ==========DRAW==========

		p.draw.rect( self.main.scr, (200,200,200), [ 0,0,self.main.scr.get_width(),self.fontsize + 5 ] )

		if round(time.time() * self.blinkpersec, 0) % 2 == 1:
			msg( self.main.scr, "".join( self.string ) + "_", [ 0, 0 ], ( 0,0,0 ), size=self.fontsize, align_to_screen=True )

		if round(time.time() * self.blinkpersec, 0) % 2 == 0:
			msg( self.main.scr, "".join( self.string ) + " ", [ 0, 0 ], ( 0,0,0 ), size=self.fontsize, align_to_screen=True )

		if len( self.returns ) > self.returnsize: del self.returns[ 0 ]
		self.draw_returns()


	def cycle_commands( self, d ):

		if len( self.memory ) > 0:
			if d==1:
				if self.memindex < len( self.memory ) - 1: 			self.memindex += 1
				elif self.memindex == len( self.memory ) - 1: 		self.memindex = -1; self.string = [  ]

			if d==0:
				if self.memindex > 0: 								self.memindex -= 1
				elif self.memindex < 0:								self.memindex = len( self.memory )-1

				elif self.memindex == 0: 							self.memindex = -1;	self.string = [  ]

	def clear( self ):
		self.returns = [  ]

	def draw_returns( self ):

		for i in range( len( self.returns ) ):
			p.draw.rect( self.main.scr, self.returns[ - i - 1 ][ 2 ], 			[ 0,self.fontsize * ( i+1 ) + 5,self.main.scr.get_width(),self.fontsize + 5 ] )

			msg( 		self.main.scr, str( self.returns[ - i - 1 ][ 1 ] ) + " >>> " + str( self.returns[ - i - 1 ][ 0 ] ),
						[ 0, self.fontsize * ( i+1 ) + 5 ], ( 0,0,0 ), size=self.fontsize )


	def get_events( self ):

		if len(self.main.handler.events) == 0:

			if self.active:
				clock = p.time.Clock(  )

				while self.active:
					
					self.event_to_text(  )

					p.display.update(  )

					clock.tick( 60 )

		for e in self.main.handler.events:

			if e.type == p.KEYUP:

				if e.key == p.K_MINUS:

					self.active = 1


	def update( self ):

		self.get_events(  )
