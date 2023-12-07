# coding=utf-8
import pytest
from pages.spotify_page import Spotify
from tests.base_test import BaseTest


class TestSearch(BaseTest):

    @pytest.fixture
    def load_pages(self):
        self.page = Spotify(self.driver, self.wait)
        self.page.go_to_home_page()
        self.page.check_title("Login - Spotify")
        self.page.enter_username()
