from selenium.webdriver import Remote as RemoteWebdriver


class BasePage:
    def __init__(self, browser: RemoteWebdriver, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        alert.accept()

    def check_head_status(self, request):
        print('http status: ' + str(request.status_code) + ' ' + request.url)
        assert request.status_code == 200

