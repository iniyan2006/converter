from kivy.app import App 

from kivy.uix.label import Label 

from kivy.network.urlrequest import UrlRequest

from kivy.properties import StringProperty

from kivy.lang import Builder


kv = """

BoxLayout:

    orientation: 'vertical'

    Label:
        id : text

        text: 'hello world'

    TextInput:
        id: input

        hint_text: 'Paste url'
        on_text: app.process()
    Button:
        text: 'shortern'
        on_release: app.process()

"""


class Shortner():

    def check_net(self, long_url):

        UrlRequest(f'https://tinyurl.com/api-create.php?url={long_url}', on_success=self.net_success)
        
    def net_success(self, req, r):
        print(r)
        
inputtext = ""
class Main(App):
    def build(self):
        return Builder.load_string(kv)

    def process(self):
        inputtext = self.root.ids.input.text
        sh = Shortner().check_net(inputtext)
        # print(self.Shortner().shorturl)
        # self.root.ids.text.text = str(shorturl)
# test = Quote()

# test.check_net()

# print(test.quote['text'])
print(inputtext)

if __name__ == "__main__":

    Main().run()

