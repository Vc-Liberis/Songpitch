from selenium.webdriver.common.by import By


class AmazonLocators:
    GET_STARTED = By.ID('LandingScreen_GetStarted')
    CAPTCHA = By.XPATH("//img[contains(@src,'Captcha')]")
    EMAILID = By.ID('ap_email')
    PASSWORD = By.ID('ap_password')
    SUBMIT = By.ID('signInSubmit')
    SIGNOUT = By.ID('RootNavigation_SignOut')
    SEARCHBAR = By.ID('SelectArtistScreen_SearchBar')
