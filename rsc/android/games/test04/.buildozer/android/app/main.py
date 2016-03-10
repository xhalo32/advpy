## -*- coding:latin-1 -*-

from kivy.app import App
from random import *

from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.scatter import Scatter
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout



class ScatterTextWidget( BoxLayout ):
	
	def CRC( self, *args ):
		color = [ random(  ) for i in xrange( 3 ) ] + [ 1 ]
		self.ids.text_label.color = color
		self.ids.label1.color = color
		self.ids.label2.color = color


class TutorialApp( App ):

	def build( self ):
		return ScatterTextWidget(  )

if __name__ == '__main__':
	TutorialApp(  ).run(  )