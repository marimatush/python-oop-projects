"""
Managing the main app.
"""

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

Builder.load_file("frontend.kv")


class MainScreen(Screen):
    """Main screen class."""

    def search_image(self):
        """Search images."""
        self.manager.current_screen.ids.img.source = "files/banana_bread.jpeg"


class RootWidget(ScreenManager):
    """Root widget class."""

    pass


class MainApp(App):
    """Main app class."""

    def build(self):
        """Build the app."""
        return RootWidget()


MainApp().run()