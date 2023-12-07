from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class BasePage:

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def go_to_page(self, url):
        self.driver.get(url)

    def get_title(self):
        return self.driver.title

    def click_element(self,element, timeout=10):
        """
        Clicks the given WebElement.

        Parameters:
        - element: WebElement instance
        - timeout: Maximum time to wait for the element to be clickable (default is 10 seconds)
        """
        try:
            clickable_element = WebDriverWait(element._parent, timeout).until(
                EC.element_to_be_clickable(element)
            )
            clickable_element.click()
            print("Clicked on the element successfully.")
        except Exception as e:
            print(f"Failed to click on the element. {str(e)}")

    def click_element(self,driver, by, value, timeout=10):
        """
        Clicks an element identified by the given locator strategy (by) and value.

        Parameters:
        - driver: WebDriver instance
        - by: The locator strategy (e.g., By.ID, By.XPATH, etc.)
        - value: The value of the locator
        - timeout: Maximum time to wait for the element to be clickable (default is 10 seconds)
        """
        try:
            element = WebDriverWait(driver, timeout).until(
                EC.element_to_be_clickable((by, value))
            )
            element.click()
            print("Clicked on the element successfully.")
        except Exception as e:
            print(f"Failed to click on the element. {str(e)}")

    def input_text(self,driver, by, value, text, timeout=10):
        """
        Enters the given text into a text box identified by the given locator strategy (by) and value.

        Parameters:
        - driver: WebDriver instance
        - by: The locator strategy (e.g., By.ID, By.XPATH, etc.)
        - value: The value of the locator
        - text: The text to be entered into the text box
        - timeout: Maximum time to wait for the text box to be present (default is 10 seconds)
        """
        try:
            textbox = WebDriverWait(driver, timeout).until(
                EC.presence_of_element_located((by, value))
            )
            textbox.clear()  # Clear any existing text in the text box
            textbox.send_keys(text)
            print(f"Entered '{text}' into the text box successfully.")
        except Exception as e:
            print(f"Failed to enter text into the text box. {str(e)}")



