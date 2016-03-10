## -*- coding:latin-1 -*-

from kivy.app import App
from kivy.clock import Clock
from kivy.graphics import Rectangle, Line, Color
from kivy.uix.widget import Widget
from kivy.core.window import Window

from random import *



class MainWidget( Widget ):

	galaxies = [  ]
	lines = [  ]
	layers = 6
	stars = 100

	layerW = Window.width
	layerH = Window.height

	layerW = 1920
	layerH = 1080

	pos = 0, 0
	mov = 0, 0
	
	def __init__( self, **kwargs ):
		super( MainWidget, self ).__init__( **kwargs )


		with self.canvas:
			for d in range( self.layers ):
				starList = [  ]
				for i in range( self.stars ):
					rect = Rectangle( pos=[ random() * self.layerW, random() * self.layerH ],
									  size=[ (self.layers-d) / 2., (self.layers-d) / 2. ] )
					starList.append( rect )
				self.galaxies.append( starList )

			Color( 0, 1, 0, 1 )

			for i in range( 5 ):
				selects = [  ]
				points = [  ]
				selects.append( self.galaxies[ randrange( 0, self.layers ) ][ randrange( 0, self.stars ) ] )
				chosen = self.galaxies[ randrange( 0, self.layers ) ][ randrange( 0, self.stars ) ]
				selects.append( chosen )

				points = selects[ 0 ].pos[ 0:2 ] + selects[ 1 ].pos[ 0:2 ]
				self.lines.append( [ Line( points=points, width=1 ), selects ] )

	def update( self, dt ):
		for i in range(len(self.lines)):

			points = self.lines[ i ][ 1 ][ 0 ].pos[ 0:2 ] + self.lines[ i ][ 1 ][ 1 ].pos[ 0:2 ]
			self.lines[ i ][ 0 ].points = points
			

	def on_touch_move( self, touch ):
		pos = touch.pos
		self.mov = pos[ 0 ] - self.pos[ 0 ], pos[ 1 ] - self.pos[ 1 ]
		
		for d in range( len( self.galaxies ) ):
			for i in range( self.stars ):
				self.galaxies[ d ][ i ].pos = \
					[ self.galaxies[ d ][ i ].pos[ 0 ] + self.mov[ 0 ] / (d + 1),
					  self.galaxies[ d ][ i ].pos[ 1 ] + self.mov[ 1 ] / (d + 1) ]

		self.pos = pos

	def on_touch_down( self, touch ):
		self.pos = touch.pos


class Main( App ):

	def build( self ):

		self.parent = Widget(  )

		mainW = MainWidget(  )
		self.parent.add_widget( mainW )

		Clock.schedule_interval(mainW.update, 1.0 / 60.0)

		return self.parent



if __name__ == '__main__':
	Main(  ).run(  )