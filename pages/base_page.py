import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import platform


class BasePage:
    if platform.system() == 'Windows':
        os.chdir("..")
    current_directory = os.getcwd()
    print("current dir ",current_directory)
    # Construct the file path using os.path.join
    file_path = os.path.join(current_directory, 'testData', 'SignUpTestData.xlsx')

    # Check if the file exists before trying to open it
    if os.path.exists(file_path):
        pass
    else:
        print(f"File not found: {file_path}")
    df = pd.read_excel(file_path, sheet_name="Sheet1")

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def go_to_page(self, url):
        self.driver.get(url)

    def get_title(self):
        return self.driver.title

    def click_element(self, element, timeout=10):
        try:
            clickable_element = self.wait.until(
                EC.element_to_be_clickable(element)
            )
            clickable_element.click()
            print(f"Clicked on the element successfully.")
        except Exception as e:
            print(f"Failed to click on the element. {str(e)}")

    def click_element_by_value(self, driver, by, value, timeout=10):
        try:
            element = self.wait.until(
                EC.element_to_be_clickable((by, value))
            )
            element.click()
            print("Clicked on the element successfully.")
        except Exception as e:
            print(f"Failed to click on the element. {str(e)}")

    def input_text_by_by(self, driver, by, value, text, timeout=10):
        try:
            textbox = self.wait.until(
                EC.presence_of_element_located((by, value))
            )
            textbox.clear()
            textbox.send_keys(text)
            print(f"Entered '{text}' into the text box successfully.")
        except Exception as e:
            print(f"Failed to enter text into the text box. {str(e)}")

    def enter_text_by_locator(self, locator, text):
        try:
            element = self.wait.until(
                EC.presence_of_element_located(locator)
            )
            element.clear()
            element.send_keys(text)
            print(f"Entered '{text}' into the text box successfully.")
        except Exception as e:
            print(f"Failed to enter text into the text box. {str(e)}")

    def scroll_to_element(driver, element):
        # Scroll until the element is in view
        driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def read_excel(self):
        artist_names = self.df['artistName']
        print(f"Name:::  {artist_names.values}")

    def get_artist_name(self):
        artist_names_list = self.df['artistName'].tolist()
        print(f"Name:::  {artist_names_list[0]}")

    def wait_for_presence_element(self, locator, timeout=30):
        try:
            element = self.wait.until(
                EC.presence_of_element_located(locator)
            )
            return element
        except Exception as e:
            raise TimeoutError(f"Element {locator} not found within {timeout} seconds.") from e

    def wait_for_element_visible(self, element_xpath, timeout=15):
        """
        Wait for an element to be visible using JavaScript Executor.
        """
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((By.XPATH, element_xpath))
            )
            WebDriverWait(self.driver, timeout).until(
                lambda driver: driver.execute_script("return arguments[0].offsetParent !== null;", element)
            )
            return element
        except Exception as e:
            raise TimeoutError(f"Element not visible within {timeout} seconds: {e}")

    def wait_for_element_clickable(self, element_xpath, timeout=10):
        """
        Wait for an element to be clickable using JavaScript Executor.
        """
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((By.XPATH, element_xpath))
            )

            WebDriverWait(self.driver, timeout).until(
                lambda driver: self.driver.execute_script(
                    "return arguments[0].offsetParent !== null && arguments[0].disabled === false;", element
                )
            )

            return element
        except Exception as e:
            raise TimeoutError(f"Element not clickable within {timeout} seconds: {e}")

    def wait_for_visiblity_element(self, locator, timeout=30):
        try:
            element = self.wait.until(
                EC.visibility_of_element_located(locator)
            )
            return element
        except Exception as e:
            raise TimeoutError(f"Element {locator} not found within {timeout} seconds.") from e

    def wait_for_element(self, locator, timeout=30):
        try:
            element = self.wait.until(
                EC.presence_of_element_located(locator) and EC.visibility_of_element_located(locator)
            )
            return element
        except Exception as e:
            raise TimeoutError(f"Element {locator} not found within {timeout} seconds.") from e
