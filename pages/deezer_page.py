from pages.base_page import BasePage
from locators.deezer import DeezerLocators


class DeezerPage(BasePage):
    def __init__(self, driver, wait):
        self.url = "https://artists.spotify.com/c/roster?offset=0"
        self.locator = DeezerLocators
        super().__init__(driver, wait)
