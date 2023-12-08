from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from data.amazon import AmazonLocators


class AmazonPage(BasePage):
    def __init__(self, driver, wait):
        self.url = "https://artists.spotify.com/c/roster?offset=0"
        self.locator = AmazonLocators
        super().__init__(driver, wait)
