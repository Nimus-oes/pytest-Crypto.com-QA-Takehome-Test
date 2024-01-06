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


# Common steps for verifying the base page
def verify_base_page(markets_page):
    # @Given the markets page is displayed
    markets_page.load()
    # (1) Dismiss the cookies window
    markets_page.cookies()
    # (2) Verify the base page url contains 'markets'
    assert 'markets' in markets_page.url(), "Markets page not accessible"
    # (3) Verify the default market tab is set to 'Spot'
    assert 'Spot' in markets_page.spot_tab(), "Spot market tab is not active"


# Common steps for verifying the pair page
def verify_pair_page(pair_page):
    # @Then the toggle menu on top of the redirected page refers to 'ZIL/USDT'
    assert 'ZIL/USDT' in pair_page.top_pair('verify'), "The pair not found on toggle menu"
    # @And the page contains 'ZIL_USDT' in its url path
    assert 'ZIL_USDT' in pair_page.page_url(), "The pair URL not found"
    # @And the page title contains 'ZIL/USDT'
    assert 'ZIL/USDT' in pair_page.page_title(), "The pair not found on page title"


@pytest.mark.nav
@pytest.mark.parametrize('size', ['desktop', 'mobile'])
@pytest.mark.parametrize('nav', ['USDT', 'All', 'Favorites'])
def test_by_nav_items(browser, nav, size):
    # Initialize page objects
    markets_page = ExchangeMarketsPage(browser)
    pair_page = TradePairPage(browser)

    # Test both desktop and mobile browsers. Default browser set in the fixture is desktop.
    if size == 'mobile':
        markets_page.set_mobile_window()

    # @Given the markets page is displayed
    verify_base_page(markets_page)

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
        markets_page.add_to_favorites()
        # And move into Favorites section
        markets_page.fav_nav()
    # (2) Find and click ZIL/USDT pair item
    markets_page.zil_pair_main()

    # @Then the page is redirected to 'ZIL/USDT'
    verify_pair_page(pair_page)


# Desktop only test
@pytest.mark.search
@pytest.mark.parametrize('market', ['All', 'Spot'])
def test_by_search_section(browser, market):
    # Initialize page objects
    markets_page = ExchangeMarketsPage(browser)
    pair_page = TradePairPage(browser)

    # @Given the markets page is displayed
    verify_base_page(markets_page)

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

    # @Then the page is redirected to 'ZIL/USDT'
    verify_pair_page(pair_page)


@pytest.mark.header
@pytest.mark.parametrize('size', ['desktop', 'mobile'])
@pytest.mark.parametrize('nav', ['USDT', 'Favorites'])
def test_by_header_spot(browser, nav, size):
    # Initialize page objects
    markets_page = ExchangeMarketsPage(browser)
    pair_page = TradePairPage(browser)

    if size == 'mobile':
        markets_page.set_mobile_window()

    # @Given the markets page is displayed
    verify_base_page(markets_page)

    # @When the user clicks UI to get into ZIL/USDT page
    if size == 'desktop':
        # Find and click Trade header nav menu
        markets_page.header_nav_trade_desktop()
        # Find and click Spot sub header menu under Trade
        markets_page.header_nav_spot_desktop()
    else:
        # Find and click the burger menu icon
        markets_page.header_burger_mobile()
        # Find and click the Trade header nav
        markets_page.header_nav_trade_mobile()
        # Find and click the Spot sub header menu under Trade
        markets_page.header_nav_spot_mobile()
    # Find and click the toggle menu on top to change the pair item
    pair_page.top_pair('select')
    # Find and click the USDT navigation tab
    pair_page.usdt_nav()
    if nav == 'Favorites':
        # Find and click favorite star icon to add the pair to the favorites
        pair_page.add_to_favorites()
        # Find and click the Favorites navigation tab
        pair_page.fav_nav()
    # Find and click ZIL/USDT pair item
    pair_page.zil_pair_toggle()

    # @Then the page is redirected to 'ZIL/USDT'
    verify_pair_page(pair_page)
