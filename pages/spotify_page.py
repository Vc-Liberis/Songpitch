from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from data.SpotifyLocators import SpotifyHomePageLocators


class Spotify(BasePage):
    def __init__(self, driver, wait):
        self.url = "https://artists.spotify.com/"
        self.locator = SpotifyHomePageLocators
        super().__init__(driver, wait)

    def go_to_home_page(self):
        self.go_to_page(self.url)

    def check_title(self, title):
        self.wait.until(EC.title_contains(title))

    def click_on_login(self):
        self.click_Login_button(*self.locator.LOGIN)

    def click_Login_button(self, by, value):
        element = self.wait.until(EC.element_to_be_clickable((by, value)))
        element.click()
