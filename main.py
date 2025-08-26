from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.clock import Clock
import random

class ClaytonIsTheBest(App):

    def build(self):
        global randomres
        self.window = BoxLayout(orientation='vertical')
        self.window.cols = 1
        self.window.size_hint = (0.8, 0.8)
        self.window.pos_hint = {"center_x":0.5, "center_y":0.5}
        randomres = random.randint(0,10)
        image = Image(source="LIS.png")
        self.window.add_widget(image)

        self.welcome = Label(text="Welcome to LIS Student Prediction System")

        self.input = TextInput(multiline=False)

        self.result = Button(text="Get Answer")
        self.result.bind(on_press=self.button_clicked)

        self.window.add_widget(self.welcome)
        self.window.add_widget(self.input)
        self.window.add_widget(self.result)


        return self.window

    def button_clicked(self,instance):
            randomres = random.randint(0,10)
            if randomres >= 5:
                self.resulto = Label(text="The Student " + self.input.text + " is a " + "Good Student")
            if randomres < 5:
                self.resulto = Label(text="The Student " + self.input.text + " is a " + "Bad Student")
            self.window.add_widget(self.resulto)

ClaytonIsTheBest().run()