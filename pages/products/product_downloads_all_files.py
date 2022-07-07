from pages.locators.locators_downloads_all_files import Locators4KVideoDownloader
from pages.locators.locators_downloads_all_files import Locators4KYouTubetoMP3
from pages.locators.locators_downloads_all_files import Locators4KStogram
from pages.locators.locators_downloads_all_files import Locators4KSlideshowMaker
from pages.locators.locators_downloads_all_files import Locators4KVideotoMP3
from pages.locators.locators_downloads_all_files import Locators4ktokkit
from pages.base_page import BasePage
import time
from requests import head

class VideoDownloader(BasePage):

    def cookie_close(self):
        close = self.browser.find_element(*Locators4KVideoDownloader.COOKIES_CLOSE)
        close.click()
        time.sleep(1)

    def caret_windows(self):
        self.browser.find_element(*Locators4KVideoDownloader.CARET_WINDOWS).click()

    def windows_x64_online(self):
        href = self.browser.find_element(*Locators4KVideoDownloader.WINDOWS_X64ONLINE).get_attribute("href")
        request = head(href)
        self.check_head_status(request)

    def windows_x64_offline(self):
        href = self.browser.find_element(*Locators4KVideoDownloader.WINDOWS_X64OFFLINE).get_attribute("href")
        request = head(href)
        self.check_head_status(request)

    def windows_x64_portable(self):
        href = self.browser.find_element(*Locators4KVideoDownloader.WINDOWS_X64PORTABLE).get_attribute("href")
        request = head(href)
        self.check_head_status(request)

    def windows_x32_online(self):
        href = self.browser.find_element(*Locators4KVideoDownloader.WINDOWS_X32ONLINE).get_attribute("href")
        request = head(href)
        self.check_head_status(request)

    def windows_x32_offline(self):
        href = self.browser.find_element(*Locators4KVideoDownloader.WINDOWS_X32OFFLINE).get_attribute("href")
        request = head(href)
        self.check_head_status(request)

    def windows_x32_portable(self):
        href = self.browser.find_element(*Locators4KVideoDownloader.WINDOWS_X32PORTABLE).get_attribute("href")
        request = head(href)
        self.check_head_status(request)

    def mac_os(self):
        href = self.browser.find_element(*Locators4KVideoDownloader.MACOS).get_attribute("href")
        request = head(href)
        self.check_head_status(request)

    def caret_ubuntu(self):
        caret = self.browser.find_element(*Locators4KVideoDownloader.CARET_UBUNTU)
        caret.click()

    def ubuntu_offline(self):
        href = self.browser.find_element(*Locators4KVideoDownloader.UBUNTU_OFFLINE).get_attribute("href")
        request = head(href)
        self.check_head_status(request)

    def ubuntu_portable(self):
        href = self.browser.find_element(*Locators4KVideoDownloader.UBUNTU_PORTABLE).get_attribute("href")
        request = head(href)
        self.check_head_status(request)

    def android(self):
        href = self.browser.find_element(*Locators4KVideoDownloader.ANDROID).get_attribute("href")
        request = head(href)
        self.check_head_status(request)


class Tokkit(BasePage):

    def cookie_close(self):
        close = self.browser.find_element(*Locators4KYouTubetoMP3.COOKIES_CLOSE)
        close.click()
        time.sleep(1)

    def caret_windows(self):
        self.browser.find_element(*Locators4KYouTubetoMP3.CARET_WINDOWS).click()

    def windows_x64_online(self):
        href = self.browser.find_element(*Locators4ktokkit.WINDOWS_X64ONLINE).get_attribute("href")
        request = head(href)
        self.check_head_status(request)

    def windows_x64_offline(self):
        href = self.browser.find_element(*Locators4ktokkit.WINDOWS_X64OFFLINE).get_attribute("href")
        request = head(href)
        self.check_head_status(request)

    def windows_x64_portable(self):
        href = self.browser.find_element(*Locators4ktokkit.WINDOWS_X64PORTABLE).get_attribute("href")
        request = head(href)
        self.check_head_status(request)

    def windows_x32_online(self):
        href = self.browser.find_element(*Locators4ktokkit.WINDOWS_X32ONLINE).get_attribute("href")
        request = head(href)
        self.check_head_status(request)

    def windows_x32_offline(self):
        href = self.browser.find_element(*Locators4ktokkit.WINDOWS_X32OFFLINE).get_attribute("href")
        request = head(href)
        self.check_head_status(request)

    def windows_x32_portable(self):
        href = self.browser.find_element(*Locators4ktokkit.WINDOWS_X32PORTABLE).get_attribute("href")
        request = head(href)
        self.check_head_status(request)

    def mac_os(self):
        href = self.browser.find_element(*Locators4ktokkit.MACOS).get_attribute("href")
        request = head(href)
        self.check_head_status(request)

    def caret_ubuntu(self):
        self.browser.find_element(*Locators4KYouTubetoMP3.CARET_UBUNTU).click()

    def ubuntu_offline(self):
        href = self.browser.find_element(*Locators4ktokkit.UBUNTU_OFFLINE).get_attribute("href")
        request = head(href)
        self.check_head_status(request)

    def ubuntu_portable(self):
        href = self.browser.find_element(*Locators4ktokkit.UBUNTU_PORTABLE).get_attribute("href")
        request = head(href)
        self.check_head_status(request)


class Youtubetomp3(BasePage):

    def cookie_close(self):
        close = self.browser.find_element(*Locators4KYouTubetoMP3.COOKIES_CLOSE)
        close.click()
        time.sleep(1)

    def caret_windows(self):
        self.browser.find_element(*Locators4KYouTubetoMP3.CARET_WINDOWS).click()

    def windows_x64_online(self):
        href = self.browser.find_element(*Locators4KYouTubetoMP3.WINDOWS_X64ONLINE).get_attribute("href")
        request = head(href)
        self.check_head_status(request)

    def windows_x64_offline(self):
        href = self.browser.find_element(*Locators4KYouTubetoMP3.WINDOWS_X64OFFLINE).get_attribute("href")
        request = head(href)
        self.check_head_status(request)

    def windows_x64_portable(self):
        href = self.browser.find_element(*Locators4KYouTubetoMP3.WINDOWS_X64PORTABLE).get_attribute("href")
        request = head(href)
        self.check_head_status(request)

    def windows_x32_online(self):
        href = self.browser.find_element(*Locators4KYouTubetoMP3.WINDOWS_X32ONLINE).get_attribute("href")
        request = head(href)
        self.check_head_status(request)

    def windows_x32_offline(self):
        href = self.browser.find_element(*Locators4KYouTubetoMP3.WINDOWS_X32OFFLINE).get_attribute("href")
        request = head(href)
        self.check_head_status(request)

    def windows_x32_portable(self):
        href = self.browser.find_element(*Locators4KYouTubetoMP3.WINDOWS_X32PORTABLE).get_attribute("href")
        request = head(href)
        self.check_head_status(request)

    def mac_os(self):
        href = self.browser.find_element(*Locators4KYouTubetoMP3.MACOS).get_attribute("href")
        request = head(href)
        self.check_head_status(request)

    def caret_ubuntu(self):
        self.browser.find_element(*Locators4KYouTubetoMP3.CARET_UBUNTU).click()

    def ubuntu_offline(self):
        href = self.browser.find_element(*Locators4KYouTubetoMP3.UBUNTU_OFFLINE).get_attribute("href")
        request = head(href)
        self.check_head_status(request)

    def ubuntu_portable(self):
        href = self.browser.find_element(*Locators4KYouTubetoMP3.UBUNTU_PORTABLE).get_attribute("href")
        request = head(href)
        self.check_head_status(request)


class Stogram(BasePage):

    def cookie_close(self):
        close = self.browser.find_element(*Locators4KStogram.COOKIES_CLOSE)
        close.click()
        time.sleep(1)

    def caret_windows(self):
        self.browser.find_element(*Locators4KStogram.CARET_WINDOWS).click()

    def windows_x64_online(self):
        href = self.browser.find_element(*Locators4KStogram.WINDOWS_X64ONLINE).get_attribute("href")
        request = head(href)
        self.check_head_status(request)

    def windows_x64_offline(self):
        href = self.browser.find_element(*Locators4KStogram.WINDOWS_X64OFFLINE).get_attribute("href")
        request = head(href)
        self.check_head_status(request)

    def windows_x64_portable(self):
        href = self.browser.find_element(*Locators4KStogram.WINDOWS_X64PORTABLE).get_attribute("href")
        request = head(href)
        self.check_head_status(request)

    def windows_x32_online(self):
        href = self.browser.find_element(*Locators4KStogram.WINDOWS_X32ONLINE).get_attribute("href")
        request = head(href)
        self.check_head_status(request)

    def windows_x32_offline(self):
        href = self.browser.find_element(*Locators4KStogram.WINDOWS_X32OFFLINE).get_attribute("href")
        request = head(href)
        self.check_head_status(request)

    def windows_x32_portable(self):
        href = self.browser.find_element(*Locators4KStogram.WINDOWS_X32PORTABLE).get_attribute("href")
        request = head(href)
        self.check_head_status(request)

    def mac_os(self):
        href = self.browser.find_element(*Locators4KStogram.MACOS).get_attribute("href")
        request = head(href)
        self.check_head_status(request)

    def caret_ubuntu(self):
        self.browser.find_element(*Locators4KStogram.CARET_UBUNTU).click()

    def ubuntu_offline(self):
        href = self.browser.find_element(*Locators4KStogram.UBUNTU_OFFLINE).get_attribute("href")
        request = head(href)
        self.check_head_status(request)

    def ubuntu_portable(self):
        href = self.browser.find_element(*Locators4KStogram.UBUNTU_PORTABLE).get_attribute("href")
        request = head(href)
        self.check_head_status(request)


class SlideshowMaker(BasePage):

    def cookie_close(self):
        close = self.browser.find_element(*Locators4KSlideshowMaker.COOKIES_CLOSE)
        close.click()
        time.sleep(1)

    def caret_windows(self):
        self.browser.find_element(*Locators4KSlideshowMaker.CARET_WINDOWS).click()

    def windows_x64_offline(self):
        href = self.browser.find_element(*Locators4KSlideshowMaker.WINDOWS_X64OFFLINE).get_attribute("href")
        request = head(href)
        self.check_head_status(request)

    def windows_x64_portable(self):
        href = self.browser.find_element(*Locators4KSlideshowMaker.WINDOWS_X64PORTABLE).get_attribute("href")
        request = head(href)
        self.check_head_status(request)

    def windows_x32_offline(self):
        href = self.browser.find_element(*Locators4KSlideshowMaker.WINDOWS_X32OFFLINE).get_attribute("href")
        request = head(href)
        self.check_head_status(request)

    def windows_x32_portable(self):
        href = self.browser.find_element(*Locators4KSlideshowMaker.WINDOWS_X32PORTABLE).get_attribute("href")
        request = head(href)
        self.check_head_status(request)

    def mac_os(self):
        href = self.browser.find_element(*Locators4KSlideshowMaker.MACOS).get_attribute("href")
        request = head(href)
        self.check_head_status(request)

    def caret_ubuntu(self):
        self.browser.execute_script("window.scrollBy(0, 2000);")
        time.sleep(2)
        self.browser.find_element(*Locators4KSlideshowMaker.CARET_UBUNTU).click()


    def ubuntu_offline(self):
        href = self.browser.find_element(*Locators4KSlideshowMaker.UBUNTU_OFFLINE).get_attribute("href")
        request = head(href)
        self.check_head_status(request)

    def ubuntu_portable(self):
        href = self.browser.find_element(*Locators4KSlideshowMaker.UBUNTU_PORTABLE).get_attribute("href")
        request = head(href)
        self.check_head_status(request)


class Videotomp3(BasePage):

    def cookie_close(self):
        close = self.browser.find_element(*Locators4KVideotoMP3.COOKIES_CLOSE)
        close.click()
        time.sleep(1)

    def caret_windows(self):
        self.browser.find_element(*Locators4KVideotoMP3.CARET_WINDOWS).click()

    def windows_x64_offline(self):
        href = self.browser.find_element(*Locators4KVideotoMP3.WINDOWS_X64OFFLINE).get_attribute("href")
        request = head(href)
        self.check_head_status(request)

    def windows_x64_portable(self):
        href = self.browser.find_element(*Locators4KVideotoMP3.WINDOWS_X64PORTABLE).get_attribute("href")
        request = head(href)
        self.check_head_status(request)

    def windows_x32_offline(self):
        href = self.browser.find_element(*Locators4KVideotoMP3.WINDOWS_X32OFFLINE).get_attribute("href")
        request = head(href)
        self.check_head_status(request)

    def windows_x32_portable(self):
        href = self.browser.find_element(*Locators4KVideotoMP3.WINDOWS_X32PORTABLE).get_attribute("href")
        request = head(href)
        self.check_head_status(request)

    def mac_os(self):
        href = self.browser.find_element(*Locators4KVideotoMP3.MACOS).get_attribute("href")
        request = head(href)
        self.check_head_status(request)

    def caret_ubuntu(self):
        self.browser.find_element(*Locators4KVideotoMP3.CARET_UBUNTU).click()

    def ubuntu_offline(self):
        href = self.browser.find_element(*Locators4KVideotoMP3.UBUNTU_OFFLINE).get_attribute("href")
        request = head(href)
        self.check_head_status(request)

    def ubuntu_portable(self):
        href = self.browser.find_element(*Locators4KVideotoMP3.UBUNTU_PORTABLE).get_attribute("href")
        request = head(href)
        self.check_head_status(request)
