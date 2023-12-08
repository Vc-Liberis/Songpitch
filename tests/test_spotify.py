# coding=utf-8
import pytest
from pages.spotify_page import Spotify
from tests.test_base import BaseTest


class TestSpotify(BaseTest):
    @pytest.fixture
    def setup_spotify(self):
        self.page = Spotify(self.driver, self.wait)

    def test_spotify_login(self, setup_spotify):
        # Your test code here
        self.page.go_to_home_page()
        self.page.enter_username("pitching@weareinstrumental.com")
        self.page.enter_password("Shifting#Supremacy#Symphony5")
        self.page.click_on_login()
        self.page.input_artist_name("Sarah Tassew")
        self.page.click_on_pitchsong_btn()
        self.page.click_on_next_btn()
        self.page.select_hometown_for_artist()


