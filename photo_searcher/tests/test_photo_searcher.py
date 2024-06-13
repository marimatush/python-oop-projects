"""
Test photo searcher.
"""

import os
import unittest

from unittest.mock import patch, Mock
import uuid
from photo_searcher.main import MainScreen, NO_IMG_URL

import wikipedia


class MockPage:
    def __init__(self, title, url, images):
        self.title = title
        self.url = url
        self.images = images


class TestPhotoSearcher(unittest.TestCase):
    """Test photo searcher."""

    def test_get_file_extension(self):
        """Testing get file extension."""
        url = "http://example.com/image.jpg"

        self.assertEqual(MainScreen.get_file_extension(self, url), ".jpg")

    @patch("photo_searcher.main.MainScreen.get_wikipedia_page")
    def test_get_image_link(self, mock_wiki_page):
        """Testing get image link."""
        # Setup the mock
        img_url = "http://example.com/image.jpg"
        mock_page = Mock()
        mock_page.images = [img_url]
        mock_wiki_page.return_value = mock_page

        mock_wiki_page.return_value = mock_page
        main_screen = MainScreen()

        result = main_screen.get_image_link("query")

        self.assertEqual(result, img_url)
        mock_wiki_page.assert_called_once_with("query")

    @patch("photo_searcher.main.MainScreen.get_wikipedia_page")
    def test_get_image_link_for_none_page(self, mock_page):
        """Testing get image link for none page."""
        query = "Python"
        mock_page.return_value = None
        main_screen = MainScreen()

        result = main_screen.get_image_link(query)

        self.assertEqual(result, NO_IMG_URL)

    @patch("wikipedia.page")
    def test_get_wikipedia_page(self, mock_wikipedia_page):
        # Setup the mock
        mock_page = Mock()
        mock_page.images = ["http://example.com/image.jpg"]
        mock_wikipedia_page.return_value = mock_page

        screen = MainScreen()

        # Call the method with a sample query
        result = screen.get_wikipedia_page("sample query")

        # Check that the result is the mock page
        self.assertEqual(result, mock_page)
        mock_wikipedia_page.assert_called_once_with(
            "sample query", auto_suggest=False, redirect=True
        )

    @patch("wikipedia.page")
    @patch("random.choice")
    def test_get_wikipedia_page_disambiguation_error(
        self, mock_random_choice, mock_wikipedia_page
    ):
        # Setup the mock for DisambiguationError
        mock_disambiguation_error = wikipedia.DisambiguationError(
            title="Test Disambiguation",
            may_refer_to=["Option1", "Option2", "Option3"],
        )
        mock_wikipedia_page.side_effect = mock_disambiguation_error

        # Mock random.choice to return a specific option
        mock_random_choice.return_value = "Option2"

        # Setup the mock for the second call to wikipedia.page
        mock_page = Mock()
        mock_page.images = ["http://example.com/image.jpg"]
        mock_wikipedia_page.return_value = mock_page

        # Instantiate the MainScreen
        screen = MainScreen()

        # Call the method with a sample query
        with self.assertRaises(wikipedia.DisambiguationError):
            screen.get_wikipedia_page("sample query")

        mock_wikipedia_page.assert_any_call(
            "sample query", auto_suggest=False, redirect=True
        )
        mock_wikipedia_page.assert_any_call(
            "Option2", auto_suggest=False, redirect=True
        )
        mock_random_choice.assert_called_once_with(["Option1", "Option2", "Option3"])

    @patch("photo_searcher.main.IMG_PATH", "test_image_path")
    @patch("requests.get")
    def test_download_image(self, mock_request_get):
        """Testing download image."""
        # Create a temporary file
        temp_image_path = "test_image_path.jpg"

        # Generate mock resposne
        mock_response = Mock()
        mock_response.content = b"test content"
        mock_request_get.return_value = mock_response

        # Set up the url
        url = "http://example.com/image.jpg"

        screen = MainScreen()
        result = screen.download_image(url)
        self.assertEqual(result, temp_image_path)
        self.assertTrue(os.path.exists(temp_image_path))

        # Clean up any created files
        os.remove(temp_image_path)

    def test_delete_image(self):
        """Testing delete image."""
        # Create a temporary file
        image_path = str(uuid.uuid4()) + ".png"
        with open(image_path, "w"):
            pass

        # Initialize the MainScreen
        screen = MainScreen()

        # Delete the image
        screen.delete_image(image_path)

        # Check that the file was deleted
        self.assertFalse(os.path.exists(image_path))


if __name__ == "__main__":
    unittest.main()
