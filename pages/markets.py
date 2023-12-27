"""
This module contains ExchangeMarketsPage,
the page object for the markets page of Crypto.com Exchange
"""
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class ExchangeMarketsPage:
    # Base Page URL
    # This page is accessible from certain countries only. VPN required.
    URL = "https://www.crypto.com/exchange/markets"

    # Locators
    SPOT_TAB = (By.CSS_SELECTOR, "button[class*='e-button--medium is-text active']")
    USDT_NAV = (By.XPATH, "//div[@class='e-tabs__nav-item']/span[text()='USDT']")
    ALL_NAV = (By.XPATH, "//div[@class='e-tabs__nav-item']/span[text()='All']")
    FAVORITES_NAV = (By.XPATH, "//div[@class='e-tabs__nav-item']/span[text()='Favorites']")
    FAVORITES_ICON = (By.XPATH, "//*[name()='svg' and following-sibling::div/a[@href='/exchange/trade/ZIL_USDT']]")
    # FAVORITES_ICON = (By.XPATH, "//*[local-name()='svg' and following-sibling::div/a[@href='/exchange/trade/BTC_USD']]/descendant::*[local-name()='use']")
    CATEGORIES_TOGGLE = ()
    ZIL_USDT_CATEGORY = ()
    ZIL_USDT_PAIR_ITEM = (By.XPATH, "//a[@href='/exchange/trade/ZIL_USDT'][.//span[@class='base'][text()='ZIL']]")
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

    # Resources to verify the base page
    def url(self):
        return self.browser.current_url

    # Resources to verify the Spot market tab
    # TODO Add explicit wait here
    def spot_tab(self):
        spot = self.browser.find_element(*self.SPOT_TAB)
        return spot.text

    # Find and click USDT navigation menu
    def usdt_nav(self):
        usdt = self.browser.find_element(*self.USDT_NAV)
        usdt.click()

    # Find and click All navigation menu
    def all_nav(self):
        nav_all = self.browser.find_element(*self.ALL_NAV)
        nav_all.click()

    # Find and click favorite icon to add the pair to favorite section
    def add_favorite(self):
        star = self.browser.find_element(*self.FAVORITES_ICON)
        self.browser.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'center'});", star)
        time.sleep(2)
        star.click()

    # Find and click Favorites navigation menu
    def fav_nav(self):
        fav = self.browser.find_element(*self.FAVORITES_NAV)
        self.browser.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'center'});", fav)
        WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located(self.FAVORITES_ICON))
        fav.click()

    # Find and click ZIL/USDT pair item
    def zil_pair(self):
        zil = self.browser.find_element(*self.ZIL_USDT_PAIR_ITEM)
        zil.send_keys(Keys.RETURN)
