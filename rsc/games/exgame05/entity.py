import pygame as p
from entitytypes import EntityTypes



class Entities:

	class Entity:

		def __init__( self, *args ):

			self.args = args

			for i in list( self.args ):
				for l in list( i ):
					setattr( self, l, i[ l ] )

			self.type = getattr( EntityTypes, self.type )( self )

			

	def e_init( self ):

		self.entitylist = [  ]

	def e_mkEntity( self, *args ):

		e = self.Entity( *args )
		self.entitylist.append( e )
		return e