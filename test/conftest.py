import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service


@pytest.fixture(scope='module')
def driver():
    CHROME_DRIVER_PATH = './msedgedriver.exe'
    service = Service(executable_path=CHROME_DRIVER_PATH)
    options = webdriver.EdgeOptions()
    browser = webdriver.Edge(service=service, options=options)

    yield browser

    browser.close()