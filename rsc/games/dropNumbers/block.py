import pygame as pg
import sys
sys.path.append( "/home/toor/Desktop/advpy/rsc/" )
import complex
import random

pg.draw.complex = complex.complex

from message import Messages

class Block():
	
	def __init__(self, scr, spd, color, game):
		
		self.scr = scr
		self.w = 100
		self.h = 50
		self.x = random.randint(0, self.scr.get_width() - self.w)
		self.y = -self.h
		self.center = [self.x + self.w/2, self.y + self.h/2]
		self.speed = spd
		self.color = color
		
		self.randomness = 10
		self.terminate = self.fail = False
		
		self.calc = [random.randint(0, 4), random.randint(0, 5)]
		self.ans = self.calc[0] + self.calc[1]
		self.displayCalc = str(self.calc[0]) + " + " + str(self.calc[1])
		
		self.msg = Messages(self.scr)
		self.game = game
	
	def draw(self):
		
		self.randomness = self.game.combo * (self.game.score) + 10

		if self.randomness > 100:
			self.randomness = 100
		
		pg.draw.complex.rrect(self.scr, self.randomC(), [int(self.x), int(self.y), int(self.w), int(self.h)], 6)

		self.msg.message(
						self.displayCalc,
						[self.x + self.w/2, self.y + self.h/2],
						size = 30,
						color=self.invert(self.color)
						)
	
	def update(self):

		self.y += self.speed
		self.center = [self.x + self.w/2, self.y + self.h/2]

		if self.y > self.scr.get_height() - 100:
			self.y -= self.speed / 2.0
		
		if self.y + self.h/2 >= self.scr.get_height():
			
			self.terminate = self.fail = True
	
	def randomC(self):

		self.c1, self.c2, self.c3 = self.color
		self.rclist = [0, 0, 0]
		
		rcolor = []
		color = self.color
		try:
			for i in range(len(color)):
				
				self.rclist[i] = random.randrange(-int(self.randomness) - 1,
												   int(self.randomness) + 1)
				tries = 50
				while color[i] + self.rclist[i] >= 255 or color[i] + self.rclist[i] <= 0:
					
					self.rclist[i] = random.randrange(-int(self.randomness),
													   int(self.randomness))
					tries -= 1
					if tries < 0: 
						self.rclist[i] = 0
						continue

				rcolor.append(color[i] + self.rclist[i])
		except:
			return color

		return rcolor
	
	def invert(self, color):
		rcolor = []
		try:
			for c in color:
				rcolor.append(255 - c)
			return rcolor
		except:
			return color
	
		
		
		
		
		
		
