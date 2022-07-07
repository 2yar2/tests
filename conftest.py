import pytest
from selenium import webdriver
from selenium.webdriver.remote.remote_connection import RemoteConnection
from selenium.webdriver.chrome.options import Options
from os import environ, getenv


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Chooce lang")
    parser.addoption('--build', action='store', default='4K Autotest',
                     help="Build name for lambdatest")

@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_langeages': user_language})
    browser = webdriver.Chrome(options=options, keep_alive=True)
    browser.implicitly_wait(20)
    browser.set_page_load_timeout(20)
    browser.set_script_timeout(20)
    browser.command_executor.set_timeout(20)

    yield browser

    browser.quit()


if USE_LAMBDATEST := getenv('USE_LAMBDATEST', False):
    username = environ['LT_USERNAME']
    access_key = environ['LT_ACCESS_KEY']

    @pytest.fixture(scope="function")
    def browser(request):
        desired_caps = {
            "build": request.config.getoption("build"),  # Change your build name here
            "name": request.node.nodeid,  # Change your test name here
            "platform": 'Windows 10',  # Change your OS version here
            "browserName": 'Chrome',  # Change your browser here
            "resolution": '1440x900',  # Change your resolution here
            "video": 'true',
            "console": 'true',  # Enable or disable console logs
            "network": 'false',  # Enable or disable network logs
            "idleTimeout": "20",
            "geoLocation": "US",
        }  # Generate capabilites from here: https://www.lambdatest.com/support/docs/selenium-automation-capabilities/

        RemoteConnection.reset_timeout()  # disable timeout to connect
        browser = webdriver.Remote(
            command_executor=f"https://{username}:{access_key}@hub.lambdatest.com/wd/hub",
            desired_capabilities=desired_caps,
            keep_alive=True)
        browser.implicitly_wait(20)
        browser.set_page_load_timeout(20)
        browser.set_script_timeout(20)
        browser.command_executor.set_timeout(20)  # enable timeout for tests

        yield browser

        def fin():
            if request.node.rep_call.failed:
                browser.execute_script("lambda-status=failed")
            else:
                browser.execute_script("lambda-status=passed")
                browser.quit()
        request.addfinalizer(fin)


    @pytest.hookimpl(tryfirst=True, hookwrapper=True)
    def pytest_runtest_makereport(item, call):
        # this sets the result as a test attribute for LambdaTest reporting.
        # execute all other hooks to obtain the report object
        outcome = yield
        rep = outcome.get_result()

        # set an report attribute for each phase of a call, which can
        # be "setup", "call", "teardown"
        setattr(item, "rep_" + rep.when, rep)
