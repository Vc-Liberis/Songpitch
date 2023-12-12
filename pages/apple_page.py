from pages.base_page import BasePage
from locators.apple import AppleLocators


class ApplePage(BasePage):
    def __init__(self, driver, wait):
        self.url = "https://artists.spotify.com/c/roster?offset=0"
        self.locator = AppleLocators
        super().__init__(driver, wait)
