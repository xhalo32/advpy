import pygame as p
from random import *

class Enemies:
	class Enemy:
		def __init__( self, par, c, x, y, w, h, spd ):
			self.c = c
			self.x = x
			self.lx = x
			self.y = y
			self.w = w
			self.h = h
			self.p = par
			self.main = par.main
			self.playerlist = self.main.playerlist

			self.vx = self.vy = 0
			self.speed = spd
			self.direction = 0
			self.timer = 0
			self.stay = False
			self.dead = False
		def update( self ):
			self.timer += 1
			if self.timer % 10 == 0:
				randplayer = self.playerlist[ randrange( 0, len( self.playerlist ) ) ]
				self.target = randplayer
				try:
					self.direction = ( self.target.x - self.x ) / abs( self.target.x - self.x )
				except: self.direction = 0
			self.vx = self.direction * self.speed
			self.x += self.vx
			if self.timer % 30 == 0 or int( self.lx ) == int( self.x ):
				self.jump(  )
			self.y += self.vy
			if self.y < self.main.scr.get_height(  ):
				self.vy += .35
				self.stay = False
			else: 
				self.vy = 1
				self.stay = True
				self.y = self.main.scr.get_height(  )
			for b in self.main.objectlist:
				if b.y < self.y < b.y + b.h + self.h:
					if b.x + b.w + self.vx <= self.x < b.x + b.w:
						self.x -= self.vx
					if b.x + self.vx >= self.x + self.w > b.x:
						self.x -= self.vx
				if b.x - self.w < self.x < b.x + b.w:
					if b.y <= self.y < b.y + self.vy:
						self.y = b.y
						self.vy = 0
						self.stay = True
					if b.y + b.h > self.y - self.h >= b.y + b.h + self.vy - 1:
						self.vy = 0
						self.y = b.y + b.h + self.h
			self.lx = float( self.x )
		def jump( self ):
			if self.stay: self.vy = -7
		def draw( self ):
			p.draw.rect( self.main.scr, self.c,
				[ int( self.x ), int( self.y - self.h ), int( self.w ), int( self.h ) ] )

	def __init__( self, main ):
		self.main = main
		self.elist = [  ]
		self.elist.append( self.Enemy( self, ( 255, 0, 0 ), 300, 300, 20, 40, 2 ) )
	def update( self ):
		l = list( self.elist )
		for b in self.elist:
			b.update(  )
			if b.dead: l.remove( b )
		self.elist = l
	def draw( self ):
		for e in self.elist:
			e.draw(  )