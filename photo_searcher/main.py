"""
Managing the main app.
"""

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen


class MainScreen(Screen):
    """Main screen class."""

    def search_images(self):
        """Search images."""
        pass


class RootWidget(ScreenManager):
    """Root widget class."""

    pass


class MainApp(App):
    """Main app class."""

    def build(self):
        """Build the app."""
        return RootWidget()


MainApp().run()
