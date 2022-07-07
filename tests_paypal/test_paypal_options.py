from pages.locators import locators_payment
from pages.products.products_payment import Paypal
import pytest


class TestPaypal:

    @pytest.mark.parametrize('option', [locators_payment.OptionButtons.PERSONAL, locators_payment.OptionButtons.PRO])
    def test_stogram(self, browser, option):
        pg = Paypal(browser, locators_payment.OptionLinks.STOGRAM)
        pg.open()

        pg.cookie_close()
        pg.select_option(option)

        pg.total_price_exists()
        pg.button_paypal_express()
        pg.paypal_login()
        pg.paypal_purchase()

        pg.find_product_image(locators_payment.ProductImage.STOGRAM)
        pg.find_product_keys(locators_payment.ProductKey.STOGRAM)


    @pytest.mark.parametrize('option', [locators_payment.OptionButtons.PERSONAL, locators_payment.OptionButtons.PRO])
    def test_bundle(self, browser, option):
        pg = Paypal(browser, locators_payment.OptionLinks.STOGRAM)
        pg.open()

        pg.cookie_close()
        pg.bundle_switch_to(option)
        pg.select_option(locators_payment.OptionButtons.BUNDLE)

        pg.total_price_exists()
        pg.button_paypal_express()
        pg.paypal_login()
        pg.paypal_purchase()

        pg.find_product_image(locators_payment.ProductImage.VD)
        pg.find_product_image(locators_payment.ProductImage.Y2MP3)
        pg.find_product_image(locators_payment.ProductImage.STOGRAM)
        pg.find_product_image(locators_payment.ProductImage.TOKKIT)
        pg.find_product_keys(locators_payment.ProductKey.VD)
        pg.find_product_keys(locators_payment.ProductKey.Y2MP3)
        pg.find_product_keys(locators_payment.ProductKey.STOGRAM)
        pg.find_product_keys(locators_payment.ProductKey.TOKKIT)
