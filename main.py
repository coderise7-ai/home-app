from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.uix.spinner import Spinner
from kivy.clock import Clock

class HomeApp(App):
    def build(self):
        # Set window background color
        Window.clearcolor = (0.95, 0.95, 0.95, 1)
        
        # Main layout
        main_layout = BoxLayout(orientation='vertical', spacing=10, padding=20)
        
        # Header
        header_label = Label(
            text='# Home',
            size_hint_y=None,
            height=40,
            markup=True,
            font_size='20sp',
            bold=True
        )
        main_layout.add_widget(header_label)
        
        # Subtitle
        subtitle_label = Label(
            text='Ask anything\n+ Add repositories, files, and spaces',
            size_hint_y=None,
            height=60,
            font_size='14sp'
        )
        main_layout.add_widget(subtitle_label)
        
        # Separator
        separator = Label(
            text='─' * 50,
            size_hint_y=None,
            height=20,
            color=(0.7, 0.7, 0.7, 1)
        )
        main_layout.add_widget(separator)
        
        # Task section
        task_label = Label(
            text='**Task**',
            size_hint_y=None,
            height=30,
            markup=True,
            font_size='16sp',
            bold=True
        )
        main_layout.add_widget(task_label)
        
        # Task buttons
        task_layout = BoxLayout(spacing=10, size_hint_y=None, height=50)
        new_btn = Button(text='[New]', background_color=(0.2, 0.6, 0.8, 1))
        create_issue_btn = Button(text='[Create issue]', background_color=(0.8, 0.2, 0.2, 1))
        task_layout.add_widget(new_btn)
        task_layout.add_widget(create_issue_btn)
        main_layout.add_widget(task_layout)
        
        # Another separator
        separator2 = Label(
            text='─' * 50,
            size_hint_y=None,
            height=20,
            color=(0.7, 0.7, 0.7, 1)
        )
        main_layout.add_widget(separator2)
        
        # Top Repositories section
        top_repo_label = Label(
            text='**Top Repositories**',
            size_hint_y=None,
            height=30,
            markup=True,
            font_size='16sp',
            bold=True
        )
        main_layout.add_widget(top_repo_label)
        
        # Empty repositories message
        empty_repo_label = Label(
            text='No repositories yet',
            size_hint_y=None,
            height=40,
            color=(0.5, 0.5, 0.5, 1),
            italic=True
        )
        main_layout.add_widget(empty_repo_label)
        
        # Another separator
        separator3 = Label(
            text='─' * 50,
            size_hint_y=None,
            height=20,
            color=(0.7, 0.7, 0.7, 1)
        )
        main_layout.add_widget(separator3)
        
        # Create project section
        project_label = Label(
            text='### Create your first project',
            size_hint_y=None,
            height=40,
            markup=True,
            font_size='18sp',
            bold=True
        )
        main_layout.add_widget(project_label)
        
        project_desc = Label(
            text='Ready to start building? Create a repository for a new idea or bring over an existing repository to keep contributing to it.',
            size_hint_y=None,
            height=60,
            text_size=(Window.width - 40, None),
            font_size='12sp'
        )
        main_layout.add_widget(project_desc)
        
        # Project buttons
        project_btn_layout = BoxLayout(spacing=10, size_hint_y=None, height=50)
        create_repo_btn = Button(
            text='• Create repository', 
            background_color=(0.2, 0.7, 0.3, 1),
            on_press=self.create_repository
        )
        import_repo_btn = Button(
            text='• Import repository', 
            background_color=(0.8, 0.5, 0.2, 1),
            on_press=self.import_repository
        )
        project_btn_layout.add_widget(create_repo_btn)
        project_btn_layout.add_widget(import_repo_btn)
        main_layout.add_widget(project_btn_layout)
        
        return main_layout
    
    def create_repository(self, instance):
        print("Create repository clicked!")
        # Add your repository creation logic here
    
    def import_repository(self, instance):
        print("Import repository clicked!")
        # Add your repository import logic here

if __name__ == '__main__':
    HomeApp().run()