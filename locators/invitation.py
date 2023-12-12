from selenium.webdriver.common.by import By

class InvitationLocators:
    SEARCH_LABEL = By.XPATH('//div[@id="entity-search"]//input')
    ROLE = By.XPATH('//select')
    COMPANY = By.ID('company')
    SUBMIT = By.XPATH('//span[text()=\'Submit\']')