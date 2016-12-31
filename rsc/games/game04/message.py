import pygame as p
p.font.init()



def msg( window, text, pos, color=( 255,255,255 ), size=25, bold=0, italic=0, centered=False, align_to_screen=False, background=( ( 0,0,0 ), 0 ) ):
	font = p.font.SysFont( 'Ubuntu Mono', int( size ), bold, italic )
	label = font.render( str( text ), 1, color )

	rect = label.get_rect(  )

	if background[ 1 ] == 1:
		p.draw.rect( window, background[ 0 ], rect )


	if not align_to_screen:
		
		if centered:
			window.blit( label, [ int( pos[ 0 ] - rect[ 2 ] / 2. ), int( pos[ 1 ] -rect[ 3 ] / 2. ) ] )
		else:
			window.blit( label, pos )

	
	elif align_to_screen:

		if rect[ 2 ] <= window.get_width(  ):
			window.blit( label, pos )

		if rect[ 2 ] > window.get_width(  ):
			window.blit( label, [ int( pos[ 0 ] - ( rect[ 2 ]-window.get_width(  ) ) ), int( pos[ 1 ] ) ] )