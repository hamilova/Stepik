import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption("--language", action="store", default="en", help="Specify the language for the test page")

@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("--language")
    options = webdriver.ChromeOptions()
    options.add_experimental_option("prefs", {"intl.accept_languages": language})
    browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit()



def item_contains_add_to_cart_button(browser):
    link = "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)


