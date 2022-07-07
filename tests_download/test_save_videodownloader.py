from pages.products.product_videodownloader import ButtonSaveVD
from pages.products.product_videodownloader import ScrollPage
from pages.products.product_videodownloader import AndroidButtonSaveVD

class TestSaveDownloader:

# Проверяем первую кнопку

    def test_button_save_vd(self, browser):
        product_page = ButtonSaveVD(browser, 'https://www.4kdownload.com/products/product-videodownloader')
        product_page.open()
        product_page.cookies_close()
        product_page.button_icon()
        product_page.button_download()
        product_page.button_save()
        print("Test Pass")

class TestScroll:

# Проверяем нижнюю кнопку

    def test_scroll(self, browser):
        product_page = ScrollPage(browser, 'https://www.4kdownload.com/products/product-videodownloader')
        product_page.open()
        product_page.cookies_close()
        product_page.scroll_page()
        product_page.button_download2()
        print("Test Pass")

class TestSaveAndroidDownloader:

#Проверяем первую кнопку

    def test_button_save_android_vd(self, browser):
        product_page = AndroidButtonSaveVD(browser, 'https://www.4kdownload.com/products/product-videodownloaderandroid')
        product_page.open()
        product_page.cookies_close()
        product_page.android_button_icon()
        product_page.android_button_download()
        print("Test Pass")

    def test_scroll(self, browser):
        product_page = ScrollPage(browser, 'https://www.4kdownload.com/products/product-videodownloaderandroid')
        product_page.open()
        product_page.cookies_close()
        product_page.scroll_page()
        product_page.android_button_save()
        print("Test Pass")