"""
This module contains TradePairPage,
the page object for the spot pair page of Crypto.com Exchange
"""


class TradePairPage:
    # Locators
    TOP_PAIR_TOGGLE = ()
    USDT_NAV = ()
    FAVORITES_NAV = ()
    ZIL_USDT_PAIR = ()

    # Initializer
    def __init__(self, browser):
        self.browser = browser

    # Resources required to verify the page title contains 'ZIL/USDT'
    def page_title(self):
        return ''

    # Resources required to verify the page url contains 'ZIL_USDT'
    def page_url(self):
        return ''

    # Resources required to verify the top toggle menu refers to 'ZIL/USDT'
    def top_pair(self):
        return ''
