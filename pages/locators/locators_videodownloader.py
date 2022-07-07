from selenium.webdriver.common.by import By


class Locators_VD:

    COOKIES_CLOSE = (By.CLASS_NAME, "icon__ic-cross")

# Desktop

    BUTTONICON = (By.XPATH, '/html/body/div[1]/div/section[1]/div/div[1]/div[1]/div/a/p')

    BUTTONDOWNLOAD = (By.XPATH, '/html/body/div[1]/div/section[1]/div/div[1]/div[1]/div/a')

    BUTTONDOWNLOAD2 = (By.CSS_SELECTOR, "a.promo__button.promo__button--videodownloader.download-button-js.js-button-download.promo__button--active.promo__button--bottom")

# Android

    ANDROIDBUTTONICON = (By.XPATH, '/html/body/div[1]/div/section[1]/div/div/div[1]/div/a/p')

    ANDROIDBUTTONDOWNLOAD = (By.XPATH, '/html/body/div[1]/div/section[1]/div/div/div[1]/div/a')

    ANDROIDBUTTONDOWNLOAD2 = (By.CSS_SELECTOR, "a.promo__button.promo__button--videodownloaderandroid.download-button-js.js-button-download.promo__button--active.promo__button--bottom")
