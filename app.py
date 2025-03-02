from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.camera import Camera

class HelloWorldApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
              
        self.camera = Camera(play=True)
        layout.add_widget(self.camera)
        
        return layout
    
    def print_hello(self, instance):
        self.label.text = "Hello, World!"

if __name__ == "__main__":
    HelloWorldApp().run()
