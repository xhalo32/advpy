import threading as thd
import random, time

class Producer():

	def __init__(self):

		self.done = 0

	def make(self):

		time.sleep(1)

		self.done += 1

	def run(self):

		for i in range(10):
			self.make()

class Consumer():

	def __init__(self, p):

		self.p = p

		self.taken = 0

	def run(self):

		while self.taken < 10:

			if self.p.done > 0:

				self.p.done -= 1
				self.taken += 1

				time.sleep(1.5)

p = Producer()
c = Consumer(p)

pt = thd.Thread(target=p.run, args=())
ct = thd.Thread(target=c.run, args=())
pt.start()
ct.start()

while 1:

	print c.taken, ct.name

	time.sleep(.5)