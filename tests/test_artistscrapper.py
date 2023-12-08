# coding=utf-8
import gzip
import json
from io import BytesIO
from time import sleep, time
import pytest
import requests
from pages.spotify_page import Spotify
from tests.test_base import BaseTest


class TestArtistScrapper(BaseTest):

    def setup_roster_header(self):
        return {
            'Authorization': self.getBearerToken(),
            'Host':'roster-view-service.spotify.com',
            'Accept':'application/json'
        }

    def setup_upcoming_release_header(self):
        return {
            'Authorization': self.getBearerToken(),
            'Accept':'application/json',
            'Content-Type':'application/json',
            'Accept-Encoding': 'gzip,deflate,br',
            'Accept-Language': 'en-US',
            'Host': 'generic.wg.spotify.com',
            'Origin':'https://artists.spotify.com',
            'Referer':'https://artists.spotify.com',
            'Connection':'keep-alive',
            'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.3 Safari/605.1.15',
            'spotify-app-version':'1.0.0.41a8451',
            'app-platform':'Browser',
            'Priority':'u=3, i'
        }

    @pytest.fixture
    def setup_spotifyscrapper(self):
        self.page = Spotify(self.driver, self.wait)
        self.page.go_to_home_page()
        self.page.check_title("Login - Spotify")
        self.page.enter_username("pitching@weareinstrumental.com")
        self.page.enter_password("Shifting#Supremacy#Symphony5")
        self.page.click_on_login()
        self.page.wait_for_dashboard()

    def getBearerToken(self):
        for request in self.driver.requests:
            if request.url.lower() == 'https://roster-view-service.spotify.com/v1/settings':
                access_token = request.headers.get('Authorization')
                print(f"Bearer Token: {access_token}")
                return access_token

    def getArtistDetails(self):
        response = requests.get('https://api.spotify.com/v2/roster', headers=self.setup_roster_header())
        return response

    def fetch_data_from_json(self,data):
        artists = data.get('artists')
        for artist in artists:
            artist_id = artist.get('id')
            artist_name = artist.get('name')
            image_url = artist.get('image_url')
            upcoming_data = self.getUpcomingReleaseDetails(artist_id)
            print(upcoming_data.json())
            print(f"Artist ID: {artist_id}")
            print(f"Artist Name: {artist_name}")
            print(f"Image URL: {image_url}")
            print(f"release details : {upcoming_data.json()['upcoming_releases']}")
            print("-" * 30)

    def getUpcomingReleaseDetails(self,artist_id):
        response = requests.get(f'https://generic.wg.spotify.com/upcoming-view-service/v1/artist/{artist_id}/catalog', headers=self.setup_upcoming_release_header())
        return response

    def test_spotifyscrapper(self, setup_spotifyscrapper):
        artist = self.getArtistDetails()
        self.fetch_data_from_json(artist.json())
        pass
