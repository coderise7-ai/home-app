from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window
# trigger
class HomeApp(App):
    def build(self):
        Window.clearcolor = (0.95, 0.95, 0.95, 1)
        
        main_layout = BoxLayout(orientation='vertical', spacing=10, padding=20)
        
        # Header
        header_label = Label(
            text='Home App',
            size_hint_y=None,
            height=40,
            font_size='20sp',
            bold=True
        )
        main_layout.add_widget(header_label)
        
        # Welcome message
        welcome_label = Label(
            text='Welcome to Your Home App!',
            size_hint_y=None,
            height=60,
            font_size='16sp'
        )
        main_layout.add_widget(welcome_label)
        
        # Simple button
        test_btn = Button(
            text='Click Me!',
            size_hint_y=None,
            height=50,
            background_color=(0.2, 0.6, 0.8, 1),
            on_press=self.button_clicked
        )
        main_layout.add_widget(test_btn)
        
        return main_layout
    
    def button_clicked(self, instance):
        print("Button clicked! App is working!")

if __name__ == '__main__':
    HomeApp().run()
