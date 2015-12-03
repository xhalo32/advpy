import pygame as pg

pg.font.init(  )

class Messages(  ):

    def __init__( self, scr ):
        self.scr = scr
    def message( self, text, pos, color = (255,255,255), size = 20, bold = 0, italic = 0 ):
        font = pg.font.SysFont( 'Ubuntu Mono', size, bold, italic )
        label = font.render( str( text ), 1, color )
        rect = label.get_rect()
        rect.center = pos
        self.scr.blit( label, rect )
        