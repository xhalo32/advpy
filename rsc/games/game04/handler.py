import pygame as p
from player import *
from arrow import *

from utils import *



class Handler:

	def __init__( self, main ):

		self.main = main
		self.Player = Player
		self.Arrow = Arrow
		self.effect = Effect( self.main )

		self.playerlist = [  ]
		self.arrowlist = [  ]

		self.totalarrows = 0
		self.events = [  ]


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
		self.totalarrows += 1

	def draw( self ):

		self.effect.draw(  )

		for player in self.playerlist: player.draw(  )
		for arrow in self.arrowlist: arrow.draw(  )

	def update( self ):
		self.handle_events(  )

		aliveplayers = [ player for player in self.playerlist if player.dead == 0 ]
		self.playerlist = aliveplayers

		alivearrows = [ arrow for arrow in self.arrowlist if arrow.dead == 0 ]
		self.arrowlist = alivearrows

		for player in self.playerlist: player.update(  )
		for arrow in self.arrowlist: arrow.update(  )

		self.effect.update(  )