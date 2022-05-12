from turtle import textinput
import kivy
kivy.require('2.1.0') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

class LoginScreen(GridLayout):
    
    def __init__(self, **kwargs):
        # Super implements the original overclass functionality
        # good practice not to remove the **kwargs while calling super
        super(LoginScreen, self).__init__(**kwargs)
        
        # GridLayout variables
        # Widgets use size hint by default
        self.cols = 2
        self.add_widget(Label(text = "User Name"))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)
        self.add_widget(Label(text = "password"))
        self.password = TextInput(password = True, multiline = False)
        self.add_widget(self.password)

class MyApp(App):

    def build(self):
        return LoginScreen()


if __name__ == '__main__':
    MyApp().run()