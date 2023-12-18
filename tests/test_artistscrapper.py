# coding=utf-8
import logging

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
        self.page.enter_username("pitching@weareinstrumental.com")
        self.page.enter_password("Shifting#Supremacy#Symphony6")
        self.page.click_on_login()
        self.page.wait_for_dashboard()
        # self.setup_roster_header()

    def save_bearer_token_for_spotify(self):
        # Extract network data using JavaScriptExecutor
        js_executor = self.driver.execute_script

        # Execute JavaScript code to retrieve performance logs
        logs = js_executor("return window.performance.getEntries()")

        # Convert logs to string (you can use a JSON library for more structured handling)
        logs_string = str(logs)

        # Print the raw network logs
        print("Network Logs: " + logs_string)

        # Parse the logs and extract headers for a specific network request (customize this based on your needs)
        # In this example, we are printing headers for the first network request
        headers = js_executor(
            "return JSON.parse(arguments[0])[0].response.headers",
            logs_string
        )
        print(logs_string)

    def getBearerToken(self):
        logging.basicConfig(level=logging.INFO)
        print("get bearer token")
        try:
            for request in self.driver.requests:
                if request.url.lower() == 'https://roster-view-service.spotify.com/v1/settings':
                    print("URL found::: https://roster-view-service.spotify.com/v1/settings")
                    access_token = request.headers.get('Authorization')
                    if access_token is None:
                        raise ValueError("Authorization header not found in the request.")
                    print(f"Bearer Token: {access_token}")
                    return access_token
            raise RuntimeError("No request found for the specified URL.")
        except Exception as e:
            print(f"Error while getting Bearer Token: {str(e)}")
            return None

    def getArtistDetails(self):
        global response
        try:
            response = requests.get('https://api.spotify.com/v2/roster', headers=self.setup_roster_header())
            response.raise_for_status()  # Raises HTTPError for bad responses
            # If the response is successful (status code 2xx), return it
            return response
        except requests.HTTPError as http_ex:
            # Handle HTTP errors (e.g., 4xx or 5xx status codes)
            print(f"HTTP Error: {http_ex}")
            print(f"Response content: {response.content}")
        except requests.RequestException as req_ex:
            # Handle general request exception (e.g., connection errors)
            print(f"Request Exception: {req_ex}")
        except Exception as ex:
            # Handle other unexpected exceptions
            print(f"Unexpected Exception: {ex}")
        return None  # Return None to indicate an error

    def fetch_data_from_json(self, data):
        artists = data.get('artists')
        for artist in artists:
            artist_id, artist_name, image_url = artist.get('id'), artist.get('name'), artist.get('image_url')
            try:
                upcoming_data = self.getUpcomingReleaseDetails(artist_id)
                upcoming_releases = upcoming_data.json().get('upcoming_releases', [])
                print(f"Artist ID: {artist_id}")
                print(f"Artist Name: {artist_name}")
                print(f"Image URL: {image_url}")
                print(f"Release Details: {upcoming_releases}")
                print("-" * 30)
            except Exception as ex:
                print(f"Error processing artist with ID {artist_id}: {ex}")

    def getUpcomingReleaseDetails(self, artist_id):
        try:
            response = requests.get(
                f'https://generic.wg.spotify.com/upcoming-view-service/v1/artist/{artist_id}/catalog',
                headers=self.setup_upcoming_release_header()
            )
            response.raise_for_status()  # Raises HTTPError for bad responses

            # If the response is successful (status code 2xx), return it
            return response
        except requests.RequestException as req_ex:
            # Handle general request exception (e.g., connection errors)
            print(f"Request Exception: {req_ex}")
        except requests.HTTPError as http_ex:
            # Handle HTTP errors (e.g., 4xx or 5xx status codes)
            print(f"HTTP Error: {http_ex}")
            print(f"Response content: {response.content}")
        except Exception as ex:
            # Handle other unexpected exceptions
            print(f"Unexpected Exception: {ex}")
        return None  # Return None to indicate an error

    def test_spotifyscrapper(self, setup_spotifyscrapper):
        global artist
        try:
            artist = self.getArtistDetails()
            if artist is None:
                print("Unable to get artist details")
        except:
            print("")
        self.fetch_data_from_json(artist.json())
        pass
