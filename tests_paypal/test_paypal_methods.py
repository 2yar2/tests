from pages.locators import locators_payment
from pages import credentials
from pages.products.products_payment import Paypal


class TestPaypal:

    def test_paypal_as_payment_option(self, browser):
        pg = Paypal(browser, locators_payment.OptionLinks.VD)
        pg.open()

        pg.cookie_close()
        pg.select_option(locators_payment.OptionButtons.PERSONAL)

        pg.set_email(credentials.PaypalTestAccount.EMAIL)
        pg.set_name('IVAN PETROV')
        pg.set_country(locators_payment.Country.UNITED_STATES)
        pg.set_city('City')
        pg.set_address('Customer Address')
        pg.set_state('State')
        pg.set_zipcode('12345')
        pg.set_payment_method(locators_payment.PaymentMethod.PAYPAL)
        pg.total_price_exists()
        pg.button_buy()
        pg.paypal_login()
        pg.paypal_purchase()
        pg.find_product_image(locators_payment.ProductImage.VD)
        pg.find_product_keys(locators_payment.ProductKey.VD)


    def test_paypal_express_button(self, browser):
        pg = Paypal(browser, locators_payment.OptionLinks.VD)
        pg.open()

        pg.cookie_close()
        pg.select_option(locators_payment.OptionButtons.PERSONAL)

        pg.button_paypal_express()
        pg.paypal_login()
        pg.paypal_purchase()

        pg.find_product_image(locators_payment.ProductImage.VD)
        pg.find_product_keys(locators_payment.ProductKey.VD)