from selenium.webdriver.common.by import By


# product buy page with options

class Cookie:
    COOKIES_CLOSE = (By.CLASS_NAME, "icon__ic-cross")


class OptionLinks:
    VD = 'https://www.qa.4kdownload.com/buy/videodownloader'
    Y2MP3 = 'https://www.qa.4kdownload.com/buy/youtubetomp3'
    STOGRAM = 'https://www.qa.4kdownload.com/buy/stogram'


class OptionButtons:
    PERSONAL = (By.CSS_SELECTOR, ".buy-page__button--personal")
    PRO = (By.CSS_SELECTOR, ".buy-page__button--professional")
    BUNDLE = (By.CSS_SELECTOR, ".buy-page__button--bundle")
    BUNDLE_OPTION_SWITCHER = (By.CSS_SELECTOR, ".buy-page__input_checkbox-bundle")



# payment form

class PaymentButton:
    BUTTON_BUY = (By.CSS_SELECTOR, ".buy-page__button--buy")
    BUTTON_PAYPAL_EXPRESS = (By.CSS_SELECTOR, ".buy-page__form-express_button--paypal")
    BUTTON_AUTHORIZE_TEST_PAYMENT = (By.CSS_SELECTOR, '.common-Button--default')


class PriceDetails:
    TOTAL_PRICE = (By.CSS_SELECTOR, ".buy-page__form-info_text--big")
    VAT_AMOUNT_TOP = (By.CSS_SELECTOR, ".buy-page__top-text--right")
    VAT_AMOUNT_BOT = (By.CSS_SELECTOR, ".buy-page__form-info_text.buy-page__form-info_note")
    LOCAL_CURRENCY_TOP = (By.CSS_SELECTOR, ".buy-page__top-text--right")
    LOCAL_CURRENCY_BOT = (By.CSS_SELECTOR, ".buy-page__form-info_text.buy-page__form-info_note")


class PaymentMethod:
    ALIPAY = (By.ID, "alipay")
    EPS = (By.ID, "eps")
    SOFORT = (By.ID, "sofort")
    BANCONTACT = (By.ID, "bancontact")
    KLARNA = (By.ID, "klarna")
    CARTES_BANCAIRES = (By.ID, "cartes-bancaires__label")
    GIROPAY = (By.ID, "giropay")
    WECHAT = (By.ID, "wechat")
    IDEAL = (By.ID, "ideal")
    P24 = (By.ID, "p24")
    MULTIBANKO = (By.ID, "multibanco")
    PAYPAL = (By.ID, "paypal")


class Klarna:
    PRICE = (By.ID, 'order-amount__container')
    BUY = (By.ID, 'buy-button')

class Yookassa:
    YOOKASSA_CARD_NUMBER = (By.ID, 'cardNumber')
    YOOKASSA_MONTH = (By.CSS_SELECTOR, '[placeholder="ММ"]')
    YOOKASSA_YEAR = (By.CSS_SELECTOR, '[placeholder="ГГ"]')
    YOOKASSA_CVC = (By.CSS_SELECTOR, '[placeholder="CVC"]')
    YOOKASSA_PAY = (By.CSS_SELECTOR, ".button__control span")
    YOOKASSA_PAYMENT_COMPLETE = (By.CSS_SELECTOR, ".title.title_last_yes")
    YOOKASSA_BACK_TO_THE_STORE = (By.XPATH, '/html/body/div[1]/div/a')

class ThreeDSecure:
    IFRAME1 = (By.XPATH, '/html/body/div[1]/iframe')
    IFRAME2 = (By.ID, "challengeFrame")
    IFRAME3 = (By.CSS_SELECTOR, ".FullscreenFrame")
    COMPLETLE_AUTHENTIFICATION = (By.ID, "test-source-authorize-3ds")


class StripeCard:
    CARD_NAME = (By.ID, "form-pay__card_name")

    IFRAME_CARD_NUMBER = (By.XPATH, '//*[@id="cardNumber"]/div/iframe')
    CARD_NUMBER = (By.XPATH, '//*[@id="root"]/form/span[2]/div/div[2]/span/input')

    IFRAME_EXPIRY_DATE = (By.XPATH, '//*[@id="cardExpiry"]/div/iframe')
    EXPIRY_DATE = (By.XPATH, '//input[@name="exp-date"]')

    IFRAME_CVC = (By.XPATH, '//*[@id="cardCvcNumber"]/div/iframe')
    CVC = (By.XPATH, '//input[@name="cvc"]')

class QrCode:
    QR = (By.XPATH, '//*[@id="wechat"]/div[2]/img')


class CustomerInfo:
    EMAIL = (By.ID, "form-pay__email")
    NAME = (By.ID, "form-pay__name")
    COUNTRY = (By.ID, "country-select-button")
    CITY = (By.ID, "form-pay__city")
    ADDRESS = (By.ID, "form-pay__address")
    STATE = (By.ID, "form-pay__state")
    ZIPCODE = (By.ID, "form-pay__zip-code")


class Country:
    AUSTRIA = (By.CSS_SELECTOR, "[data-index='14']")
    BELGIUM = (By.CSS_SELECTOR, "[data-index='21']")
    CHINA = (By.CSS_SELECTOR, "[data-index='46']")
    FINLAND = (By.CSS_SELECTOR, "[data-index='74']")
    FRANCE = (By.CSS_SELECTOR, "[data-index='75']")
    GERMANY = (By.CSS_SELECTOR, "[data-index='82']")
    HONGKONG = (By.CSS_SELECTOR, "[data-index='98']")
    NETHERLANDS = (By.CSS_SELECTOR, "[data-index='155']")
    POLAND = (By.CSS_SELECTOR, "[data-index='176']")
    PORTUGAL = (By.CSS_SELECTOR, "[data-index='177']")
    SINGAPORE = (By.CSS_SELECTOR, "[data-index='199']")
    UNITED_KINGDOM = (By.CSS_SELECTOR, "[data-index='237']")
    UNITED_STATES = (By.CSS_SELECTOR, "[data-index='238']")
    RUSSIA = (By.CSS_SELECTOR, "[data-index='182']")

class CompanyInfo:
    IMCOMPANY_CHECKBOX = (By.ID, "company-checkbox__label")
    COMPANYNAME = (By.ID, "form-pay__name-company")
    VATID = (By.ID, "form-pay__vat-company")


# paypal.com

class PaypalAccount:
    EMAIL = (By.ID, "email")
    PASSWORD = (By.ID, "password")
    COOKIE = (By.ID, "acceptAllButton")
    BUTTON_NEXT = (By.ID, "btnNext")
    BUTTON_LOGIN = (By.ID, "btnLogin")
    BUTTON_CONTINUE = (By.ID, "payment-submit-btn")


# Thanks for purchase page

class ProductImage:
    VD = (By.CSS_SELECTOR, ".pay-success__header_img--videodownloader")
    Y2MP3 = (By.CSS_SELECTOR, ".pay-success__header_img--youtubetomp3")
    STOGRAM = (By.CSS_SELECTOR, ".pay-success__header_img--stogram")
    TOKKIT = (By.CSS_SELECTOR, ".pay-success__header_img--tokkit")


class ProductKey:
    VD = (By.CLASS_NAME, "videodownloader_key")
    Y2MP3 = (By.CLASS_NAME, "youtubetomp3_key")
    STOGRAM = (By.CLASS_NAME, "stogram_key")
    TOKKIT = (By.CLASS_NAME, "tokkit_key")

class SelectQuantity:
    LICENSE = (By.CSS_SELECTOR, ".buy-page__top-text.buy-page__popup-select_arrow.buy-page__popup-select_arrow.dark-blue-arrow-down")

    @staticmethod
    def get_quantity_locator(quantity):
        return (By.ID, f'form-header-quanity-option-{quantity}')
