from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from data.spotify import SpotifyHomePageLocators


class Spotify(BasePage):
    def __init__(self, driver, wait):
        self.url = "https://artists.spotify.com/c/roster?offset=0"
        self.locator = SpotifyHomePageLocators
        super().__init__(driver, wait)

    def go_to_home_page(self):
        self.go_to_page(self.url)

    def check_title(self, title):
        self.wait.until(EC.title_contains(title))

    def enter_username(self,username):
        #self.scroll_to_element(self.locator.EMAIL_USERNAME)
        self.enter_text_by_locator(self.locator.EMAIL_USERNAME,username)

    def enter_password(self,password):
        #self.scroll_to_element(self.locator.PASSWORD)
        self.enter_text_by_locator(self.locator.PASSWORD,password)

    def click_on_login(self):
        self.click_Login_button(*self.locator.LOGIN)

    def click_Login_button(self, by, value):
        element = self.wait.until(EC.element_to_be_clickable((by, value)))
        element.click()
