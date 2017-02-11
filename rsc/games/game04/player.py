import pygame as p
import time

from math import *
from random import *

import utils, message


class Player:

	def __init__( self, main, **kwargs ):

		self.main = main

		self.score = Score( self )

		self.press = { "up" : 0, "left" : 0, "down" : 0, "right" : 0 }
		self.dead = 0
		self.points = self.combo = self.misclicks = self.misses = self.hits = 0
		self.arrows_gone_by = 0
		self.easymode = 0
		self.arrowrate = 30
		self.scoreboardside = -1
		self.totalarrows = 0
		
		self.endtimer = 0

		self.pressarrow_color = (150,0,255)

		for arg in kwargs:
			setattr( self, arg, kwargs[ arg ] )


	def wrong( self ):
		self.misclicks += 1
		self.combo = 0

	def miss( self ):
		self.combo = 0
		self.misses += 1

	def hit( self ):
		self.points += 1 + self.combo / 10.0
		self.combo += 1
		self.hits += 1

		if self.combo == 10: self.main.handler.effect.mkPopUpMessage(
			(200,220,0), [self.pos[0], self.main.size[1] / 2], "10 STREAK!", 30, 80, { "italic" : 1 } )
		if self.combo == 50: self.main.handler.effect.mkPopUpMessage(
			(0,220,200), [self.pos[0], self.main.size[1] / 2], "50 STREAK!", 40, 120, { "italic" : 1 } )
		if self.combo == 100: self.main.handler.effect.mkPopUpMessage(
			(255,0,0), [self.pos[0], self.main.size[1] / 2], "100 STREAK!", 60, 200, { "italic" : 1, "bold" : 1 } )

	def up( self ):
		self.press[ "up" ] = time.time(  )
		self.main.handler.effect.mkPressArrow( self.pressarrow_color, self.pos, 0 ) # 0 for UP
		if self.check_wrong(  ): self.press[ "up" ] = 0

	def left( self ):
		self.press[ "left" ] = time.time(  )
		self.main.handler.effect.mkPressArrow( self.pressarrow_color, self.pos, 1 ) # 0 for UP
		if self.check_wrong(  ): self.press[ "left" ] = 0

	def down( self ):
		self.press[ "down" ] = time.time(  )
		self.main.handler.effect.mkPressArrow( self.pressarrow_color, self.pos, 2 ) # 0 for UP
		if self.check_wrong(  ): self.press[ "down" ] = 0

	def right( self ):
		self.press[ "right" ] = time.time(  )
		self.main.handler.effect.mkPressArrow( self.pressarrow_color, self.pos, 3 ) # 0 for UP
		if self.check_wrong(  ): self.press[ "right" ] = 0

	def check_wrong( self ):
		if not self.arrow_in_reach and not self.easymode: # arrow might still hit, even though you get a fault
			self.wrong(  )
			return 1
		else: return 0

	def draw( self ):
		
		p.draw.rect( self.main.scr, self.color, ( self.pos[ 0 ] - 100, self.pos[ 1 ]-1, 200, 2 ) )

		self.score.draw(  )

	def update( self ):
		self.arrow_in_reach = 0

		for arrow in self.main.handler.arrowlist:
			if arrow.limits[ 0 ] - 20 < self.pos[ 1 ] - arrow.pos[ 1 ] < arrow.limits[ 1 ] + 20: self.arrow_in_reach = 1; break

		for e in self.main.handler.events:
			if e.type == p.KEYDOWN:

				if   e.key == self.ULDR[ 0 ]: self.up(  )
				elif e.key == self.ULDR[ 1 ]: self.left(  )
				elif e.key == self.ULDR[ 2 ]: self.down(  )
				elif e.key == self.ULDR[ 3 ]: self.right(  )



class Score:

	def __init__( self, player ):

		self.player = player
		self.main = player.main

	def draw( self ):

		p = self.player
		d = p.pos[ 0 ] + 120*p.scoreboardside
		ratio = 0

		try: 
			ratio = float(p.hits)/p.arrows_gone_by
			per = str( format( round( ratio * 100, 2 ), ".2f" ) ) + "%"
		except: per = "%"


		message.msg( self.main.scr,	str(p.hits) + "/" + str(p.arrows_gone_by),
													[ d, 10 ],			(0,0,255), weight=p.scoreboardside )
		if p.arrows_gone_by: 
			message.msg( self.main.scr,	per,		[ d, 30 ],			(225*(1-ratio), 225*ratio, 0),
																			size=20, weight=p.scoreboardside )

		message.msg( self.main.scr, p.points, 		[ d, 100 ],			(0,0,200), weight=p.scoreboardside )
		message.msg( self.main.scr, p.combo, 		[ d, 130 ],			(0,200,0), weight=p.scoreboardside )
		message.msg( self.main.scr, p.misclicks, 	[ d, 160 ],			(200,0,0), weight=p.scoreboardside )
		message.msg( self.main.scr, p.misses, 		[ d, 190 ],			(200,200,0), weight=p.scoreboardside )

		message.msg( self.main.scr, p.totalarrows,
													[ p.pos[ 0 ], 20 ],	(100,200,230), weight=p.scoreboardside )