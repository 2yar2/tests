from pages.locators import locators_payment
from pages import credentials
from pages.products.products_payment import Stripe
import pytest


class TestStripe:

    @pytest.mark.parametrize('option', [locators_payment.OptionButtons.PERSONAL, locators_payment.OptionButtons.PRO])
    def test_bundle(self, browser, option):
        pg = Stripe(browser, locators_payment.OptionLinks.VD)
        pg.open()

        pg.cookie_close()
        pg.bundle_switch_to(option)
        pg.select_option(locators_payment.OptionButtons.BUNDLE)

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
        pg.find_product_image(locators_payment.ProductImage.Y2MP3)
        pg.find_product_image(locators_payment.ProductImage.STOGRAM)
        pg.find_product_image(locators_payment.ProductImage.TOKKIT)
        pg.find_product_keys(locators_payment.ProductKey.VD)
        pg.find_product_keys(locators_payment.ProductKey.Y2MP3)
        pg.find_product_keys(locators_payment.ProductKey.STOGRAM)
        pg.find_product_keys(locators_payment.ProductKey.TOKKIT)


    @pytest.mark.parametrize('option', [locators_payment.OptionButtons.PERSONAL, locators_payment.OptionButtons.PRO])
    def test_vd(self, browser, option):
        pg = Stripe(browser, locators_payment.OptionLinks.VD)
        pg.open()

        pg.cookie_close()
        pg.select_option(option)

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
        pg.find_product_keys(locators_payment.ProductKey.VD)


    @pytest.mark.parametrize('option', [locators_payment.OptionButtons.PERSONAL, locators_payment.OptionButtons.PRO])
    def test_y2mp3(self, browser, option):
        pg = Stripe(browser, locators_payment.OptionLinks.Y2MP3)
        pg.open()

        pg.cookie_close()
        pg.select_option(option)

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

        pg.find_product_image(locators_payment.ProductImage.Y2MP3)
        pg.find_product_keys(locators_payment.ProductKey.Y2MP3)


    @pytest.mark.parametrize('option', [locators_payment.OptionButtons.PERSONAL, locators_payment.OptionButtons.PRO])
    def test_stogram(self, browser, option):
        pg = Stripe(browser, locators_payment.OptionLinks.STOGRAM)
        pg.open()

        pg.cookie_close()
        pg.select_option(option)

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

        pg.find_product_image(locators_payment.ProductImage.STOGRAM)
        pg.find_product_keys(locators_payment.ProductKey.STOGRAM)
