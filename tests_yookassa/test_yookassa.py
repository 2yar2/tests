from pages.locators import locators_payment
from pages import credentials
from pages.products.products_payment import Yookassa

class TestYookassa:

    def test_youkassa(self, browser):
        pg = Yookassa(browser, locators_payment.OptionLinks.VD)
        pg.open()

        pg.cookie_close()
        pg.select_option(locators_payment.OptionButtons.PERSONAL)

        pg.set_email(credentials.PaypalTestAccount.EMAIL)
        pg.set_name('IVAN PETROV')
        pg.set_city('City')
        pg.set_address('Customer Address')
        pg.set_state('State')
        pg.set_zipcode('12345')
        pg.set_country(locators_payment.Country.RUSSIA)
        pg.button_buy()

        pg.set_yookassa_number('4111 1111 1111 1111')
        pg.set_yookassa_month('11')
        pg.set_yookassa_year('25')
        pg.set_yookassa_cvc('333')
        pg.set_yookassa_pay()
        pg.set_payment_complete()
        pg.set_bask_to_the_store()

        pg.find_product_image(locators_payment.ProductImage.VD)
        pg.find_product_keys(locators_payment.ProductKey.VD)