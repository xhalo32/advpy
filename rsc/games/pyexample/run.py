import pygame as pg
import threading as thd

pg.init()

class Main():
	SIZE = (640, 480)
	active = True

	def __init__( self ):

		self.scr = pg.display.set_mode( self.SIZE )
		self.x = self.y = 0
		self.bx = self.by = 20
		self.lock = thd.Lock(  )

		self.isLastThread = True

	def __call__( self, caller ):

		self.caller = caller

		if self.isLastThread:
			self.caller.isLastThread = True
			self.isLastThread = False

	def run( self ):

		clock = pg.time.Clock( )

		while self.active:

			for e in pg.event.get(  ):
				if e.type == pg.QUIT:
					self.active = False

			self.scr.fill( pg.Color( 'gray' ) )

			self.x, self.y = pg.mouse.get_pos(  )

			pg.draw.circle(self.scr, pg.Color( 'BLACK' ), [self.x, self.y], 10)

			if self.isLastThread:
				pg.display.flip(  )

			clock.tick( 60 )

		pg.quit(  )



class Thing(  ):

	def __init__( self, main ):

		self.name = thd.current_thread(  ).name
		self.main = main
		self.main( self )

	def run( self ):

		clock = pg.time.Clock(  )

		while self.main.active:

			self.main.bx += 1

			pg.draw.circle(self.main.scr, pg.Color( 'BLACK' ), [ self.main.bx, self.main.by ], 10)

			if self.isLastThread:
				pg.display.flip(  )
				
			clock.tick( 60 )


main = Main(  )
thing = Thing( main )

t1 = thd.Thread( target=main.run, args=(  ) )
t1.start(  )

t2 = thd.Thread( target=thing.run, args=(  ) )
t2.start(  )
	
print "EXIT MAIN"