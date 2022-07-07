import time
from pages.locators.locators_download_stogram import Locators_Stogram
from pages.base_page import BasePage
from requests import head


class ButtonDownloadStogram(BasePage):

    def cookie_close(self):
        close = self.browser.find_element(*Locators_Stogram.COOKIES_CLOSE)
        close.click()
        time.sleep(1)

    def button_download(self):
        href = self.browser.find_element(*Locators_Stogram.BUTTONDOWNLOAD).get_attribute("href")
        request = head(href)
        self.check_head_status(request)


class ButtonDownloadStogramScroll(BasePage):

    def cookie_close(self):
        close = self.browser.find_element(*Locators_Stogram.COOKIES_CLOSE)
        close.click()
        time.sleep(1)

    def scroll_page(self):
        self.browser.execute_script("window.scrollBy(0, 1500);")
        time.sleep(2)

    def button_download(self):
        href = self.browser.find_element(*Locators_Stogram.BUTTONDOWNLOADSECOND).get_attribute("href")
        request = head(href)
        self.check_head_status(request)
