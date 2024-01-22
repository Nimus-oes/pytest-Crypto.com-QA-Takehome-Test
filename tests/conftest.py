"""
This module contains shared fixtures.
This test does not support headless browsers due to the access restriction over VPN
"""

import pytest
import selenium.webdriver
from pages.markets import ExchangeMarketsPage
from pages.pair import TradePairPage


# Create a browser instance for each test case
@pytest.fixture
def browser():
    b = selenium.webdriver.Chrome()
    # The default browser size is desktop
    b.set_window_size(1200, 891)
    yield b
    b.quit()


# Create a Markets page object model instance for each test case
@pytest.fixture()
def markets_page(browser):
    return ExchangeMarketsPage(browser)


# Create a pair page object model instance for each test case
@pytest.fixture()
def pair_page(browser):
    return TradePairPage(browser)
