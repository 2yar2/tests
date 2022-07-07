from pages.locators import locators_payment
from pages import credentials
from pages.products.products_payment import Stripe
import time


class TestStripe:

    def test_card(self, browser):
        pg = Stripe(browser, locators_payment.OptionLinks.VD)
        pg.open()

        pg.cookie_close()
        pg.select_option(locators_payment.OptionButtons.PERSONAL)

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



    def test_card_3d_secure(self, browser):
        pg = Stripe(browser, locators_payment.OptionLinks.VD)
        pg.open()

        pg.cookie_close()
        pg.select_option(locators_payment.OptionButtons.PERSONAL)

        pg.set_email(credentials.StripeTestAccount.EMAIL)
        pg.set_name('IVAN PETROV')
        pg.set_country(locators_payment.Country.UNITED_STATES)
        pg.set_city('City')
        pg.set_address('Customer Address')
        pg.set_state('State')
        pg.set_zipcode('12345')

        pg.total_price_exists()

        pg.set_card_name('IVAN PETROV')
        pg.set_card_number('4000002500003155')
        pg.set_expiry_date('0126')
        pg.set_cvc('777')

        pg.button_buy()
        pg.stripe_authorize_3d_secure()

        pg.find_product_image(locators_payment.ProductImage.VD)
        pg.find_product_keys(locators_payment.ProductKey.VD)



    def test_eps(self, browser):
        pg = Stripe(browser, locators_payment.OptionLinks.VD)
        pg.open()

        pg.cookie_close()
        pg.select_option(locators_payment.OptionButtons.PERSONAL)

        pg.set_country(locators_payment.Country.AUSTRIA)
        assert pg.vat_amount_displayed()

        pg.set_email(credentials.StripeTestAccount.EMAIL)
        pg.set_name('IVAN PETROV')
        pg.set_city('City')
        pg.set_address('Customer Address')
        pg.set_state('State')
        pg.set_zipcode('12345')
        pg.set_payment_method(locators_payment.PaymentMethod.EPS)
        pg.total_price_exists()
        pg.button_buy()
        pg.stripe_authorize_test_payment()

        pg.find_product_image(locators_payment.ProductImage.VD)
        pg.find_product_keys(locators_payment.ProductKey.VD)



    def test_sofort(self, browser):
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
        pg.set_payment_method(locators_payment.PaymentMethod.SOFORT)
        pg.total_price_exists()
        pg.button_buy()
        pg.stripe_authorize_test_payment()

        pg.find_product_image(locators_payment.ProductImage.VD)
        pg.find_product_keys(locators_payment.ProductKey.VD)



    def test_bancontact(self, browser):
        pg = Stripe(browser, locators_payment.OptionLinks.VD)
        pg.open()

        pg.cookie_close()
        pg.select_option(locators_payment.OptionButtons.PERSONAL)

        pg.set_email(credentials.StripeTestAccount.EMAIL)
        pg.set_name('IVAN PETROV')
        pg.set_country(locators_payment.Country.BELGIUM)
        assert pg.vat_amount_displayed()
        pg.set_city('City')
        pg.set_address('Customer Address')
        pg.set_state('State')
        pg.set_zipcode('12345')
        pg.set_payment_method(locators_payment.PaymentMethod.BANCONTACT)
        pg.total_price_exists()
        pg.button_buy()
        pg.stripe_authorize_test_payment()

        pg.find_product_image(locators_payment.ProductImage.VD)
        pg.find_product_keys(locators_payment.ProductKey.VD)


    def test_alipay(self, browser):
        pg = Stripe(browser, locators_payment.OptionLinks.VD)
        pg.open()

        pg.cookie_close()
        pg.select_option(locators_payment.OptionButtons.PERSONAL)

        pg.set_email(credentials.StripeTestAccount.EMAIL)
        pg.set_name('IVAN PETROV')
        pg.set_country(locators_payment.Country.CHINA)
        pg.local_currency_exists()
        pg.set_city('City')
        pg.set_address('Customer Address')
        pg.set_state('State')
        pg.set_zipcode('12345')
        pg.set_payment_method(locators_payment.PaymentMethod.ALIPAY)
        pg.total_price_exists()
        pg.button_buy()
        pg.stripe_authorize_test_payment()

        pg.find_product_image(locators_payment.ProductImage.VD)
        pg.find_product_keys(locators_payment.ProductKey.VD)


    def test_klarna(self, browser):
        pg = Stripe(browser, locators_payment.OptionLinks.VD)
        pg.open()

        pg.cookie_close()
        pg.select_option(locators_payment.OptionButtons.PERSONAL)

        pg.set_email(credentials.StripeTestAccount.EMAIL)
        pg.set_name('IVAN PETROV')
        pg.set_country(locators_payment.Country.FINLAND)
        assert pg.vat_amount_displayed()
        pg.set_city('City')
        pg.set_address('Customer Address')
        pg.set_state('State')
        pg.set_zipcode('12345')
        pg.set_payment_method(locators_payment.PaymentMethod.KLARNA)
        pg.total_price_exists()
        pg.button_buy()
        pg.check_klarna_payment_page()


    def test_cartes_bancaires(self, browser):
        pg = Stripe(browser, locators_payment.OptionLinks.VD)
        pg.open()

        pg.cookie_close()
        pg.select_option(locators_payment.OptionButtons.PERSONAL)

        pg.set_email(credentials.StripeTestAccount.EMAIL)
        pg.set_name('IVAN PETROV')
        pg.set_country(locators_payment.Country.FRANCE)
        assert pg.vat_amount_displayed()
        pg.set_city('City')
        pg.set_address('Customer Address')
        pg.set_state('State')
        pg.set_zipcode('12345')
        pg.set_payment_method(locators_payment.PaymentMethod.CARTES_BANCAIRES)
        pg.total_price_exists()

        pg.set_card_name('IVAN PETROV')
        pg.set_card_number('4000002500001001')
        pg.set_expiry_date('0126')
        pg.set_cvc('777')

        pg.button_buy()
        #pg.stripe_authorize_test_payment()

        pg.find_product_image(locators_payment.ProductImage.VD)
        pg.find_product_keys(locators_payment.ProductKey.VD)


    def test_giropay(self, browser):
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
        pg.set_payment_method(locators_payment.PaymentMethod.GIROPAY)
        pg.total_price_exists()
        pg.button_buy()
        pg.stripe_authorize_test_payment()

        pg.find_product_image(locators_payment.ProductImage.VD)
        pg.find_product_keys(locators_payment.ProductKey.VD)



    def test_ideal(self, browser):
        pg = Stripe(browser, locators_payment.OptionLinks.VD)
        pg.open()

        pg.cookie_close()
        pg.select_option(locators_payment.OptionButtons.PERSONAL)

        pg.set_email(credentials.StripeTestAccount.EMAIL)
        pg.set_name('IVAN PETROV')
        pg.set_country(locators_payment.Country.NETHERLANDS)
        assert pg.vat_amount_displayed()
        pg.set_city('City')
        pg.set_address('Customer Address')
        pg.set_state('State')
        pg.set_zipcode('12345')
        pg.set_payment_method(locators_payment.PaymentMethod.IDEAL)
        pg.total_price_exists()
        pg.button_buy()
        pg.stripe_authorize_test_payment()

        pg.find_product_image(locators_payment.ProductImage.VD)
        pg.find_product_keys(locators_payment.ProductKey.VD)



    def test_p24(self, browser):
        pg = Stripe(browser, locators_payment.OptionLinks.VD)
        pg.open()

        pg.cookie_close()
        pg.select_option(locators_payment.OptionButtons.PERSONAL)

        pg.set_email(credentials.StripeTestAccount.EMAIL)
        pg.set_name('IVAN PETROV')
        pg.set_country(locators_payment.Country.POLAND)
        assert pg.vat_amount_displayed()
        pg.set_city('City')
        pg.set_address('Customer Address')
        pg.set_state('State')
        pg.set_zipcode('12345')
        pg.set_payment_method(locators_payment.PaymentMethod.P24)
        pg.total_price_exists()
        pg.button_buy()
        pg.stripe_authorize_test_payment()

        pg.find_product_image(locators_payment.ProductImage.VD)
        pg.find_product_keys(locators_payment.ProductKey.VD)


    def test_multibanko(self, browser):
        pg = Stripe(browser, locators_payment.OptionLinks.VD)
        pg.open()

        pg.cookie_close()
        pg.select_option(locators_payment.OptionButtons.PERSONAL)

        pg.set_email(credentials.StripeTestAccount.EMAIL)
        pg.set_name('IVAN PETROV')
        pg.set_country(locators_payment.Country.PORTUGAL)
        assert pg.vat_amount_displayed()
        pg.set_city('City')
        pg.set_address('Customer Address')
        pg.set_state('State')
        pg.set_zipcode('12345')
        pg.set_payment_method(locators_payment.PaymentMethod.MULTIBANKO)
        pg.total_price_exists()
        pg.button_buy()
        time.sleep(5)
        pg.stripe_authorize_test_payment()

        pg.find_product_image(locators_payment.ProductImage.VD)
        pg.find_product_keys(locators_payment.ProductKey.VD)


    def test_wechat(self, browser):
        pg = Stripe(browser, locators_payment.OptionLinks.VD)
        pg.open()

        pg.cookie_close()
        pg.select_option(locators_payment.OptionButtons.PERSONAL)

        pg.set_email(credentials.StripeTestAccount.EMAIL)
        pg.set_name('IVAN PETROV')
        pg.set_country(locators_payment.Country.CHINA)
        pg.set_city('City')
        pg.set_address('Customer Address')
        pg.set_state('State')
        pg.set_zipcode('12345')
        pg.set_payment_method(locators_payment.PaymentMethod.WECHAT)
        pg.total_price_exists()
        pg.button_buy()
        time.sleep(5)
        pg.set_qrcode()



