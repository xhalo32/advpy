## -*- coding:latin-1 -*-

from kivy.app import App
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.graphics import Rectangle, Line, Color
from kivy.properties import *
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.uix.scrollview import ScrollView

from random import *

Builder.load_string( '''
<ScrollableLabel>:
	text: ""
	Label:
		text: root.text
		font_size: 50
		text_size: self.width, None
		size_hint_y: None
		height: self.texture_size[ 1 ]

''' )

class ScrollableLabel( ScrollView ):
	text = StringProperty( "" )
	plist = [ 2 ]

	def update( self, dt ):
		self.size = self.parent.size
		self.text += "\n" + self.nextPrime(  )

	def nextPrime( self ):
		for i in range( 100 ):
			t = self.plist[ -1 ] + i
			plist = [  ]

			for p in self.plist:
				if t % p:
					plist.append( False )
				elif t == p:
					pass
				else:
					plist.append( True )

				if all( plist ):
					return t


class Main( App ):

	def build( self ):

		self.parent = Widget(  )

		mainS = ScrollableLabel(  )

		self.parent.add_widget( mainS )

		Clock.schedule_interval( mainS.update, 1.0 / 10.0 )

		return self.parent



if __name__ == '__main__':
	Main(  ).run(  )