# Crypto.com-QA-Takehome-Test

## Test Target
Navigating to ZIL/USDT page from crypto.com/exchange/markets

## Test Methodology
- Behavior Driven Development

## Tech Stack
- Python
- pytest

## Supported Browser
- Google Chrome
- Mozilla Firefox

# Test Scope and Limits
This test suite is specific to ZIL/USDT trade pair only, and it cannot cover any other pairs. 

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
1. [TODO] Create page objects for markets and spot pair page
2. [TODO] Initialize a simple WebDriver instance with fixture and open crypto.com/exchange/markets page with it
3. [TODO] Take one of the entry points to the trade page and implement it with code
   - Locate the 'USDT' navigation menu and click the ZIL/USDT pair item under it
4. [TODO] Verify the redirected page
   - The page contains 'ZIL_USDT' in its url path
   - The page title contains 'ZIL/USDT'
   - The toggle menu on top of the page refers to 'ZIL/USDT'
5. [TODO] Implement other test cases, reusing the common steps