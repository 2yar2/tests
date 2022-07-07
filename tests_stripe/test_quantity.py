from pages.locators import locators_payment
from pages import credentials
from pages.products.products_payment import Stripe, Paypal
import pytest

class TestQuantity:

    @pytest.mark.parametrize('quantity', [1, 5, 10])
    def test_stripe(self, browser, quantity):
        pg = Stripe(browser, locators_payment.OptionLinks.VD)
        pg.open()

        pg.cookie_close()
        pg.select_option(locators_payment.OptionButtons.PERSONAL)
        pg.select_license_quantity(quantity)
        pg.set_email(credentials.StripeTestAccount.EMAIL)
        pg.set_name('IVAN PETROV')
        pg.set_country(locators_payment.Country.UNITED_STATES)
        pg.set_city('City')
        pg.set_address('Customer Address')
        pg.set_state('State')
        pg.set_zipcode('12345')

        pg.total_price_exists()

        pg.set_card_name('IVAN PETROV')
        pg.set_card_number('4242424242424242')
        pg.set_expiry_date('0126')
        pg.set_cvc('777')

        pg.button_buy()

        pg.find_product_image(locators_payment.ProductImage.VD)
        pg.find_product_keys(locators_payment.ProductKey.VD, quantity)

