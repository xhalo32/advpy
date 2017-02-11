import pygame as p
import time

from math import *

import utils


class Arrow:

	def __init__( self, main, **kwargs ):

		self.main = main

		self.active = 1

		self._strength = 20
		self.strength = self._strength
		self.dead = 0
		self.hit = [ 0,0 ]
		self.speed = 3
		self.precision = 0.2		# must be greater than time spent in limits
		self.limits = [ -20,10 ] 	# 0: upper 1: lower
		self.button_delta = 40
		self.order = "LDUR"

		for arg in kwargs:
			setattr( self, arg, kwargs[ arg ] )

		self.color = self._color
		self._color2 = ( 255, 10, 200 )

		self.dir = [ 0,0 ]
		if "U" in self.button: self.dir[ 1 ] = -1
		if "L" in self.button: self.dir[ 0 ] = -1
		if "D" in self.button: self.dir[ 1 ] = 1
		if "R" in self.button: self.dir[ 0 ] = 1

		self.difangle = utils.get_angle( self.dir )


	def draw( self ):

		# for one arrow
		#p.draw.polygon( self.main.scr, self.color, utils.triangle( self.pos, self.strength, self.difangle - 180 ) )

		# for multiple arrows

		tl = abs(float(self.pos[ 1 ] + 30)) / 100.0 # translate effect
		if tl > 1: tl = 1

		for b in self.button:
			p.draw.polygon( self.main.scr, self.color,

				utils.arrow( self.pos, "ULDR".index( b ), unit=tl, delta=self.button_delta, order=self.order ) )


	def update( self ):

		self.pos[ 1 ] += self.speed
		if self.pos[ 1 ] > self.main.size[ 1 ] - 50: self.strength = ( self.main.size[ 1 ] - self.pos[ 1 ] ) / 50.0 * self._strength

		if self.pos[ 1 ] > self.main.size[ 1 ]:

			self.owner.miss(  )

			for b in self.button:
				self.main.handler.effect.mkExplosion( self._color, ( 0,0,0 ), 2, 2, 5, 60,
					[ self.pos[ 0 ] + self.button_delta * ( -1.5 + self.order.index( b ) ), self.pos[ 1 ] ] )

			self.dead = 1


			# when in range of player

		if self.limits[ 0 ] < self.owner.pos[ 1 ] - self.pos[ 1 ] < self.limits[ 1 ]:

			self.color = self._color2

			'''for button in self.button:
			
				if button == "U":
					if time.time(  ) - self.owner.press[ "up" ] < self.precision: self.hit[ 1 ] = -1
				if button == "L":
					if time.time(  ) - self.owner.press[ "left" ] < self.precision: self.hit[ 0 ] = -1
				if button == "D":
					if time.time(  ) - self.owner.press[ "down" ] < self.precision: self.hit[ 1 ] = 1
				if button == "R":
					if time.time(  ) - self.owner.press[ "right" ] < self.precision: self.hit[ 0 ] = 1
			'''

			if self.active:
				if time.time(  ) - self.owner.press[ "up" ] < self.precision: self.hit[ 1 ] = -1; self.owner.press[ "up" ] = 0
				if time.time(  ) - self.owner.press[ "left" ] < self.precision: self.hit[ 0 ] = -1; self.owner.press[ "left" ] = 0
				if time.time(  ) - self.owner.press[ "down" ] < self.precision: self.hit[ 1 ] = 1; self.owner.press[ "down" ] = 0
				if time.time(  ) - self.owner.press[ "right" ] < self.precision: self.hit[ 0 ] = 1; self.owner.press[ "right" ] = 0

					# test for correct buttons

				if self.hit == self.dir:

					if "U" in self.button:
						self.main.handler.mixer.play( "note1" )
					if "R" in self.button:
						self.main.handler.mixer.play( "note2" )
					if "D" in self.button:
						self.main.handler.mixer.play( "note3" )
					if "L" in self.button:
						self.main.handler.mixer.play( "note4" )

					self.owner.hit(  )
					for b in self.button:
						self.main.handler.effect.mkExplosion( self._color, self._color2, 1, 2, 20, 60,
	[ self.pos[ 0 ] + self.button_delta * ( -1.5 + self.order.index( b ) ), self.pos[ 1 ] ] ) # explosions everywhere

					self.dead = 1

					# test if wrong button is pressed: disable tests

				for i in range( 2 ):
					if self.hit[ i ] != self.dir[ i ] and self.hit[ i ] != 0:

						self.hit[ i ] = 0
						self.owner.wrong(  )
						self.active = 0
						break



		elif self.owner.pos[ 1 ] - self.pos[ 1 ] < self.limits[ 1 ]: self.color = self._color

		if self.dead: self.owner.arrows_gone_by += 1