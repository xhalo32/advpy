from random import random
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.graphics import Color, Ellipse, Line
from kivy.uix.slider import Slider



class MyPaintWidget( Widget ):
	color = ( 1, 1, 1 )
	w = 1
	slider = Slider( min=1, max=10, value=1, orientation="horizontal", pos=( 500, 0 ), size=( 200, 100 ) )

	def on_touch_down( self, touch ):

		if touch.y > 100:
			with self.canvas:

				Color( *self.color, mode='hsv' )

				d = 5 * self.w
				Ellipse( pos=( touch.x - d / 2, touch.y - d / 2), size=(d, d))
				
				# ud means user data
				touch.ud[ 'line' ] = Line( points=( touch.x, touch.y ) )

	def on_touch_up( self, touch ):

		if touch.y > 100:
			with self.canvas:
				d = 5 * self.w
				Ellipse( pos=( touch.x - d / 2, touch.y - d / 2), size=(d, d))

	def on_touch_move( self, touch ):

		if touch.y > 100:
			touch.ud[ 'line' ].points += [touch.x, touch.y]
			touch.ud[ 'line' ].width = self.w
		else:
			self.w = self.slider.value


class MyPaintApp(App):

	def build( self ):
		parent = Widget(  )
		self.painter = MyPaintWidget(  )

		clearbtn = Button( text='Clear' )
		clearbtn.bind( on_release=self.clear_canvas )
		
		Gbtn = Button( text='GREEN', pos=( 100, 0 ) )
		Gbtn.bind( on_release=self.green_color )
				
		Rbtn = Button( text='RED', pos=( 200, 0 ) )
		Rbtn.bind( on_release=self.red_color )

		Bbtn = Button( text='BLUE', pos=( 300, 0 ) )
		Bbtn.bind( on_release=self.blue_color )
					
		Mbtn = Button( text='MAGENTA', pos=( 400, 0 ) )
		Mbtn.bind( on_release=self.mag_color )
		
		parent.add_widget(self.painter)
		parent.add_widget(self.painter.slider)

		parent.add_widget(clearbtn)
		parent.add_widget(Gbtn)
		parent.add_widget(Rbtn)
		parent.add_widget(Bbtn)
		parent.add_widget(Mbtn)

		return parent

	def clear_canvas( self, obj ):
		self.painter.canvas.clear()

	def green_color( self, obj ):
		self.painter.color = ( 0.3, 1, 1 )

	def red_color( self, obj ):
		self.painter.color = ( 1, 1, 1 )

	def blue_color( self, obj ):
		self.painter.color = ( 0.6, 1, 1 )

	def mag_color( self, obj ):
		self.painter.color = ( 0.8, 1, 1 )


if __name__ == '__main__':
	MyPaintApp().run()