from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from data.SpotifyLocators import SpotifyLocators


class Spotify(BasePage):
    def __init__(self, driver, wait):
        self.url = "https://artists.spotify.com/c/roster?offset=0"
        self.locator = SpotifyLocators
        super().__init__(driver, wait)

    def go_to_home_page(self):
        self.go_to_page(self.url)

    def check_title(self, title):
        self.wait.until(EC.title_contains(title))

    def enter_username(self):
        self.input_text(by,locators,value)

    def enter_password(self,by,locators,value):
        self.input_text(by,locators,value)

    def click_on_loginbtn(self,element):
        self.click_element(element)
