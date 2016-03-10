from random import random, randint
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.graphics import Color, Ellipse, Line
from kivy.graphics.vertex_instructions import Rectangle
from kivy.uix.slider import Slider
from kivy.uix.label import Label
from kivy.clock import Clock



class NumberWidget( Widget ):

	labelList = [  ]
	speed = 120
	max_speed = 20
	time = 0
	tick = 0
	points = 0

	def update( self, dt ):
		if self.time == 0:
			with self.canvas:
				self.pointLabel = Label( pos=[ 0, 900 ], text=str(self.points), font_size=50 )
		self.time += dt
		self.tick += 1

		if self.tick % int(self.speed) == 0:
			if self.speed > self.max_speed: self.speed -= 1

			with self.canvas:
				Color( random(  ), random(  ), random(  ), 1 )
				x = 1820 * random()
				rect = Rectangle( pos=[ x -10, 1080 + 20 ], size=[ 120, 60 ] )
				lab = Label( pos=[ x, 1080 ], text=str(randint(1,5))+" + "+str(randint(0,5)), font_size=50 )
				self.labelList.append( [ lab, rect ] )

		lol = self.labelList
		for l in range(len(self.labelList)):

			self.labelList[ l ][ 0 ].pos[ 1 ] -= (130 - self.speed) / 10.
			self.labelList[ l ][ 1 ].pos = [ self.labelList[ l ][ 1 ].pos[0], self.labelList[ l ][ 1 ].pos[ 1 ] - (130 - self.speed) / 10. ]

			if self.labelList[ l ][ 0 ].pos[ 1 ] < 80:
				t = self.labelList[ l ][ 0 ].text

				am = int( t[ 0 ] ) + int( t[ 4 ] )
				self.points = self.points - 2*am

				lol.remove( l )
				self.labelList[ l ][ 0 ].text=""
				self.labelList[ l ][ 0 ].font_size = 0
				self.labelList[ l ][ 1 ].size = [ 0,0 ]

		self.labelList = lol

		self.pointLabel.text = str( self.points )

	def _press( self, o ):
		self.press( int(o.text) )

	def press( self, n ):
		if self.labelList:
			t = self.labelList[ 0 ][ 0 ].text

			if int( t[ 0 ] ) + int( t[ 4 ] ) == n:

				self.points += n
				lol = self.labelList
				self.labelList[ 0 ][ 0 ].text = ""
				self.labelList[ 0 ][ 1 ].size = [ 0,0 ]
				lol.remove( self.labelList[ 0 ] )
				self.labelList = lol

class NumberApp( App ):

	def buildNums( self ):

		for i in range( 1, 11 ):
			print i
			btn = Button( text=str( i ), pos=( 150 * (i-1) + 192, 0 ), size=( 150, 100 ), background_color=( 1, 0, 1, 0.3 ), color=( 1, 1, 1, 1 ) )
			btn.bind( on_press=self.main._press )

			self.parent.add_widget( btn )

	def build( self ):

		self.parent = Widget(  )

		self.main = NumberWidget(  )

		self.buildNums(  )
		Clock.schedule_interval(self.main.update, 1.0 / 60.0)
		self.parent.add_widget(self.main)

		return self.parent

if __name__ == '__main__':
	NumberApp().run()