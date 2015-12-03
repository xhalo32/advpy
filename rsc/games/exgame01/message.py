import pygame
pygame.font.init(  )

class Messages(  ):

	def __init__( self, scr ):

		self.scr = scr

	def message( self, text, pos, color = (255,255,255), size = 25, bold = 0, italic = 0 ):
		font = pygame.font.SysFont( 'Ubuntu Mono', size, bold, italic )
		label = font.render( str( text ), 1, color )
		self.scr.blit( label, pos )