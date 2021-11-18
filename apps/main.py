from kivy.app import App
from kivy.lang import Builder
from kivy.event import EventDispatcher
from kivy.network.urlrequest import UrlRequest
from kivy.properties import ListProperty
from kivy.clock import Clock

kv = """
BoxLayout:
    orientation: 'vertical'
    Label:
        id: label
        text_size: self.size
        valign: 'center'
        halign: 'center'
        padding: 10,10
        font_size: 40
    Button:
        size_hint_y: None
        height: 48
        text: 'Get Cat Facts'
        on_release: app.aw.check_net()
"""


class AccessWeb(EventDispatcher):
    facts = ListProperty()

    def check_net(self):
        UrlRequest('https://cat-fact.herokuapp.com/facts', on_success=self.net_success)

    def net_success(self,req, r):
        print(f'Success: {req.is_finished}')
        self.facts.clear()
        for fact in r:
            self.facts.append(fact['text'])
        print(self.facts)
        app = App.get_running_app()
        app.root.ids.label.text = self.facts[0]




class TestAccessWebApp(App):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cnt = 0
        self.aw = None

    def build(self):
        self.aw = AccessWeb()
        return Builder.load_string(kv)

    def on_start(self):
        Clock.schedule_interval(self.display_cat_fact, 5)

    def display_cat_fact(self, dt):
        if self.aw.facts:
            self.root.ids.label.text = self.aw.facts[self.cnt]
            self.cnt = (self.cnt+ 1) % len(self.aw.facts)


TestAccessWebApp().run()

