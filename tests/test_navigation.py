"""
These tests cover the navigation to ZIL/USDT pair page.
"""
from pages.markets import ExchangeMarketsPage
from pages.pair import TradePairPage


def test_by_nav_usdt(browser):
    # Initialize market page object
    markets_page = ExchangeMarketsPage(browser)
    pair_page = TradePairPage(browser)

    # @Given the markets page is displayed
    markets_page.load()
    assert 'markets' in markets_page.url(), "Markets page not accessible"

    # @When the user clicks UI to get into ZIL/USDT page
    # Verify the default market tab is set to 'Spot'
    assert 'Spot' in markets_page.spot_tab(), "Spot market tab is not active"
    # Find and click USDT nav menu
    markets_page.usdt_nav()
    # Find and click ZIL/USDT pair item
    markets_page.zil_pair()

    # @Then the toggle menu on top of the redirected page refers to 'ZIL/USDT'
    assert 'ZIL/USD' in pair_page.top_pair(), "The pair not found on toggle menu"
    # @And the page contains 'ZIL_USDT' in its url path
    assert 'ZIL_USD' in pair_page.page_url(), "The pair URL not found"
    # @And the page title contains 'ZIL/USDT'
    assert 'ZIL/USD' in pair_page.page_title(), "The pair not found on page title"


def test_by_nav_all(browser):
    # Initialize market page object
    markets_page = ExchangeMarketsPage(browser)
    pair_page = TradePairPage(browser)

    # @Given the markets page is displayed
    markets_page.load()
    assert 'markets' in markets_page.url(), "Markets page not accessible"

    # @When the user clicks UI to get into ZIL/USDT page
    # Verify the default market tab is set to 'Spot'
    assert 'Spot' in markets_page.spot_tab(), "Spot market tab is not active"
    # Find and click All nav menu
    markets_page.all_nav()
    # Find and click ZIL/USDT pair item
    markets_page.zil_pair()

    # @Then the toggle menu on top of the redirected page refers to 'ZIL/USDT'
    assert 'ZIL/USD' in pair_page.top_pair(), "The pair not found on toggle menu"
    # @And the page contains 'ZIL_USDT' in its url path
    assert 'ZIL_USD' in pair_page.page_url(), "The pair URL not found"
    # @And the page title contains 'ZIL/USDT'
    assert 'ZIL/USD' in pair_page.page_title(), "The pair not found on page title"


def test_by_nav_favorites(browser):
    # Initialize market page object
    markets_page = ExchangeMarketsPage(browser)
    pair_page = TradePairPage(browser)

    # @Given the markets page is displayed
    markets_page.load()
    assert 'markets' in markets_page.url(), "Markets page not accessible"

    # @When the user clicks UI to get into ZIL/USDT page
    # Verify the default market tab is set to 'Spot'
    assert 'Spot' in markets_page.spot_tab(), "Spot market tab is not active"
    # Move into All section, find and click favorite star icon to add the pair to the favorites
    markets_page.all_nav()
    markets_page.add_favorite()
    # Find and click Favorites nav menu
    markets_page.fav_nav()
    # Find and click ZIL/USDT pair item
    markets_page.zil_pair()

    # @Then the toggle menu on top of the redirected page refers to 'ZIL/USDT'
    assert 'ZIL/USD' in pair_page.top_pair(), "The pair not found on toggle menu"
    # @And the page contains 'ZIL_USDT' in its url path
    assert 'ZIL_USD' in pair_page.page_url(), "The pair URL not found"
    # @And the page title contains 'ZIL/USDT'
    assert 'ZIL/USD' in pair_page.page_title(), "The pair not found on page title"