from selenium.webdriver.common.by import By


class SpotifyHomePageLocators:
    EMAIL_USERNAME = (By.CSS_SELECTOR, "#login-username")
    PASSWORD = (By.CSS_SELECTOR, "#login-password")
    LOGIN = (By.CSS_SELECTOR, "#login-button")
    SEARCH_BYARTIST = (By.CSS_SELECTOR, "[placeholder=\"Search roster\"]")
    ROASTER_ARTIST_TABLE = (By.XPATH, "//table/tbody/tr//td//button/span")
    ROASTER_ARTIST_BUTTON = (By.CSS_SELECTOR, "button[data-encore-id='popoverNavigationLink']")
    SONG_TOPITCH = (By.XPATH, "//h2[normalize-space()='Choose a song to pitch']/..//div[@role='radio']//*[@role='img']")
    NEXT_BUTTON = (By.XPATH, "//button[@data-slo-id='pitch-next-btn']")
    CLEAR_BUTTON = (By.XPATH, "//button[@data-testid='clear-button']")
    HOMETOWN_FORARTISTS = (By.CSS_SELECTOR, "div#entity-search input")
    LOCATION_SUGGESTION = (By.CSS_SELECTOR, "li[role='option']")
    ADD_SONG = (By.XPATH, "//h2[normalize-space()='Add song details']")
    CHOOSE_GENRE_TEXT = (By.XPATH, "//span[@id='genres-label']")
    CHOOSE_GENRE_DROPDOWN = (By.CSS_SELECTOR, "input#genre-select")
    GENRE_SUGGESTION = (By.CSS_SELECTOR, "div[id*='react-select-2-option']")
    TYPE_MUSICCULTURE = (By.XPATH, "//span[normalize-space()='Choose up to 2 music cultures.']/../../div/button")
    TYPE_MOOD = (By.XPATH, "//span[normalize-space()='Choose up to 2 moods.']/../../div/button")
    TYPE_SONGSTYLE = (By.XPATH, "//span[normalize-space()='Choose up to 2 song styles.']/../../div/button")
    TYPE_OFINSTRUMENTS = (By.XPATH, "//span[normalize-space()='What instruments are on this song?']/../../div/button")
    IS_THIS_COVER = (By.CSS_SELECTOR,
        "fieldset[data-encore-id=\"formGroup\"] div[data-encore-id=\"formRadio\"] label[for^=\"is-cover\"]")
    IS_IT_REMIX = (By.CSS_SELECTOR,
        "fieldset[data-encore-id='formGroup'] div[data-encore-id='formRadio'] label[for^='is-remix']")
    HOW_WAS_IT_RECORDED = (By.CSS_SELECTOR,
        "fieldset[data-encore-id='formGroup'] div[data-encore-id='formRadio'] label[for^='recording-type']")
    IS_IT_INSTRUMENTAL = (By.CSS_SELECTOR,
        "fieldset[data-encore-id='formGroup'] div[data-encore-id='formRadio'] label[for^='is-instrumental']")
    CHOOSE_LANGUAGES = (By.CSS_SELECTOR, "div#entity-search input")
    LANGUAGES_LYRICS = (By.XPATH, "//span[normalize-space()='What languages are the lyrics in?']")
    DESCRIPTION = (By.CSS_SELECTOR, "textarea#song-info")
    ARTIST_INFO = (By.CSS_SELECTOR, "button[aria-label=\"Toggle seeing artist info\"]")
