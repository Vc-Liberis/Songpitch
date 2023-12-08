# coding=utf-8
import pytest
from pages.spotify_page import Spotify
from tests.test_base import BaseTest

class TestArtistScrapper(BaseTest):

    @pytest.fixture
    def setup_spotifyscrapper(self):
        self.page = Spotify(self.driver, self.wait)
        self.page.go_to_home_page()
        # self.page.check_title("Login - Spotify")
        self.page.enter_username("pitching@weareinstrumental.com")
        self.page.enter_password("Accuracy#Hardiness2#Tameness")
        self.page.click_on_login()


    def test_spotifyscrapper(self, setup_spotifyscrapper):
        # Your test code here
        pass
