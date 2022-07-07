from pages import credentials
from pages.locators import locators_payment
from pages.products.products_payment import Stripe


class TestCompanyVat:

    def test_austria(self, browser):
        pg = Stripe(browser, locators_payment.OptionLinks.VD)
        pg.open()

        pg.cookie_close()
        pg.select_option(locators_payment.OptionButtons.PERSONAL)

        pg.set_email(credentials.StripeTestAccount.EMAIL)
        pg.set_name('IVAN PETROV')
        pg.set_country(locators_payment.Country.AUSTRIA)
        assert pg.vat_amount_displayed()
        pg.set_city('City')
        pg.set_address('Customer Address')
        pg.set_state('State')
        pg.set_zipcode('12345')

        pg.set_company_vatid('ATU66889218')
        assert not pg.vat_amount_displayed()

        pg.set_card_name('IVAN PETROV')
        pg.set_card_number('4242424242424242')
        pg.set_expiry_date('0126')
        pg.set_cvc('777')

        pg.total_price_exists()
        pg.button_buy()

        pg.find_product_image(locators_payment.ProductImage.VD)
        pg.find_product_keys(locators_payment.ProductKey.VD)


    def test_germany(self, browser):
        pg = Stripe(browser, locators_payment.OptionLinks.VD)
        pg.open()

        pg.cookie_close()
        pg.select_option(locators_payment.OptionButtons.PERSONAL)

        pg.set_email(credentials.StripeTestAccount.EMAIL)
        pg.set_name('IVAN PETROV')
        pg.set_country(locators_payment.Country.GERMANY)
        assert pg.vat_amount_displayed()
        pg.set_city('City')
        pg.set_address('Customer Address')
        pg.set_state('State')
        pg.set_zipcode('12345')

        pg.set_company_vatid('DE194710861')
        assert pg.vat_amount_displayed()

        '''
        disable next actions due to night downtime in eu vat validation service

        pg.set_card_name('IVAN PETROV')
        pg.set_card_number('4242424242424242')
        pg.set_expiry_date('0126')
        pg.set_cvc('777')

        pg.total_price_exists()
        pg.button_buy()

        pg.find_product_image(locators_payment.ProductImage.VD)
        pg.find_product_keys(locators_payment.ProductKey.VD)
        '''

    def test_uk(self, browser):
        pg = Stripe(browser, locators_payment.OptionLinks.VD)
        pg.open()

        pg.cookie_close()
        pg.select_option(locators_payment.OptionButtons.PERSONAL)

        pg.set_email(credentials.StripeTestAccount.EMAIL)
        pg.set_name('IVAN PETROV')
        pg.set_country(locators_payment.Country.UNITED_KINGDOM)
        assert pg.vat_amount_displayed()
        pg.set_city('City')
        pg.set_address('Customer Address')
        pg.set_state('State')
        pg.set_zipcode('12345')

        pg.set_company_vatid('GB773663791')
        assert pg.vat_amount_displayed()

        pg.set_card_name('IVAN PETROV')
        pg.set_card_number('4242424242424242')
        pg.set_expiry_date('0126')
        pg.set_cvc('777')

        pg.total_price_exists()
        pg.button_buy()

        pg.find_product_image(locators_payment.ProductImage.VD)
        pg.find_product_keys(locators_payment.ProductKey.VD)
