import time
from pages.locators.locators_download_youtubetomp3 import Locators_Youtube_to_mp3
from pages.base_page import BasePage
from requests import head


class DownloadYoutubetomp3(BasePage):

    def cookies_close(self):
        close = self.browser.find_element(*Locators_Youtube_to_mp3.COOKIES_CLOSE)
        close.click()
        time.sleep(1)

    def button_download(self):
        href = self.browser.find_element(*Locators_Youtube_to_mp3.BUTTONDOWNLOAD).get_attribute("href")
        request = head(href)
        self.check_head_status(request)


class DownloadYoutubetomp3Scroll(BasePage):

    def cookies_close(self):
        close = self.browser.find_element(*Locators_Youtube_to_mp3.COOKIES_CLOSE)
        close.click()
        time.sleep(1)

    def scroll_page(self):
        self.browser.execute_script("window.scrollBy(0, 1500);")
        time.sleep(2)

    def button_download(self):
        href = self.browser.find_element(*Locators_Youtube_to_mp3.BUTTONDOWNLOADSECOND).get_attribute("href")
        request = head(href)
        self.check_head_status(request)
