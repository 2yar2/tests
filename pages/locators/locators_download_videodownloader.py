from selenium.webdriver.common.by import By

class Locators_Videodownloader:

    COOKIES_CLOSE = (By.CLASS_NAME, "icon__ic-cross")

    BUTTONDOWNLOAD = (By.CSS_SELECTOR, ".promo__button-text")

    BUTTONDOWNLOAD2 = (By.CSS_SELECTOR, ".promo__button.promo__button--videodownloader.download-button-js.js-button-download.promo__button--active.promo__button--bottom")

    ANDROIDBUTTONDOWNLOAD2 = (By.CSS_SELECTOR, "a.promo__button.promo__button--videodownloaderandroid.download-button-js.js-button-download.promo__button--active.promo__button--bottom")