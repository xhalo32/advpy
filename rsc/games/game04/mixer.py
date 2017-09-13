import pygame as p


#p.mixer.init( frequency=22050, channels=1, buffer=4096 )


class Mixer:

	def __init__( self, main ):

		self.main = main

		self.note1 = p.mixer.Sound( "note1.wav" )
		self.note2 = p.mixer.Sound( "note2.wav" )
		self.note3 = p.mixer.Sound( "note3.wav" )
		self.note4 = p.mixer.Sound( "note4.wav" )

	def play( self, sound ):

		getattr( self, sound ).play(  )
