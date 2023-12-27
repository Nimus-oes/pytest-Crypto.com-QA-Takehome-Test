"""
This module contains TradePairPage,
the page object for the spot pair page of Crypto.com Exchange
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TradePairPage:
    # Locators
    TOP_PAIR_TOGGLE = (By.CSS_SELECTOR, "div.toggle")
    USDT_NAV = ()
    FAVORITES_NAV = ()
    ZIL_USDT_PAIR = ()

    # Initializer
    def __init__(self, browser):
        self.browser = browser

    # Resources to verify the page title contains 'ZIL/USDT'
    def page_title(self):
        return self.browser.title

    # Resources to verify the page url contains 'ZIL_USDT'
    def page_url(self):
        return self.browser.current_url

    # Resources to verify the top toggle menu refers to 'ZIL/USDT'
    def top_pair(self):
        # Wait for the top toggle menu
        WebDriverWait(self.browser, 10).until(EC.text_to_be_present_in_element(self.TOP_PAIR_TOGGLE, 'ZIL/USD'))
        # After loading all elements, find the element
        toggle = self.browser.find_element(*self.TOP_PAIR_TOGGLE)
        return toggle.text
