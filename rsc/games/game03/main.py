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
		self.command = ""
		self.lt = self.nt = self.delta = 0
		

		self.handler = Handler( self )
		self.cl = self.handler.cl
		

		self.handler.create( "Snake", { "lenght" : 100, "speed" : [2,0] } )

		self.loop(  )

	def exec_command( self, com ):
		#exec( com )
		try:
			com = "self.command = " + com
			exec( com )
		except Exception as e:
			self.command = e
		return self.command

	def write( self, arg ):
		return arg

	def say( self, arg ):
		print arg

	def fps( self ):

		self.nt = time.time(  )
		if self.lt != 0: self.delta = self.nt - self.lt; #print 1.0 / self.delta
		self.lt = time.time(  )

	def loop( self ):

		clk = p.time.Clock(  )

		while self.active:

			self.handler.update(  )


			self.scr.fill( ( 230,230,230 ) )

			self.handler.draw(  )
			

			p.display.update(  )
			clk.tick( self.FPS )

			self.fps(  )