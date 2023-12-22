"""
These tests cover the navigation to ZIL/USDT pair page.
"""
from pages.markets import ExchangeMarketsPage
from pages.pair import TradePairPage


def test_open(browser):
    # Initialize market page object
    markets_page = ExchangeMarketsPage(browser)

    # Given the markets page is displayed
    markets_page.load()
    assert 'markets' in markets_page.url()

    # When the user clicks UI to get into ZIL/USDT page
    # Then the redirected page contains 'ZIL_USDT' in its url path
    # And the page title contains 'ZIL/USDT'
    # And the toggle menu on top of the page refers to 'ZIL/USDT'
