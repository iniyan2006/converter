
from kivy.app import App
from kivy.lang import Builder
from kivy.event import EventDispatcher
from kivy.network.urlrequest import UrlRequest
from kivy.properties import ListProperty
from kivy.clock import Clock

kv = """
BoxLayout:
    orientation: 'vertical'
    AsyncImage:
        id: image
        source: "https://random.dog/1ae6411b-8f81-438a-a793-7642a3e61128.jpg"
    Button:
        size_hint_y: None
        height: 48
        text: 'Get Dog Image'
        on_release: app.aw.check_net()
"""


class AccessWeb(EventDispatcher):
    facts = ListProperty()

    def check_net(self):
        UrlRequest('https://random.dog/woof', on_success=self.net_success)

    def net_success(self,req, r):
        print(f'Success: {req.is_finished}')
        self.dog.clear()
        self.dog.append(f"https://random.dog/{r}")
        print(str(r))
        print(self.dog)
        app = App.get_running_app()
        app.root.ids.image.source = self.facts[0]


class TestAccessWebApp(App):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cnt = 0
        self.aw = None

    def build(self):
        self.aw = AccessWeb()
        return Builder.load_string(kv)

    def on_start(self):
        Clock.schedule_interval(self.display_dog_image, 5)

    def display_dog_image(self, dt):
        if self.aw.dog:
            self.root.ids.image.source = self.aw.dog[0]


TestAccessWebApp().run()
