import pygame as p
from main import Main
import fps 
import time, threading



class Run( Main ):

	def __init__( self ):

		self.init(  )

		self.start(  )

	def start( self ):

		self.timer = 0
		self.active = True
		c = p.time.Clock(  )

		self.updateT = threading.Thread( target=self.update )
		self.updateT.daemon = True
		self.updateT.start(  )
		
		while self.active:

			self.draw(  )

			c.tick( 60 )

		p.quit(  )
		quit(  )

try:
	r = Run(  )
except:

p.quit(  )
quit(  )