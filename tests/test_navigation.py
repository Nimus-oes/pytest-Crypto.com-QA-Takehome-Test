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
    # (1) Dismiss the cookies window
    # (2) Verify the base page url contains 'markets'
    # (3) Verify the default market tab is set to 'Spot'
    markets_page.verify_base_page()

    # @When the user clicks UI to get into ZIL/USDT page
    # (1) Find and click the navigation menu
    if nav == 'USDT':
        markets_page.usdt_nav()
    elif nav == 'All':
        markets_page.all_nav()
    elif nav == 'Favorites':
        # Move into All section first
        markets_page.all_nav()
        # Then find and click favorite star icon to add the pair to the favorites
        markets_page.add_favorite()
        # And move into Favorites section
        markets_page.fav_nav()
    # (2) Find and click ZIL/USDT pair item
    markets_page.zil_pair_main()

    # @Then the toggle menu on top of the redirected page refers to 'ZIL/USDT'
    # @And the page contains 'ZIL_USDT' in its url path
    # @And the page title contains 'ZIL/USDT'
    pair_page.verify_pair_page()


@pytest.mark.parametrize('market', ['All', 'Spot'])
def test_by_search_section(browser, market):
    # Initialize market page object
    markets_page = ExchangeMarketsPage(browser)
    pair_page = TradePairPage(browser)

    # @Given the markets page is displayed
    # (1) Dismiss the cookies window
    # (2) Verify the base page url contains 'markets'
    # (3) Verify the default market tab is set to 'Spot'
    markets_page.verify_base_page()

    # @When the user clicks UI to get into ZIL/USDT page
    # (1) Find and click search icon on top
    markets_page.top_search_icon()
    # (2) Find and click the market tab
    if market == 'All':
        # Verify the default market tab is set to 'All'
        assert 'All' in markets_page.top_search_all(), "All market tab is not set to default in search section"
    elif market == 'Spot':
        # Find and click the Spot market tab
        markets_page.top_search_spot()
    # (3) Find and click ZIL/USDT pair item
    markets_page.zil_pair_search()

    # @Then the toggle menu on top of the redirected page refers to 'ZIL/USDT'
    # @And the page contains 'ZIL_USDT' in its url path
    # @And the page title contains 'ZIL/USDT'
    pair_page.verify_pair_page()


def test_by_header_nav(browser):
    pass


def test_by_footer_nav(browser):
    pass