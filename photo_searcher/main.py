"""
Managing the main app.
"""

import os
import random
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

import requests
import wikipedia

Builder.load_file("frontend.kv")


NO_IMG_URL = (
    "https://upload.wikimedia.org/wikipedia/commons/thumb/a/ac/"
    "No_image_available.svg/1024px-No_image_available.svg.png"
)


class MainScreen(Screen):
    """Main screen class."""

    def get_image_link(self, query: str):
        """Get image link."""
        # Get wikipedia page and list of images urls
        page = None
        page = self.get_wikipedia_page(query)

        # Get the image url
        if page is not None and len(page.images) > 0:
            img_url = page.images[0]
        else:
            img_url = NO_IMG_URL

        return img_url

    def get_file_extension(self, url: str):
        """Get file extension."""
        # Extract the file name from the URL
        file_name = os.path.basename(url)

        # Split the file name into name and extension
        _, file_extension = os.path.splitext(file_name)
        return file_extension

    def get_wikipedia_page(self, query: str):
        """Get wikipedia page."""
        try:
            page = wikipedia.page(query, auto_suggest=False, redirect=True)
        except wikipedia.DisambiguationError as e:
            rand_choice = random.choice(e.options)
            try:
                page = wikipedia.page(rand_choice, auto_suggest=False, redirect=True)
            except wikipedia.PageError:
                print("Page not found.")
                return None
        except wikipedia.PageError:
            print("Page not found.")
            return None
        return page

    def download_image(self, url: str):
        """Download the image."""
        image_path: str = "files/response_img" + self.get_file_extension(url)
        headers = {"User-Agent": "My User Agent 1.0"}
        response = requests.get(url, headers=headers)
        with open(image_path, "wb") as file:
            file.write(response.content)
        return image_path

    def delete_image(self, path: str):
        """Delete the image."""
        os.remove(path)

    def search_image(self):
        """Search images."""
        # Get user query from text input
        query = self.manager.current_screen.ids.user_query.text.strip()

        # Get image link
        img_url = self.get_image_link(query)

        # Download image
        img_path = self.download_image(img_url)

        self.manager.current_screen.ids.img.source = img_path
        self.manager.current_screen.ids.img.reload()

        # Delete image
        self.delete_image(img_path)


class RootWidget(ScreenManager):
    """Root widget class."""

    pass


class MainApp(App):
    """Main app class."""

    def build(self):
        """Build the app."""
        return RootWidget()


MainApp().run()
