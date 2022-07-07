from pages.products.product_downloads_all_files import VideoDownloader
from pages.products.product_downloads_all_files import Youtubetomp3
from pages.products.product_downloads_all_files import Stogram
from pages.products.product_downloads_all_files import SlideshowMaker
from pages.products.product_downloads_all_files import Videotomp3
from pages.products.product_downloads_all_files import Tokkit

DOWNLOADS_URL = 'https://www.qa.4kdownload.com/downloads/'


class Test4KVideoDownloader:

    def test_download_videodownloader(self, browser):
        product_page = VideoDownloader(browser, DOWNLOADS_URL)
        product_page.open()
        product_page.cookie_close()
        product_page.caret_windows()
        product_page.windows_x64_online()
        product_page.windows_x64_offline()
        product_page.windows_x64_portable()
        product_page.windows_x32_online()
        product_page.windows_x32_offline()
        product_page.windows_x32_portable()
        product_page.mac_os()
        product_page.caret_ubuntu()
        product_page.ubuntu_offline()
        product_page.ubuntu_portable()
        product_page.android()


class Test4KTokkit:

    def test_download_tokkit(self, browser):
        product_page = Tokkit(browser, DOWNLOADS_URL)
        product_page.open()
        product_page.cookie_close()
        product_page.caret_windows()
        product_page.windows_x64_online()
        product_page.windows_x64_offline()
        product_page.windows_x64_portable()
        product_page.windows_x32_online()
        product_page.windows_x32_offline()
        product_page.windows_x32_portable()
        product_page.mac_os()
        product_page.caret_ubuntu()
        product_page.ubuntu_offline()
        product_page.ubuntu_portable()


class Test4KYouTubetoMP3:

    def test_download_youtubetomp3(self, browser):
        product_page = Youtubetomp3(browser, DOWNLOADS_URL)
        product_page.open()
        product_page.cookie_close()
        product_page.caret_windows()
        product_page.windows_x64_online()
        product_page.windows_x64_offline()
        product_page.windows_x64_portable()
        product_page.windows_x32_online()
        product_page.windows_x32_offline()
        product_page.windows_x32_portable()
        product_page.mac_os()
        product_page.caret_ubuntu()
        product_page.ubuntu_offline()
        product_page.ubuntu_portable()


class Test4KStogram:

    def test_download_stogram(self, browser):
        product_page = Stogram(browser, DOWNLOADS_URL)
        product_page.open()
        product_page.cookie_close()
        product_page.caret_windows()
        product_page.windows_x64_online()
        product_page.windows_x64_offline()
        product_page.windows_x64_portable()
        product_page.windows_x32_online()
        product_page.windows_x32_offline()
        product_page.windows_x32_portable()
        product_page.mac_os()
        product_page.caret_ubuntu()
        product_page.ubuntu_offline()
        product_page.ubuntu_portable()


class Test4KSlideshow:

    def test_download_slideshow(self, browser):
        product_page = SlideshowMaker(browser, DOWNLOADS_URL)
        product_page.open()
        product_page.cookie_close()
        product_page.caret_windows()
        product_page.windows_x64_offline()
        product_page.windows_x64_portable()
        product_page.windows_x32_offline()
        product_page.windows_x32_portable()
        product_page.mac_os()
        product_page.caret_ubuntu()
        product_page.ubuntu_offline()
        product_page.ubuntu_portable()


class Test4KVideotomp3:

    def test_download_videotomp3(self, browser):
        product_page = Videotomp3(browser, DOWNLOADS_URL)
        product_page.open()
        product_page.cookie_close()
        product_page.caret_windows()
        product_page.windows_x64_offline()
        product_page.windows_x64_portable()
        product_page.windows_x32_offline()
        product_page.windows_x32_portable()
        product_page.mac_os()
        product_page.caret_ubuntu()
        product_page.ubuntu_offline()
        product_page.ubuntu_portable()

