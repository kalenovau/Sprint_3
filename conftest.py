import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import links


@pytest.fixture(scope= 'function')
def driver():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
    driver.get(links.main_link)
    yield driver
    driver.quit()
