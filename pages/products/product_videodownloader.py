import time
from pages.locators.locators_videodownloader import Locators_VD
from pages.base_page import BasePage


class ButtonSaveVD(BasePage):

    def cookies_close(self):
        close = self.browser.find_element(*Locators_VD.COOKIES_CLOSE)
        close.click()
        time.sleep(2)

    def button_icon(self):
        self.browser.find_element(*Locators_VD.BUTTONICON)

    def button_download(self):
        href = self.browser.find_element(*Locators_VD.BUTTONDOWNLOAD).get_attribute("href")
        assert "4kdownload.com/thanks-for-downloading?source=videodownloader" in href

    def button_save(self):
        self.browser.find_element(*Locators_VD.BUTTONDOWNLOAD).click()
        time.sleep(2)

class AndroidButtonSaveVD(BasePage):

    def cookies_close(self):
        close = self.browser.find_element(*Locators_VD.COOKIES_CLOSE)
        close.click()
        time.sleep(2)

    def android_button_icon(self):
        self.browser.find_element(*Locators_VD.ANDROIDBUTTONICON)

    def android_button_download(self):
        href = self.browser.find_element(*Locators_VD.ANDROIDBUTTONDOWNLOAD).get_attribute("href")
        assert "4kdownload.com/thanks-for-downloading?source=videodownloaderandroid" in href


class ScrollPage(BasePage):

    def scroll_page(self):
        self.browser.execute_script("window.scrollBy(0, 1500);")
        time.sleep(2)

    def cookies_close(self):
        close = self.browser.find_element(*Locators_VD.COOKIES_CLOSE)
        close.click()

    def button_download2(self):
        self.browser.find_element(*Locators_VD.BUTTONDOWNLOAD2).click()
        time.sleep(1)

    def android_button_save(self):
        self.browser.find_element(*Locators_VD.ANDROIDBUTTONDOWNLOAD2).click()
        time.sleep(1)
