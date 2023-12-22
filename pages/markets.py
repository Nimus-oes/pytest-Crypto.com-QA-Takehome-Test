"""
This module contains ExchangeMarketsPage,
the page object for the markets page of Crypto.com Exchange
"""


class ExchangeMarketsPage:
    # Base Page URL
    # This page is accessible from certain countries only. VPN required.
    URL = 'https://www.crypto.com/exchange/markets'

    # Locators
    USDT_NAV = ()
    ALL_NAV = ()
    FAVORITES_NAV = ()
    CATEGORIES_TOGGLE = ()
    ZIL_USDT_CATEGORY = ()
    ZIL_USDT_PAIR_BANNER = ()
    TOP_SEARCH = ()
    TOP_SEARCH_SPOT = ()
    ZIL_USDT_PAIR_SEARCH = ()
    BURGER_MEU = ()
    TRADE_HEADER_MOBILE = ()
    SPOT_HEADER_MOBILE = ()
    TRADE_HEADER_DESKTOP = ()
    SPOT_HEADER_DESKTOP = ()
    TRADE_FOOTER_MOBILE = ()
    SPOT_FOOTER_MOBILE = ()
    TRADE_FOOTER_DESKTOP = ()
    SPOT_FOOTER_DESKTOP = ()

    # Initializer
    def __init__(self, browser):
        self.browser = browser

    # Load the base page - crypto.com/exchange/markets
    def load(self):
        self.browser.get(self.URL)

    # Resources required to verify the base page
    def url(self):
        return self.browser.current_url

    # Click the found element
    def click(self):
        pass

