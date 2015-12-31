
import pygame as p
import sys, tick, time, random
sys.path.append( "/home/toor/Desktop/advpy/rsc/" )
from complex import complex
import fps
	
p.init(  )

cols = [ 0, 127, 255 ]

class Run( tick.Tick ):

	def __init__( self ):

		self.size = ( 600, 400 )
		self.scr = p.display.set_mode( self.size )
		self.active = True
		self.vx = self.vy = 0
		self.x, self.y = [ i // 2 for i in self.size ]

		self.rot = 0
		self.timer = 0

		self.init(  )
		fps.init( self )

	def loop( self ):
		clock = p.time.Clock(  )

		while self.active:
			self.events = p.event.get(  )

			self.update(  )
			self.draw(  )

			clock.tick( 60 )

run = Run(  )
run.loop(  )

p.quit(  )
quit(  )