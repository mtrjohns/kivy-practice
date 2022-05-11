import kivy
kivy.require('1.9.0')

from kivy.app import App
from kivy.uix.button import Label

# hellokivy.kv will need to be made to assign it to the HelloKivyApp
class HelloKivyApp(App):

    def build(self):
        return Label()

helloKivy = HelloKivyApp()

helloKivy.run()