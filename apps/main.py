from kivy.app import App
import kivy
from kivy.uix.label import Label
import requests
class Main(App):
    def build(self):
        rq = requests.get("https://random.dog/woof.json")
        return Label(text=str(rq.content))

Main().run()
