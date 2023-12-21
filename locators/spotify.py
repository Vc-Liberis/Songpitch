from selenium.webdriver.common.by import By


class SpotifyHomePageLocators:
    emailUsername = (By.CSS_SELECTOR, "#login-username")
    password = (By.CSS_SELECTOR, "#login-password")
    loginBtn = (By.CSS_SELECTOR, "#login-button")
    searchByArtist = (By.CSS_SELECTOR, "[placeholder=\"Search roster\"]")
    rosterHeader = (By.XPATH, "//h1[contains(text(), 'Your roster')]")
    roasterArtistSpan = (By.XPATH, "//table/tbody/tr//td//button//following::span[1]")
    selectTimePeriodDrpDwn = (By.XPATH, "//div[@data-testid='dropdown-select-time-period']//div[contains(text(), 'Last 24 hours')]")
    roasterArtistTable = (By.XPATH, "//table/tbody/tr//td//button/span")
    spotifyLoaderSVG = (By.XPATH, "//*[local-name()='svg' and @role='progressbar']")
    firstArtistStarImg = (By.XPATH, "(//*[local-name()='svg' and @data-testid='starred'])[1]")
    roasterArtistTableHeader = (By.XPATH, "//table//tr/th[contains(text(), 'Change')]")
    roasterArtistStreamBtn = (By.XPATH, "//div[contains(text(), 'Streams')]//parent::button")
    roasterArtistBtn = (By.CSS_SELECTOR, "button[locators-encore-id='popoverNavigationLink']")
    songToPitch = (By.XPATH, "//h2[normalize-space()='Choose a song to pitch']/..//div[@role='radio']//*[@role='img']")
    nextBtn = (By.XPATH, "//button[@locators-slo-id='pitch-next-btn']")
    clearBtn = (By.XPATH, "//button[@locators-testid='clear-button']")
    hometownForArtists = (By.CSS_SELECTOR, "div#entity-search input")
    locationSuggestions = (By.CSS_SELECTOR, "li[role='option']")
    addSong = (By.XPATH, "//h2[normalize-space()='Add song details']")
    chooseGenreText = (By.XPATH, "//span[@id='genres-label']")
    chooseGenreDrpDwn = (By.CSS_SELECTOR, "input#genre-select")
    genreSuggestion = (By.CSS_SELECTOR, "div[id*='react-select-2-option']")
    typeMusicCulture = (By.XPATH, "//span[normalize-space()='Choose up to 2 music cultures.']/../../div/button")
    typeMood = (By.XPATH, "//span[normalize-space()='Choose up to 2 moods.']/../../div/button")
    typeSongsStyle = (By.XPATH, "//span[normalize-space()='Choose up to 2 song styles.']/../../div/button")
    typeOfInstruments = (By.XPATH, "//span[normalize-space()='What instruments are on this song?']/../../div/button")
    isThisCover = (By.CSS_SELECTOR,
        "fieldset[locators-encore-id=\"formGroup\"] div[locators-encore-id=\"formRadio\"] label[for^=\"is-cover\"]")
    isItRemix = (By.CSS_SELECTOR,
        "fieldset[locators-encore-id='formGroup'] div[locators-encore-id='formRadio'] label[for^='is-remix']")
    howWasItRecorded = (By.CSS_SELECTOR,
        "fieldset[locators-encore-id='formGroup'] div[locators-encore-id='formRadio'] label[for^='recording-type']")
    isItInstrumental = (By.CSS_SELECTOR,
        "fieldset[locators-encore-id='formGroup'] div[locators-encore-id='formRadio'] label[for^='is-instrumental']")
    chooseLanguages = (By.CSS_SELECTOR, "div#entity-search input")
    languagesLyrics = (By.XPATH, "//span[normalize-space()='What languages are the lyrics in?']")
    description = (By.CSS_SELECTOR, "textarea#song-info")
    artistInfo = (By.CSS_SELECTOR, "button[aria-label=\"Toggle seeing artist info\"]")
    pitchASongLinkBtn = (By.XPATH, "//span[contains(text(), 'Pitch a song')]//parent::a")
