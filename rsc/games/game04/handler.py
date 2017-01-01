import pygame as p
from player import *
from arrow import *
from generator import *

import utils



class Handler:

	def __init__( self, main ):

		self.main = main
		self.Player = Player
		self.Arrow = Arrow
		self.effect = utils.Effect( self.main )

		self.playerlist = [  ]
		self.generator = Generator( self.main )

		self.arrowlist = [  ]

		self.events = [  ]

		self.effect.mkPopUpMessage( (10,210,20), (400,300), "START", 100, 120, { "italic" : 1 } )


	def handle_events( self ):

		self.events = p.event.get(  )

		for e in self.events:
			if e.type == p.QUIT: self.main.active = 0
			elif e.type == p.KEYDOWN: 
				if e.key == p.K_r: self.main.reset(  )

	def create_player( self, **kwargs ):
		self.playerlist.append( self.Player( self.main, **kwargs ) )

	def create_arrow( self, **kwargs ):
		self.arrowlist.append( self.Arrow( self.main, **kwargs ) )

	def draw( self ):

		self.effect.draw(  )

		for player in self.playerlist: player.draw(  )
		for arrow in self.arrowlist: arrow.draw(  )

		self.effect.drawlate(  )

	def update( self ):
		self.handle_events(  )

		aliveplayers = [ player for player in self.playerlist if player.dead == 0 ]
		self.playerlist = aliveplayers

		alivearrows = [ arrow for arrow in self.arrowlist if arrow.dead == 0 ]
		self.arrowlist = alivearrows

		for player in self.playerlist: player.update(  )
		for arrow in self.arrowlist: arrow.update(  )

		self.generator.update(  )

		self.effect.update(  )