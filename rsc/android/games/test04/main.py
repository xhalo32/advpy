## -*- coding:latin-1 -*-

from kivy.app import App
from random import *

from kivy.properties import *
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.scatter import Scatter
from kivy.animation import Animation
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics.vertex_instructions import *
from kivy.graphics.context_instructions import *


class ScatterTextWidget( BoxLayout ):

	text_color = ListProperty( [ 1, 1, 1, 1 ] )

	def __init__( self , **kwargs ):
		super( ScatterTextWidget, self ).__init__( **kwargs )
	
	def CRC( self, *args ):
		self.text_color = [random() for i in xrange(3)]+[1]


class TutorialApp( App ):

	def build( self ):
		return ScatterTextWidget(  )

if __name__ == '__main__':
	TutorialApp(  ).run(  )