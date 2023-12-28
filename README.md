# Crypto.com-QA-Takehome-Test

## Test Target
Navigating to ZIL/USDT page from crypto.com/exchange/markets

## Test Methodology
- Behavior Driven Development

## Tech Stack
- Python
- pytest
- Selenium

## Supported Browser
- Google Chrome
- Mozilla Firefox is *not supported* due to markets page access issue

## Test Scope and Limits
- This test suite is specific to ZIL/USDT trade pair only, and it cannot cover any other pairs. 
- There are two ways to access favorites items for testing: (1) logging in to an account and accessing its favorite items, (2) adding the item to favorites and accessing the favorites. This test suite does not cover the option 1.

___

===========================================================

## Step 1: Defining the Behaviors
1. Given: the markets page is displayed
2. When: the user clicks UI to get into ZIL/USDT page
   - The test can be separated into multiple test cases as per the different entry points
3. Then: the redirected page contains 'ZIL_USDT' in its url path
4. And: the page title contains 'ZIL/USDT'
5. And: the toggle menu on top of the page refers to 'ZIL/USDT'

## Step 2: Identifying the Entry Points
There are different UI elements on crypto.com/exchange/markets that users can click on to access the ZIL/USDT page.

- **By 'USDT' nav menu**: Click 'USDT' from the top navigation item > Select ZIL/USDT among the listed pairs
- **By 'All' nav menu**: Click 'All' from the top navigation item > Select ZIL/USDT among the listed pairs
- **By 'Favorites' nav menu**: Click 'Favorites' from the top navigation item > Select ZIL/USDT among the listed pairs (if any)
- **By 'Categories' toggle menu**: Click 'Categories' toggle menu on top > Select 'L1/L2/Polkadot Parachains' > Select ZIL/USDT among the listed pairs
- **By top search menu**: Only when screen width is over 991 px
  - Click search icon on top > The top navigation menu 'All' is already selected > Select ZIL/USDT among the listed pairs 
  - Click search icon on top > Select 'Spot' from the top navigation menu > Select ZIL/USDT among the listed pairs
- **By 'Trade' > 'Spot' header nav menu**:
  - For mobile (340~991 px): Click burger menu on top > Click 'Trade' menu > Select 'Spot' > Click the pair name toggle on top (ex: BTC/USD) > Select 'USDT' from the top navigation menu > Select ZIL/USDT
  - For mobile (340~991 px): Click burger menu on top > Click 'Trade' menu > Select 'Spot' > Click the pair name toggle on top (ex: BTC/USD) > Select 'Favorites' from the top navigation menu > Select ZIL/USDT (if any)
  - For desktop (over 991 px): Click 'Trade' navigation menu on top > Select 'Spot' > Click the pair name toggle on top (ex: BTC/USD) > Select 'USDT' from the top navigation menu > Select ZIL/USDT
  - For desktop (over 991 px): Click 'Trade' navigation menu on top > Select 'Spot' > Click the pair name toggle on top (ex: BTC/USD) > Select 'Favorites' from the top navigation menu > Select ZIL/USDT (if any)
- **By 'Trade' > 'Spot' footer nav menu**:
  - For mobile (under 992 px): Click 'Trade' of the mobile footer menu > Select 'Spot' > Click the pair name toggle on top (ex: BTC/USD) > Select 'USDT' from the top navigation menu > Select ZIL/USDT
  - For mobile (under 992 px): Click 'Trade' of the mobile footer menu > Select 'Spot' > Click the pair name toggle on top (ex: BTC/USD) > Select 'Favorites' from the top navigation menu > Select ZIL/USDT (if any)
  - For desktop (over 991 px): Click 'Spot' under the 'Trade' of the footer menu > Click the pair name toggle on top (ex: BTC/USD) > Select 'USDT' from the top navigation menu > Select ZIL/USDT
  - For desktop (over 991 px): Click 'Spot' under the 'Trade' of the footer menu > Click the pair name toggle on top (ex: BTC/USD) > Select 'Favorites' from the top navigation menu > Select ZIL/USDT (if any)

## Step 3: Designing Test Suite Structure
- `pages` contains the page objects for the markets and spot pair pages
- `tests` contains the shared fixtures and the test cases

## Step 4: Implementing Test Cases
1. Create page objects for markets and spot pair page
2. Initialize a simple WebDriver instance with fixture and open crypto.com/exchange/markets page with it
3. Take one of the entry points to the trade page and implement it with code
   - Locate the 'USDT' navigation menu and click the ZIL/USDT pair item under it
4. Verify the redirected page
   - The page contains 'ZIL_USDT' in its url path
   - The page title contains 'ZIL/USDT'
   - The toggle menu on top of the page refers to 'ZIL/USDT'
5. [TODO] Implement other test cases, reusing the common steps

## How to Handle ElementNotInteractableException
During the test development, I found many errors related to Element Not Interactable Exception whenever the browser tries to interact with the elements. There are three major solutions to tackle this exception.
1. Explicitly wait for the element to be interactable. Try adding more conditions for the wait if one is not enough.
```
from selenium.webdriver.support import expected_conditions as EC
WebDriverWait(driver, 10).until(EC.element_to_be_clickable(ELEMENT_LOCATOR) and EC.element_to_be_clickable(ELEMENT_LOCATOR))
```
2. Scroll the element into viewport. If the element is not visible enough due to the position on the page, scroll it into the center of viewport.
```
driver.execute_script("arguments[0].scrollIntoView();", element)
```
```
driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'center'});", star)
```
3. Try different types of click method.
```
element.click()
```
```
from selenium.webdriver.common.keys import Keys
element.send_keys(Keys.RETURN)
```
```
driver.execute_script("arguments[0].click();", element)
```
```
from selenium.webdriver.common.action_chains import ActionChains
ActionChains(driver).move_to_element(element).click().perform()
```

## How to Find an SVG Element with XPath
In order to interact with an SVG element via XPath in Selenium, `name()` or `local-name()` method should be called. 
```
//*[name()=query]
```
```
//*[local-name()=query]
```

## Challenges and Solutions
1. Markets page is not accessible presumably due to the geo restrictions from South Korea
> **Solution**: Used VPN for testing. This resolved the access issue with Chrome browser, however, the issue still remains with Firefox even with VPN.
2. ElementNotInteractableException raised when clicking ZIL/USDT pair item
> **Solution**: Clicked the pair item with send_keys() method instead of click()
3. ElementNotInteractableException raised when clicking favorites star icon
> **Solution**: After scrolling the element into viewport, hard slept for 2 seconds for the element to be interactable. Although hard sleep is not recommended for efficient testing, there was no workable solution I could find other than this (explicit wait didn't work for this element)
4. Categories dropdown menu is not showing when clicked or mouse hovered
> **Solution**: No solution found yet. 
> 
> Tried explicit wait, hard sleep, ActionChain, and JavaScript to trigger the hover effect but none of it worked.