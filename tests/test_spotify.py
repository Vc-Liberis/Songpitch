# coding=utf-8
import pytest
from selenium.webdriver.common.by import By

from pages.spotify_page import Spotify
from tests.test_base import BaseTest
from data.spotify import SpotifyHomePageLocators


class TestSpotify(BaseTest):

    @pytest.fixture
    def load_pages(self):
        self.page = Spotify(self.driver, self.wait)
        self.page.go_to_home_page()

    def test_title(self, load_pages):
        # self.page.check_title("Spotify")
        self.page.click_on_login()


    # def login_spotify(self, load_pages):
