# tests/TestArtistScrapper.py
import pytest
from pages.spotify_page import Spotify
from tests.test_base import BaseTest
# from api import HeaderSetup
# from api.SpotifyApi import SpotifyApi


class TestArtistScrapper(BaseTest):
    # header_setup = HeaderSetup


    @pytest.fixture
    def setup_spotifyscrapper(self):
        self.page = Spotify(self.driver, self.wait)
        self.page.go_to_home_page()
        self.page.enter_username("pitching@weareinstrumental.com")
        self.page.enter_password("Shifting#Supremacy#Symphony5")
        self.page.click_on_login()
        self.page.wait_for_dashboard()

    # def test_apple_scrapper(self, setup_spotifyscrapper):
    #     spotify_api_instance = SpotifyApi(self.driver, self.wait, self.header_setup)
    #     artist = spotify_api_instance.get_artist_details()
    #     spotify_api_instance.fetch_data_from_json(artist.json())
