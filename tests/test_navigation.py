"""
These tests cover the navigation to ZIL/USDT pair page.
The tests follow below behaviors:
    @Given the markets page is displayed
    @When the user clicks UI to get into ZIL/USDT page
    @Then the toggle menu on top of the redirected page refers to 'ZIL/USDT'
    @And the page contains 'ZIL_USDT' in its url path
    @And the page title contains 'ZIL/USDT'
"""
from pages.markets import ExchangeMarketsPage
from pages.pair import TradePairPage
import pytest


@pytest.mark.parametrize('nav', ['USDT', 'All', 'Favorites'])
def test_by_nav_items(browser, nav):
    # Initialize market page object
    markets_page = ExchangeMarketsPage(browser)
    pair_page = TradePairPage(browser)

    # @Given the markets page is displayed
    # (1) Verify the base page url contains 'markets'
    # (2) Verify the default market tab is set to 'Spot'
    markets_page.verify_base_page()

    # @When the user clicks UI to get into ZIL/USDT page
    # (1) Find and click the navigation menu
    if nav == 'USDT':
        markets_page.usdt_nav()
    elif nav == 'All':
        markets_page.all_nav()
    elif nav == 'Favorites':
        # Move into All section first
        # Then find and click favorite star icon to add the pair to the favorites
        # And move into Favorites section
        markets_page.all_nav()
        markets_page.add_favorite()
        markets_page.fav_nav()
    # (2) Find and click ZIL/USDT pair item
    markets_page.zil_pair()

    # @Then the toggle menu on top of the redirected page refers to 'ZIL/USDT'
    # @And the page contains 'ZIL_USDT' in its url path
    # @And the page title contains 'ZIL/USDT'
    pair_page.verify_pair_page()


def test_by_search_section(browser):
    pass


def test_by_header_nav(browser):
    pass


def test_by_footer_nav(browser):
    pass