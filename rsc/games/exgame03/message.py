import pygame
pygame.font.init(  )

class Messages(  ):

	@classmethod
	def message( self, window, text, pos, color = (255,255,255), size = 25, bold = 0, italic = 0 ):
		font = pygame.font.SysFont( 'Ubuntu Mono', size, bold, italic )
		label = font.render( str( text ), 1, color )
		window.blit( label, pos )