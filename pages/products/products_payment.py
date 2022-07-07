from pages.locators import locators_payment
from pages.base_page import BasePage
from pages import credentials
import time
from selenium.webdriver.common.keys import Keys
import logging


class _ProductOptionPage(BasePage):

    def scroll_top(self):
        self.browser.find_element_by_tag_name('body').send_keys(Keys.HOME)
        time.sleep(0.3)

    def cookie_close(self):
        self.browser.find_element(*locators_payment.Cookie.COOKIES_CLOSE).click()
        time.sleep(1)

    def _bundle_switch_to_personal(self):
        try:
            self.browser.find_element(*locators_payment.OptionButtons.PRO)
        except Exception:
            pass
        else:
            self.browser.find_elements(*locators_payment.OptionButtons.BUNDLE_OPTION_SWITCHER)[-1].click()

    def _bundle_switch_to_pro(self):
        try:
            self.browser.find_element(*locators_payment.OptionButtons.PRO)
        except Exception:
            self.browser.find_elements(*locators_payment.OptionButtons.BUNDLE_OPTION_SWITCHER)[-1].click()

    def bundle_switch_to(self, option_locator):
        if option_locator == locators_payment.OptionButtons.PRO:
            self._bundle_switch_to_pro()
        else:
            self._bundle_switch_to_personal()

    def select_option(self, option_selector: tuple):
        self.browser.find_elements(*option_selector)[-1].click()

    def select_license_quantity(self, quantity):
        self.browser.find_elements(*locators_payment.SelectQuantity.LICENSE)[0].click()
        time.sleep(1)

        quantity_locator = locators_payment.SelectQuantity.get_quantity_locator(quantity)
        self.browser.find_element(*quantity_locator).click()
        time.sleep(2)

class _PaymentForm(BasePage):

    def set_email(self, email: str):
        email_element = self.browser.find_element(*locators_payment.CustomerInfo.EMAIL)
        time.sleep(1)
        email_element.send_keys(email)

    def set_name(self, name: str):
        name_element = self.browser.find_element(*locators_payment.CustomerInfo.NAME)
        name_element.send_keys(name)

    def set_country(self, country_selector: tuple):
        self.browser.find_element(*locators_payment.CustomerInfo.COUNTRY).click()
        self.browser.find_element(*country_selector).click()
        time.sleep(2)

    def set_city(self, city):
        city_element = self.browser.find_element(*locators_payment.CustomerInfo.CITY)
        city_element.send_keys(city)

    def set_address(self, address):
        address_element = self.browser.find_element(*locators_payment.CustomerInfo.ADDRESS)
        address_element.send_keys(address)

    def set_state(self, state):
        state_element = self.browser.find_element(*locators_payment.CustomerInfo.STATE)
        state_element.send_keys(state)

    def set_zipcode(self, zipcode):
        zipcode_element = self.browser.find_element(*locators_payment.CustomerInfo.ZIPCODE)
        zipcode_element.send_keys(zipcode)

    def set_company_vatid(self, vatid):
        self.browser.find_element(*locators_payment.CompanyInfo.IMCOMPANY_CHECKBOX).click()
        vat_element = self.browser.find_element(*locators_payment.CompanyInfo.VATID)
        vat_element.send_keys(vatid)
        company_name_element = self.browser.find_element(*locators_payment.CompanyInfo.COMPANYNAME)
        company_name_element.send_keys('OpenMedia')
        time.sleep(2)

    def vat_amount_displayed(self):
        try:
            self.browser.find_element(*locators_payment.PriceDetails.VAT_AMOUNT_TOP)
            self.browser.find_element(*locators_payment.PriceDetails.VAT_AMOUNT_BOT)
        except Exception:
            return False
        else:
            return True

    def set_payment_method(self, payment_method_selector: tuple):
        self.browser.find_element(*payment_method_selector).click()
        time.sleep(1)

    def check_klarna_payment_page(self):
        # Too complicated confirmation, just check we in klarna page.
        self.browser.find_element(*locators_payment.Klarna.PRICE)
        self.browser.find_element(*locators_payment.Klarna.BUY)

    def total_price_exists(self):
        self.browser.find_element(*locators_payment.PriceDetails.TOTAL_PRICE)

    def local_currency_exists(self):
        self.browser.find_element(*locators_payment.PriceDetails.LOCAL_CURRENCY_TOP)
        self.browser.find_element(*locators_payment.PriceDetails.LOCAL_CURRENCY_BOT)

    def button_paypal_express(self):
        self.scroll_top()
        self.browser.find_element(*locators_payment.PaymentButton.BUTTON_PAYPAL_EXPRESS).click()
        time.sleep(3)

    def button_buy(self):
        self.browser.find_element(*locators_payment.PaymentButton.BUTTON_BUY).click()
        time.sleep(3)

    def stripe_authorize_test_payment(self):
        time.sleep(3)
        self.browser.find_element(*locators_payment.PaymentButton.BUTTON_AUTHORIZE_TEST_PAYMENT).click()
        time.sleep(5)

    def stripe_authorize_3d_secure(self):
        self.browser.switch_to.frame(self.browser.find_element(*locators_payment.ThreeDSecure.IFRAME1))
        self.browser.switch_to.frame(self.browser.find_element(*locators_payment.ThreeDSecure.IFRAME2))
        time.sleep(2)
        self.browser.switch_to.frame(self.browser.find_element(*locators_payment.ThreeDSecure.IFRAME3))
        time.sleep(2)

        self.browser.find_element(*locators_payment.ThreeDSecure.COMPLETLE_AUTHENTIFICATION).submit()
        time.sleep(5)
        self.browser.switch_to.default_content()
        time.sleep(2)


class _StripeCardForm(BasePage):

    def set_card_name(self, card_name):
        name_element = self.browser.find_element(*locators_payment.StripeCard.CARD_NAME)
        name_element.send_keys(card_name)

    def set_card_number(self, card_number):
        self.browser.switch_to.frame(self.browser.find_element(*locators_payment.StripeCard.IFRAME_CARD_NUMBER))
        number_element = self.browser.find_element(*locators_payment.StripeCard.CARD_NUMBER)
        number_element.send_keys(card_number)
        self.browser.switch_to.default_content()

    def set_expiry_date(self, expiry_date):
        self.browser.switch_to.frame(self.browser.find_element(*locators_payment.StripeCard.IFRAME_EXPIRY_DATE))
        date_element = self.browser.find_element(*locators_payment.StripeCard.EXPIRY_DATE)
        date_element.send_keys(expiry_date)
        self.browser.switch_to.default_content()

    def set_cvc(self, cvc):
        self.browser.switch_to.frame(self.browser.find_element(*locators_payment.StripeCard.IFRAME_CVC))
        cvc_element = self.browser.find_element(*locators_payment.StripeCard.CVC)
        cvc_element.send_keys(cvc)
        self.browser.switch_to.default_content()
        time.sleep(1)

    def set_qrcode(self):
        self.browser.find_element(*locators_payment.QrCode.QR)


class _ThanksPage(BasePage):

    def find_product_image(self, product_image_selector):
        time.sleep(4)
        self.browser.find_element(*product_image_selector)

    def find_product_keys(self, product_keys_selector, quantity=1):
        time.sleep(1)
        key_elements = self.browser.find_elements(*product_keys_selector)
        assert len(key_elements) == quantity


class _PaypalPage(BasePage):

    def _try_close_cookie(self):
        try:
            time.sleep(1)
            if cookie_button := self.browser.find_element(*locators_payment.PaypalAccount.COOKIE):
                cookie_button.click()
            time.sleep(1)
        except Exception:
            logging.exception('Paypal Cookie Button not clickable')

    def paypal_login(self):
        time.sleep(7)
        self._try_close_cookie()
        login_element = self.browser.find_element(*locators_payment.PaypalAccount.EMAIL)
        login_element.send_keys(credentials.PaypalTestAccount.EMAIL)
        self.browser.find_element(*locators_payment.PaypalAccount.BUTTON_NEXT).click()

        self._try_close_cookie()
        password_element = self.browser.find_element(*locators_payment.PaypalAccount.PASSWORD)
        password_element.send_keys(credentials.PaypalTestAccount.PSWD)
        self.browser.find_element(*locators_payment.PaypalAccount.BUTTON_LOGIN).click()

    def paypal_purchase(self):
        time.sleep(5)
        self._try_close_cookie()
        self.browser.find_element(*locators_payment.PaypalAccount.BUTTON_CONTINUE).click()
        time.sleep(10)

class _Yookassa(BasePage):

    def set_yookassa_number(self, card_number):
        number = self.browser.find_element(*locators_payment.Yookassa.YOOKASSA_CARD_NUMBER)
        number.send_keys(card_number)

    def set_yookassa_month(self, card_month):
        month = self.browser.find_element(*locators_payment.Yookassa.YOOKASSA_MONTH)
        month.send_keys(card_month)

    def set_yookassa_year(self, card_year):
        year = self.browser.find_element(*locators_payment.Yookassa.YOOKASSA_YEAR)
        year.send_keys(card_year)

    def set_yookassa_cvc(self, card_cvc):
        cvc = self.browser.find_element(*locators_payment.Yookassa.YOOKASSA_CVC)
        cvc.send_keys(card_cvc)

    def set_yookassa_pay(self):
        self.browser.find_element(*locators_payment.Yookassa.YOOKASSA_PAY).click()

    def set_payment_complete(self):
        self.browser.find_element(*locators_payment.Yookassa.YOOKASSA_PAYMENT_COMPLETE)

    def set_bask_to_the_store(self):
        self.browser.find_element(*locators_payment.Yookassa.YOOKASSA_BACK_TO_THE_STORE).click()

class Paypal(_ProductOptionPage, _PaymentForm, _PaypalPage, _ThanksPage):
    pass


class Stripe(_ProductOptionPage, _PaymentForm, _StripeCardForm, _ThanksPage):
    pass


class Yookassa(_ProductOptionPage, _PaymentForm, _Yookassa, _ThanksPage):
    pass
