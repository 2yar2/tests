import time
from pages.locators.locators_stogram import Locators_Stogram
from pages.base_page import BasePage
from requests import head


class ButtonDownloadStogram(BasePage):

    def cookie_close(self):
        close = self.browser.find_element(*Locators_Stogram.COOKIES_CLOSE)
        close.click()
        time.sleep(1)

    def scroll_page(self):
        self.browser.execute_script("window.scrollBy(0, 1500);")
        time.sleep(2)

    def check_button_download_top(self):
        btn = self.browser.find_element(*Locators_Stogram.BUTTONDOWNLOAD)
        href = btn.get_attribute("href")
        assert "4kdownload.com/thanks-for-downloading?source=stogram" in href
        request = head(href)
        self.check_head_status(request)
        btn.click()
        time.sleep(2)


    def check_button_download_bot(self):
        btn = self.browser.find_element(*Locators_Stogram.BUTTONDOWNLOAD2)
        href = btn.get_attribute("href")
        assert "4kdownload.com/thanks-for-downloading?source=stogram" in href
        request = head(btn.get_attribute("href"))
        self.check_head_status(request)
        btn.click()
        time.sleep(2)
