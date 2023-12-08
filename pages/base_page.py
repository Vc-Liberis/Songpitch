import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    excel_file_path = "C:\\Users\\SurajDengale\\IdeaProjects\\vinayLatest\\Songpitch\\testData\\SignUpTestData.xlsx"
    df = pd.read_excel(excel_file_path, sheet_name="Sheet1")

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def go_to_page(self, url):
        self.driver.get(url)

    def get_title(self):
        return self.driver.title

    def click_element(self, element, timeout=10):
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

    def click_element_by_value(self, driver, by, value, timeout=10):
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

    def input_text_by_by(self, driver, by, value, text, timeout=10):
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

    def enter_text_by_locator(self, locator, text):
        """
        Enters the given text into a text box identified by the provided locator.

        Parameters:
        - driver: WebDriver instance
        - locator: Tuple (By, value) representing the locator strategy and value (e.g., (By.ID, "your_element_id"))
        - text: The text to be entered into the text box
        """
        try:
            element = self.wait.until(
                EC.presence_of_element_located(locator)
            )
            element.clear()  # Clear any existing text in the text box
            element.send_keys(text)
            print(f"Entered '{text}' into the text box successfully.")
        except Exception as e:
            print(f"Failed to enter text into the text box. {str(e)}")

    def scroll_to_element(driver, element):
        # Scroll until the element is in view
        driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def read_excel(self):
        # print(f"Column:: {df.columns.ravel()}" )
        # Fetch the 'artistName' column
        artist_names = self.df['artistName']
        print(f"Name:::  {artist_names.values}")

    def get_artist_name(self):
        artist_names_list = self.df['artistName'].tolist()
        print(f"Name:::  {artist_names_list[0]}")
