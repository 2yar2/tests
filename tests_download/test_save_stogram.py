from pages.products.product_stogram import ButtonDownloadStogram


class TestSaveStogram:

    def test_top_button_save(self, browser):
        product_page = ButtonDownloadStogram(browser, 'https://www.4kdownload.com/products/product-stogram')
        product_page.open()
        product_page.cookie_close()
        product_page.check_button_download_top()

    def test_bottom_button_save(self, browser):
        product_page = ButtonDownloadStogram(browser, 'https://www.4kdownload.com/products/product-stogram')
        product_page.open()
        product_page.cookie_close()
        product_page.scroll_page()
        product_page.check_button_download_bot()
