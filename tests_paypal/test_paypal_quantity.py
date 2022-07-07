from pages.locators import locators_payment
from pages.products.products_payment import Paypal
import pytest

class TestQuantity:

    @pytest.mark.parametrize('quantity', [1, 5, 10])
    def test_paypal(self, browser, quantity):
        pg = Paypal(browser, locators_payment.OptionLinks.VD)
        pg.open()

        pg.cookie_close()
        pg.bundle_switch_to(locators_payment.OptionButtons.PERSONAL)
        pg.select_option(locators_payment.OptionButtons.BUNDLE)

        pg.select_license_quantity(quantity)
        pg.total_price_exists()
        pg.button_paypal_express()
        pg.paypal_login()
        pg.paypal_purchase()

        pg.find_product_image(locators_payment.ProductImage.VD)
        pg.find_product_image(locators_payment.ProductImage.Y2MP3)
        pg.find_product_image(locators_payment.ProductImage.STOGRAM)
        pg.find_product_image(locators_payment.ProductImage.TOKKIT)
        pg.find_product_keys(locators_payment.ProductKey.VD, quantity)
        pg.find_product_keys(locators_payment.ProductKey.Y2MP3, quantity)
        pg.find_product_keys(locators_payment.ProductKey.STOGRAM, quantity)
        pg.find_product_keys(locators_payment.ProductKey.TOKKIT, quantity)