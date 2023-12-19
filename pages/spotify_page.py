import time

from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators.spotify import SpotifyHomePageLocators


class Spotify(BasePage):
    def __init__(self, driver, wait):
        self.url = "https://artists.spotify.com/c/roster?offset=0"
        self.locator = SpotifyHomePageLocators
        super().__init__(driver, wait)

    def go_to_home_page(self):
        self.go_to_page(self.url)

    def check_title(self, title):
        self.wait.until(EC.title_contains(title))
        
    def enter_username(self, username):
        self.enter_text_by_locator(self.locator.emailUsername, username)

    def enter_password(self, password):
        self.enter_text_by_locator(self.locator.password, password)

    def click_on_login(self):
        self.click_element(self.locator.loginBtn)

    def click_button(self, by, value):
        element = self.wait.until(EC.element_to_be_clickable((by, value)))
        element.click()

    def input_artist_name(self, value):
        self.enter_text_by_locator(self.locator.searchByArtist, value)

    def click_on_pitchsong_btn(self):
        self.click_button(*self.locator.pitchASongLinkBtn)

    def click_on_next_btn(self):
        self.click_button(*self.locator.nextBtn)

    def select_hometown_for_artist(self):
        self.click_button(*self.locator.hometownForArtists)
        self.enter_text_by_locator(self.locator.hometownForArtists, "London, England, United Kingdom")

    def wait_for_dashboard(self):
        time.sleep(150)
        # self.wait_for_element_to_disappear(self.locator.spotifyLoaderSVG)
        # time.sleep(5)
        # self.wait_for_element_to_disappear(self.locator.spotifyLoaderSVG)
        # self.wait_for_presence_element(self.locator.roasterArtistTable)
