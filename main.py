""" import everything you need here """
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty

import kivy
kivy.require('1.8.0')

""" start of the actual program """

class RootWidget(BoxLayout):
    container = ObjectProperty(None)

class MedicationCheckApp(App):

    #definition to build the app
    def build(self):
        self.root = Builder.load_file('0.kv')

    #definition to switch the pages
    def medsTaken(self, answer):
        filename = answer + '.kv'
        # unload to make an empty page
        Builder.unload_file(filename)
        # clear page
        self.root.clear_widgets()
        # load the content of the .kv file
        answer = Builder.load_file(filename)
        # add the content of the .kv file
        self.root.add_widget(answer)

#run the app
if __name__ == "__main__":
    MedicationCheckApp().run()





