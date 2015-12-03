import pygame as pg
import threading


class MainThread(threading.Thread):
	SIZE = (640, 480)
	active = True

	def __init__(self, tid, name):

		threading.Thread.__init__(self)
		self.scr = pg.display.set_mode(self.SIZE)
		self.x = 0
		self.name = name
		self.tid = tid

	def run(self):

		clock = pg.time.Clock()

		while self.active:

			for e in pg.event.get():
				if e.type == pg.QUIT:
					self.active = False

			self.scr.fill(pg.Color('GREEN'))

			self.x = pg.mouse.get_pos()[0]
			pg.draw.circle(self.scr, pg.Color('BLACK'), [self.x, 100], 10)

			pg.display.flip()

			clock.tick(60)

		self.name.exit()


##class MonitorThread(threading.Thread):
##
##	def __init__(self, thread):
##		threading.Thread.__init__(self)
##		self.Thread1 = thread
##
##	def run(self):
##		while self.Thread1.active:
##			print self.Thread1.x


Thread1 = MainThread(1, "T1")
#Thread2 = MonitorThread(Thread1)

Thread1.start()
#Thread2.start()

print "exit main"
