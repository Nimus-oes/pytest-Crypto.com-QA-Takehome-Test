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
    COOKIES = (By.CSS_SELECTOR, "[title='Accept Cookies']")
    SPOT_TAB = (By.CSS_SELECTOR, "button[class*='e-button--medium is-text active']")
    USDT_NAV = (By.XPATH, "//div[@class='e-tabs__nav-item']/span[text()='USDT']")
    ALL_NAV = (By.XPATH, "//div[@class='e-tabs__nav-item']/span[text()='All']")
    FAVORITES_NAV = (By.XPATH, "//div[@class='e-tabs__nav-item']/span[text()='Favorites']")
    FAVORITES_ICON = (By.XPATH, "//*[name()='svg' and following-sibling::div/a[@href='/exchange/trade/ZIL_USDT']]")
    CATEGORIES_TOGGLE = (By.XPATH, "//div[@class='text']")
    ZIL_USDT_CATEGORY = (By.XPATH, "//div[@class='category'][contains(., 'L1/L2/Polkadot Parachains')]")
    ZIL_USDT_PAIR_MAIN = (By.XPATH, "//a[@href='/exchange/trade/ZIL_USDT'][.//span[@class='base'][text()='ZIL']]")
    TOP_SEARCH_ICON = (By.XPATH, "//*[name()='svg' and @class='e-icon e-icon-search']")
    TOP_SEARCH_ALL = (By.XPATH, "//div[@class='e-tabs tabs']/div/div[@class='e-tabs__nav-item active']/span")
    TOP_SEARCH_SPOT = (By.XPATH, "//div[@class='e-tabs__nav-item spot-beta-tab-item']/span")
    ZIL_USDT_PAIR_SEARCH = (By.XPATH, "//div[@class='group-item']/a[@href='/exchange/trade/ZIL_USDT']/div[text()='ZIL/USDT']")
    TRADE_HEADER_DESKTOP = (By.XPATH, "//button[@class='link-btn e-button e-button--primary e-button--default is-text'][contains(., 'Trade')]")
    SPOT_HEADER_DESKTOP = (By.XPATH, "//div[@class='sub-menu']/a[@href='/exchange/trade?type=spot']")
    BURGER_MENU = (By.XPATH, "//*[name()='svg' and @class='e-icon e-icon-burger pointer']")
    TRADE_HEADER_MOBILE = (By.XPATH, "//span[@class='menu-name' and text()='Trade']")
    SPOT_HEADER_MOBILE = (By.XPATH, "//span[@class='sub-menu-name' and text()='Spot']")
    MOBILE_MENU = (By.CLASS_NAME, "mobile-menu")
    SPOT_FOOTER_DESKTOP = (By.XPATH, "//a[@href='/exchange/trade?type=spot' and @class='sub-title']")

    # Initializer
    def __init__(self, browser):
        self.browser = browser

    #----------------MARKETS PAGE MAIN SECTION----------------#
    # Set the window size to mobile
    def set_mobile_window(self):
        self.browser.set_window_size(360, 800)

    # Load the base page - crypto.com/exchange/markets
    def load(self):
        self.browser.get(self.URL)

    # Dismiss the cookie window
    def cookies(self):
        WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(self.COOKIES))
        ck = self.browser.find_element(*self.COOKIES)
        ck.send_keys(Keys.RETURN)

    # Resources to verify the base page url
    def url(self):
        return self.browser.current_url

    # Resources to verify the default market of base page is set to Spot
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

    # Find and click Favorites navigation menu
    def fav_nav(self):
        fav = self.browser.find_element(*self.FAVORITES_NAV)
        self.browser.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'center'});", fav)
        try:
            WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(self.FAVORITES_NAV))
        except:
            time.sleep(3)
        fav.click()

    # Find and click favorite icon next to ZIL/USDT pair to add to favorites
    def add_to_favorites(self):
        star = self.browser.find_element(*self.FAVORITES_ICON)
        self.browser.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'center'});", star)
        time.sleep(2)
        star.click()

    # Find and click ZIL/USDT pair item from the list on markets page
    def zil_pair_main(self):
        zil = self.browser.find_element(*self.ZIL_USDT_PAIR_MAIN)
        zil.send_keys(Keys.RETURN)

    #----------------TOP SEARCH SECTION----------------#
    # Find and click the top search icon
    def top_search_icon(self):
        ts = self.browser.find_element(*self.TOP_SEARCH_ICON)
        ActionChains(self.browser).move_to_element(ts).perform()

    # Resources to verify the 'All' market tab in the top search section
    def top_search_all(self):
        market = self.browser.find_element(*self.TOP_SEARCH_ALL)
        return market.text

    # Find and click Spot market tab from the top search section
    def top_search_spot(self):
        spot = self.browser.find_element(*self.TOP_SEARCH_SPOT)
        spot.click()

    # Find and click ZIL/USDT pair item from the top search section
    def zil_pair_search(self):
        zil = self.browser.find_element(*self.ZIL_USDT_PAIR_SEARCH)
        zil.click()

    #----------------HEADER NAV SECTION----------------#
    # Find and click Trade header nav from desktop
    def header_nav_trade_desktop(self):
        trade = self.browser.find_element(*self.TRADE_HEADER_DESKTOP)
        ActionChains(self.browser).move_to_element(trade).perform()

    # Find and click Spot sub header under Trade from desktop
    def header_nav_spot_desktop(self):
        spot = self.browser.find_element(*self.SPOT_HEADER_DESKTOP)
        spot.click()

    # Find and click burger menu icon from mobile
    def header_burger_mobile(self):
        burger = self.browser.find_element(*self.BURGER_MENU)
        burger.click()
        WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(self.TRADE_HEADER_MOBILE))

    # Find and click Trade header nav from mobile
    def header_nav_trade_mobile(self):
        trade = self.browser.find_element(*self.TRADE_HEADER_MOBILE)
        trade.click()
        WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(self.SPOT_HEADER_MOBILE))

    # Find and click Spot sub header under Trade from mobile
    def header_nav_spot_mobile(self):
        spot = self.browser.find_element(*self.SPOT_HEADER_MOBILE)
        spot.click()
