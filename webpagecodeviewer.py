from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.modalview import ModalView
from kivy.properties import StringProperty, ObjectProperty
from kivy.uix.rst import RstDocument
from kivy.lang import Builder
from kivy.app import App

import requests

Builder.load_string('''
<Texttest>:
	orientation:'vertical'
	canvas.before:
		Color:
			rgba:(0.6,0.6,.9,1)
		Rectangle:
			pos:self.pos
			size:self.size
	BoxLayout:
		size_hint:(1,0.1)
		TextInput:
			id:text_input
			size_hint_y:None
			height:'48dp'
		Button:
			text:'search'
			on_press:root.text_value()
			size_hint_y:None
			height:'48dp'
			size_hint_x:None
			width:'48dp'
	BoxLayout:
		size_hint:(1,1)
		RstDocument:
			size_hint:(0.98,0.98)
			text:root.text_values
			
 ''')
class Texttest(BoxLayout):
	text_input  = ObjectProperty()
	text_values = StringProperty('')
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		
		self.modal_error = ModalView(size_hint=(None,None),size=(400,400))
		
	def text_value(self):
		self.text_values = self.ids.text_input.text
		if self.text_values.startswith('http://') or self.text_values.startswith('https://'):
			content = requests.get(self.text_values).content
			self.text_values = str(content)
		else:
			self.modal_error.add_widget(Label(text='invalid url must start with http://'))
			self.modal_error.open()
		print(self.text_values)
		
class Main(App):
		
		def build(self):
			return Texttest()
			
		
if __name__ == '__main__':
		Main().run()
		
		
	