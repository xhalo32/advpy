import random
import time

from block import Block
from message import Messages
import pygame as pg
from slider import Slider
from effects import Effect
from effecttype import EffectTypes, EffectSubTypes

pg.init()

class Run():
	
	def __init__(self):
		
		self.blocklist = []
		self.scr = pg.display.set_mode((640, 480), pg.RESIZABLE)
		self.clock = pg.time.Clock()

		self.active = False
		self.designated_speed = 0
		self.designated_timing = 60
		self.not100 = False
		self.FPS = 40

		self.center = self.scr.get_width()/2, self.scr.get_height()/2

		self.reset()
		self.sliders()
		self.effect = Effect(self)
		
		self.msg = Messages(self.scr)
	
	def sliders(self):
		
		randCols = [0, 50, 200, 250]
		
		self.startSlider = Slider(self.scr,
							pos_size=[200, 100, 160, 40],
							steps=10,
							colour=(randCols[random.randint(0, 3)],
											 randCols[random.randint(0, 3)],
											 randCols[random.randint(0, 3)]),
							secondary_colour=(randCols[random.randint(0, 2)],
											  randCols[random.randint(0, 2)],
											  randCols[random.randint(0, 2)]),
							)
		
		self.startSlider2 = Slider(self.scr,
							pos_size=[200, 50, 160, 40],
							steps=100,
							colour=(randCols[random.randint(0, 3)],
											 randCols[random.randint(0, 3)],
											 randCols[random.randint(0, 3)]),
							secondary_colour=(randCols[random.randint(0, 2)],
											  randCols[random.randint(0, 2)],
											  randCols[random.randint(0, 2)]),
							)
		
	def reset(self):

		self.timing = self.designated_timing
		self.speed = self.designated_speed
		self.score = 0
		self.combo = 1
		self.timer = 0
		self.effect.fireworks = []
		
	def mkBlock(self):
		
		randCols = [0, 50, 200, 250]
		
		b = Block(self.scr, self.speed, (
						randCols[random.randint(0, 3)],
						randCols[random.randint(0, 3)],
						randCols[random.randint(0, 3)]
						), self)
		
		self.blocklist.append(b)   
		
	def updateBlock(self, event):
		
		if len(self.blocklist) > 0:
			
			for e in event:
				if e.type == pg.KEYDOWN:
					
					if e.key in range(48, 58) or e.key in range(256, 266):
					
						if e.key == 48 + self.blocklist[0].ans or \
						e.key == 256 + self.blocklist[0].ans:

							##SCORE!

							self.effect.fireWork( 
								data={
								"pos" : self.blocklist[0].center, 
								"size" : 90,
								"radius" : 3,
								"speed" : 5,
								"timer" : 1,
								"dragindex" : 0.005,
								"type" : EffectTypes.DIFFUSE,
							   #"subtypes" : [EffectSubTypes.RAINBOW],
								"color" : self.blocklist[0].color
								} )	

							self.blocklist[0].terminate = True
							
							self.score += (1 + self.speed / 10) + \
							  self.combo * self.blocklist[0].ans
							self.combo += self.blocklist[0].ans / 50.0
							
						else:

							#WRONG KEY 
							self.score -= self.blocklist[0].ans
							self.combo -= 0.1
					
		toterminate = []
		
		for b in range(len(self.blocklist)):
			
			self.blocklist[b].update()
			
			if self.blocklist[b].terminate:
				toterminate.append(b)
				
			if self.blocklist[b].fail:
				self.score -= 2 * self.blocklist[b].ans
				self.combo -= 0.5
				self.effect.fireWork( 
					data={
					"pos" : self.blocklist[b].center, 
					"size" : 80,
					"radius" : 3,
					"speed" : 6,
					"timer" : 1.3,
					"dragindex" : 0.002,
					"type" : EffectTypes.EXPAND,
				   #"subtypes" : [EffectSubTypes.RAINBOW],
					"color" : self.blocklist[0].color
					} )	
				
		for b in toterminate:
				
			del self.blocklist[b]
			
	def draw(self):

		self.effect.draw()
	
		for b in self.blocklist:
			b.draw()
	
		self.msg.message(round(self.score, 2), [70, 40], pg.Color('blue'), 30)
		self.msg.message(round(self.timer / 40, 5), [70, 120], pg.Color('red'), 30)
		self.msg.message(round(self.combo, 2), [70, 80], pg.Color('darkgreen'), 30)
	
	def lose(self):

		done = 0

		self.msg.message("YOU LOSE!", [200, 200], pg.Color('red'), 45)
		
		self.msg.message(
			"YOU SURVIVED " + str(round( self.timer / 40, 2) ) + "s!",
			[200, 250], pg.Color('black'), 40)

		pg.display.flip()

		while not done:

			for e in pg.event.get():

				if e.type == pg.QUIT:
					pg.quit()
					quit()

				if e.type == pg.KEYDOWN:
					if e.key == pg.K_SPACE:
						done = 1
	
	def start(self):
		
		while not self.active:
			
			self.scr.fill(pg.Color('gray'))
			
			event = pg.event.get()
			for e in event:
				if e.type == pg.QUIT:
					pg.quit()
					quit()
				if e.type == pg.KEYDOWN:
					if e.key == pg.K_SPACE:
						self.loop()
			
			
			speed_sliderpos = self.startSlider.run(self.speed)
			timing_sliderpos = self.startSlider2.run(self.timing)
			
			self.designated_speed = speed_sliderpos + 1
			self.speed = speed_sliderpos + 1
			
			self.designated_timing = timing_sliderpos + 10
			self.timing = timing_sliderpos + 10
			
			self.designated_timing = timing_sliderpos
			
			self.msg.message("[SPACE]", [200, 200], pg.Color('magenta'), 45, 1)
			
			pg.display.update()
			self.clock.tick(40)
	
	def loop(self):
		
		self.active = True
		self.losing = False
		
		self.reset()
		
		self.blocklist = []
		
		while self.active:

			lasttime = time.time(  )
			
			self.scr.fill(pg.Color('gray'))
			event = pg.event.get()
			for e in event:
				if e.type == pg.QUIT:
					self.active = False
					
			if self.score < 0:
				self.active = False
				self.losing = True
			
			self.timer += 1
			self.speed += 0.003
			self.timing -= 0.005
			self.combo -= 0.01 / 40
			
			if self.combo <= 0.5:
				self.combo = 0.5
				
			if self.timer % int(self.timing + 1) == 0:
				self.mkBlock()

			self.effect.update()
				
			self.updateBlock(event)
			self.draw()

			self.FPS = 1.0 / ( time.time(  ) - lasttime )
			self.msg.message( round( self.FPS, 1 ), ( 500, 20 ), size=25 )
			
			pg.display.flip()
			
			self.clock.tick(self.FPS)
		
		if self.losing:
			self.lose()
			
running = Run()
running.start()
		
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
			
			
			
			
			
			
			
			
			
			
			
			
			
			