## -*- coding:latin-1 -*-

from kivy.app import App
from kivy.lang import Builder

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.settings import *

from settings_json import settings_json

Builder.load_string( '''
<Interface>:
	orientation: 'vertical'
	Button:
		text: "Settings"
		font_size: 150
		on_release: app.open_settings(  )

''' )

class Interface( BoxLayout ):
	pass

class SettingsApp( App ):
	def build( self ):
		self.settings_cls = SettingsWithSidebar
		# self.config.items( 'example' )
		# self.config.get( 'example', 'boolex' )
		#self.use_kivy_settings = False
		# setting = self.config.get( 'example', 'boolex' )
		return Interface(  )

	def build_config( self, config ):
		config.setdefaults( 'example', { 
			'boolex' : True,
			'intex' : 20,
			'optionex' : '2',
			'stringex' : 'Strings',
			'pathex' : '/some/path',

		} )

	def build_settings( self, settings_widget ):
		settings_widget.add_json_panel( 'Panel Name',
										self.config,
										data=settings_json
										)

	def on_config_change( self, *args ): ## args = config, section, key, value
		print args


SettingsApp(  ).run(  )