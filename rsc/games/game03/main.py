import pygame as p
import time
from random import *
from math import *

from message import *
from snake import *
from handler import *


p.init(  )
p.font.init(  )



class Main:

	def __init__( self ):

		self.size = ( 600, 400 )
		self.scr = p.display.set_mode( self.size )

		self.active = 1
		self.FPS = 60
		self.gridsize = [ 8, 8 ]

		

		self.handler = Handler( self )
		self.objs = self.handler.object_list
		self.cl = self.handler.cl
		self.showfps = 2
		self.debug = 0
		
		self.reset(  )


		self.handler.menu.activate_menu( "Main" )

		self.loop(  )

	def reset( self ):
		



		self.command = ""
		self.lt = self.nt = self.delta = 0

		self.handler.reset(  )

		self.handler.create( "Snake", { "speed" : [2,0] } )
		self.handler.create( "Snake", { 
			"speed" : [2,0],
			"pos" : [ 100,100 ],
			"DN" : p.K_DOWN,
			"UP" : p.K_UP,
			"RT" : p.K_RIGHT,
			"LT" : p.K_LEFT,
			"color" : [ 200,200,50 ],
		} )




	def exec_command( self, com ):
		#exec( com )
		try:
			com = "self.command = " + com
			exec( com )
		except Exception as e:
			self.command = e
		return self.command

	#def exec_command_self_cl( cl, com ):
	#	#exec( com )
	#	try:
	#		com = "cl.command = " + com
	#		exec( com )
	#	except Exception as e:
	#		cl.command = e
	#	return cl.command

	## ======COMMANDS======


	def write( self, arg ):
		return arg

	def say( self, arg ):
		print arg



	## ========GAME========


	def get_gindex( self, pos ):

		gwidth = 	float( self.scr.get_width(  ) ) 	/ self.gridsize[ 0 ]
		gheight = 	float( self.scr.get_height(  ) ) 	/ self.gridsize[ 1 ]

		pos_in_grid = [ -1,-1 ]

		for x in range( self.gridsize[ 0 ] ):
			if gwidth * x <= pos[ 0 ] < gwidth * ( x+1 ): pos_in_grid[ 0 ] = x 								## pos x is in grid n
			elif pos[ 0 ] == self.scr.get_width(  ): pos_in_grid[ 0 ] = self.gridsize[ 0 ] - 1	## pos x is in last grid

		for y in range( self.gridsize[ 1 ] ):
			if gheight * y <= pos[ 1 ] < gheight * ( y+1): pos_in_grid[ 1 ] = y 							## pos y is in grid n
			elif pos[ 1 ] == self.scr.get_height(  ): pos_in_grid[ 1 ] = self.gridsize[ 1 ] - 1	## pos y is in last grid

		return pos_in_grid

	def fps( self ):

		self.nt = time.time(  )
		if self.lt != 0: self.delta = self.nt - self.lt; #print 1.0 / self.delta
		self.lt = time.time(  )

	def loop( self ):

		clk = p.time.Clock(  )

		while self.active:

			self.handler.update(  )

			self.scr.fill( [ x + 232 for x in ( 0,0,0 ) ] )

			self.handler.draw(  )
			

			p.display.update(  )
			clk.tick( self.FPS )

			self.fps(  )