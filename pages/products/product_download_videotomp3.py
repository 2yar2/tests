import time
from pages.locators.locators_download_videotomp3 import Locators_Videotomp3
from pages.base_page import BasePage
from requests import head


class ButtonSaveDownload(BasePage):

    def cookies_close(self):
        close = self.browser.find_element(*Locators_Videotomp3.COOKIES_CLOSE)
        close.click()
        time.sleep(2)

    def button_download(self):
        href = self.browser.find_element(*Locators_Videotomp3.BUTTONDOWNLOAD).get_attribute("href")
        request = head(href)
        self.check_head_status(request)


class ButtonSaveDownloadSecond(BasePage):

    def scroll_page(self):
        self.browser.execute_script("window.scrollBy(0, 1500);")
        time.sleep(2)

    def cookies_close(self):
        close = self.browser.find_element(*Locators_Videotomp3.COOKIES_CLOSE)
        close.click()

    def button_download(self):
        href = self.browser.find_element(*Locators_Videotomp3.BUTTONDOWNLOADSECOND).get_attribute("href")
        request = head(href)
        self.check_head_status(request)
