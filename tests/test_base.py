import os
from pathlib import Path

import yaml
from selenium import webdriver
from selenium.webdriver.chrome import service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.service import Service
import warnings
import pytest
import subprocess
import platform
from seleniumwire import webdriver

os.environ['WDM_LOG_LEVEL'] = '1'
os.environ["WDM_LOCAL"] = "1"


def config():
    path = Path(__file__).parent / "../locators/config.yaml"
    try:
        with open(path) as config_file:
            data = yaml.load(config_file, Loader=yaml.FullLoader)
        return data
    finally:
        config_file.close()


class BaseTest:
    def get_chrome_version(self):
        try:
            if platform.system() == 'Windows':
                # For Windows
                result = subprocess.run(['reg', 'query', 'HKEY_CURRENT_USER\\Software\\Google\\Chrome\\BLBeacon'],
                                        capture_output=True, text=True)
                version_line = next(line for line in result.stdout.split('\n') if 'version' in line)
                version = version_line.split()[2]
            elif platform.system() == 'Darwin':
                # For macOS
                result = subprocess.run(['/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome', '--version'],
                                        capture_output=True, text=True, shell=True)
                version = result.stdout.strip().split()[-1]
            elif platform.system() == 'Linux':
                # For Linux
                result = subprocess.run(['google-chrome', '--version'], capture_output=True, text=True)
                version = result.stdout.strip().split()[-1]
            else:
                raise NotImplementedError(f"Unsupported operating system: {platform.system()}")

            return version
        except Exception as e:
            print(f"Error: {e}")
            return None

    def get_chrome_binary_directory(self):
        try:
            if platform.system() == 'Windows':
                # For Windows
                result = subprocess.run(['where', 'chrome'], capture_output=True, text=True)
                directory = result.stdout.strip().split('\n')[0]
            elif platform.system() == 'Darwin':
                # For macOS
                directory = '/Applications/Google Chrome.app/Contents/MacOS/'
            elif platform.system() == 'Linux':
                # For Linux
                result = subprocess.run(['which', 'google-chrome'], capture_output=True, text=True)
                directory = result.stdout.strip()
            else:
                raise NotImplementedError(f"Unsupported operating system: {platform.system()}")

            return directory
        except Exception as e:
            print(f"Error: {e}")
            return None

    @pytest.fixture(autouse=True)
    def init_driver(self):
        print("Init driver")
        chrome_version = self.get_chrome_version()
        if chrome_version:
            print(f"Google Chrome Version: {chrome_version}")

        # Check Chrome binary directory
        chrome_directory = self.get_chrome_binary_directory()
        if chrome_directory:
            print(f"Google Chrome Binary Directory: {chrome_directory}")
        print(os.path.join(os.getcwd(), 'driver', 'chromedriver'))
        warnings.simplefilter("ignore", ResourceWarning)
        # Set a valid timeout for the "connect" attribut

        if config()['browser'] == 'chrome':
            self.driver = webdriver.Chrome()  # Set implicit wait time
        elif config()['browser'] == 'firefox':
            options = webdriver.FirefoxOptions()
            if config()['headless']:
                options.add_argument('--headless')
                options.add_argument('--no-sandbox')
                options.add_argument('--disable-gpu')
                options.add_argument('--window-size=1920,1080')
            self.driver = webdriver.Firefox(options=options)
        elif config()['browser'] == 'headless':
            chromedriver_path = os.path.join(os.getcwd(), 'driver', 'chromedriver')
            service = Service(executable_path=chromedriver_path)
            options = webdriver.ChromeOptions()
            if config()['headless']:
                options.add_argument('--headless')
                options.add_argument('--no-sandbox')
                options.add_argument('--disable-gpu')
                options.add_argument('--window-size=1920,1080')
                options.binary_location = '/usr/bin/google-chrome'
            self.driver = webdriver.Chrome(
                service=service,
                options=options
              )
        else:
            raise Exception("Incorrect Browser")

        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 30)
        yield self.wait, self.driver

        if self.driver is not None:
            self.driver.close()
            self.driver.quit()
