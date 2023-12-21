import os
from pathlib import Path

import yaml
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
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
                result = subprocess.run([r'/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome', '--version'],
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

        if config()['browser'] == 'chrome':
            chrome_options = Options()
            if config()['headless']:
                chrome_options.add_argument('--no-sandbox')
                chrome_options.add_argument("--disable-gpu")
                chrome_options.add_argument("--disable-software-rasterizer")
                chrome_options.add_argument('--window-size=1920,1080')
            self.driver = webdriver.Chrome(options=chrome_options)

        elif config()['browser'] == 'firefox':
            options = webdriver.FirefoxOptions()
            if config()['headless']:
                options.add_argument('--headless')
                options.add_argument('--no-sandbox')
                options.add_argument('--disable-gpu')
                options.add_argument('--window-size=1920,1080')

                # Additional options to mimic human-like behavior and potentially avoid CAPTCHAs
                options.set_preference("general.useragent.override","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
                options.set_preference("privacy.resistFingerprinting", True)
                options.set_preference("privacy.trackingprotection.fingerprinting.enabled", True)
                options.set_preference("privacy.trackingprotection.cryptomining.enabled", True)
                options.set_preference("privacy.trackingprotection.enabled", True)
                options.set_preference("privacy.trackingprotection.socialtracking.enabled", True)
            self.driver = webdriver.Firefox(options=options)

        elif config()['browser'] == 'headless':
            chrome_options = Options()
            if config()['headless']:
                chrome_options.add_argument('--headless')
                chrome_options.add_argument('--no-sandbox')
                chrome_options.add_argument("--disable-gpu")
                chrome_options.add_argument("--disable-extensions")
                chrome_options.add_argument('--disable-dev-shm-usage')
                chrome_options.add_argument('--disable-browser-side-navigation')
                chrome_options.add_argument("--disable-software-rasterizer")
                chrome_options.add_argument('--accept_insecure_certs=true')
                chrome_options.add_argument('--window-size=1920x1080')
            self.driver = webdriver.Chrome(options=chrome_options)

        else:
            raise Exception("Incorrect Browser")

        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 30)
        yield self.wait, self.driver

        if self.driver is not None:
            self.driver.close()
            self.driver.quit()
