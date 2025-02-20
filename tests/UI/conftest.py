import pytest
import os
from selene import browser
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from qa_guru_python17_diploma_work.utils import attach
from dotenv import load_dotenv

DEFAULT_BROWSER_NAME = "chrome"
DEFAULT_BROWSER_VERSION = "126.0"


def pytest_addoption(parser):
    parser.addoption("--browser_name", default="chrome")
    parser.addoption("--browser_version", default="126.0")


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope="function", autouse=True)
def setup_browser(request):
    browser_name = request.config.getoption('browser_name') or DEFAULT_BROWSER_NAME
    browser_version = request.config.getoption('browser_version') or DEFAULT_BROWSER_VERSION
    options = Options()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    selenoid_capabilities = {
        "browserName": browser_name,
        "browserVersion": browser_version,
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }

    options.capabilities.update(selenoid_capabilities)

    login = os.getenv('LOGIN')
    password = os.getenv('PASSWORD')

    driver = webdriver.Remote(
        command_executor=f"https://{login}:{password}@selenoid.autotests.cloud/wd/hub",
        options=options)

    browser.config.driver = driver
    browser.config.base_url = 'https://start.ru/'
    browser.config.driver.maximize_window()

    yield browser

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)

    browser.quit()
