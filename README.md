# Crypto.com-QA-Takehome-Test-pytest

## Test Target
Navigating to ZIL/USDT page from crypto.com/exchange/markets  
&nbsp;
## Test Scenario
This test suite follows the Behavior Driven Development process
1. Given: the markets page is displayed
2. When: the user clicks UI to get into ZIL/USDT page
   - The test can be separated into multiple test cases as per the different entry points
3. Then: the redirected page contains 'ZIL_USDT' in its url path
4. And: the page title contains 'ZIL/USDT'
5. And: the toggle menu on top of the page refers to 'ZIL/USDT  
&nbsp;
## Test Design Pattern
Page Object Model (POM) design pattern is applied
  - `pages` contains the page objects for the markets and spot pair pages
  - `tests` contains the shared fixtures and the test cases  
&nbsp;
## Tech Stack
- Python 3
- pytest
- Selenium
- Chrome WebDriver  
&nbsp;
## Supported Browser
- Google Chrome  
&nbsp;
## Test Cases (Total 12)
- `test_by_nav_items()` 
  1. By **USDT** navigation menu on desktop
  2. By **USDT** navigation menu on mobile
  3. By **All** navigation menu on desktop
  4. By **All** navigation menu on mobile
  5. By **Favorites** navigation menu on desktop
  6. By **Favorites** navigation menu on mobile  
  &nbsp;  
  ![Test by navigation items](/.screenshots/test_by_nav_items.png?raw=true)  
  &nbsp;
- `test_by_search_section()`
  1. By top **search** section > **All** market tab on desktop
  2. By top **search** section > **Spot** market tab on desktop  
&nbsp;  
![Test by search section](/.screenshots/test_by_search_section.png?raw=true)  
&nbsp;
- `test_by_header_spot()`
  1. By **Trade** header > **Spot** sub header > **USDT** navigation menu on desktop 
  2. By **burger** menu > **Trade** header > **Spot** sub header > **USDT** navigation menu on mobile
  3. By **Trade** header > **Spot** sub header > **Favorites** navigation menu on desktop
  4. By **burger** menu > **Trade** header > **Spot** sub header > **Favorites** navigation menu on mobile  
&nbsp;  
![Test by header](/.screenshots/test_by_header_desktop.png?raw=true)  
![Test by header](/.screenshots/test_by_header_mobile.png?raw=true)  
![Test by header](/.screenshots/pair_toggle.png?raw=true)  
&nbsp;
## Limits
- This test suite is specific to English language. Other language pages are not supported.
- This test suite is specific to ZIL/USDT trade pair only, and it does **not** cover any other pairs. 
- There are two ways to access favorites items for testing: (1) logging into an account and accessing its favorite items, (2) adding the item to favorites on the spot without login and accessing the favorites. This test suite does not cover the option 1.
- The test suite does not cover the 'Categories' option due to the technical issue that fails to show dropdown content.
- The test suite does not cover the footer Trade > Spot option due to the spot page inaccessible issue  
&nbsp;
## Setting Up the Project
### Prerequisites
Make sure these are already installed in your system
- Python 3
- pip
- Chrome WebDriver  
### Installing the Repo and Dependencies
**Step 1**: Open your terminal and navigate to the directory where you want to clone this repository
```
cd path/to/your/directory
```
**Step 2**: Clone this repository and navigate to the repository directory  
This might require your GitHub username and personal access tokens.
```
git clone https://github.com/Nimus-oes/Crypto.com-QA-Takehome-Test.git
```
```
cd Crypto.com-QA-Takehome-Test
```
**Step 3**: Create a virtual environment
```
python3 -m venv .venv
```
**Step 4**: Activate the virtual environment
```
source .venv/bin/activate
```
**Step 5** : Install the required packages from the cloned repository
```
pip install -r requirements.txt
```  
&nbsp;
## How to Run the Tests
### Run all tests in the test suite
```
python -m pytest
```  
### Run tests by entry points
The test suite is classified into three marks depending on their positions on the page: `nav`, `search`, and `header`
- Tests by navigation items (6 test cases)
```
python -m pytest -m nav
```
- Tests by search section on top of the page (2 test cases)
```
python -m pytest -m search
```
- Tests by Trade > Spot menu on the header (4 test cases)
```
python -m pytest -m header
```
### Run all tests and save the report in html
```
python -m pytest --html={report_name}.html
```
### Run tests by entry points and save the report in html
Replace `{mark}` with `nav`, `search`, or `header`
```
python -m pytest -m {mark} --html={report_name}.html
```
### Run tests in parallel
```
python -m pytest -n {number_of_threds}
```  
&nbsp;
___  
&nbsp;
Below is the log for learnings and challenges that I had during this test development.  
&nbsp;
## How to Handle ElementNotInteractableException
During the test development, I found many errors related to Element Not Interactable Exception whenever the browser tries to interact with the elements. There are three major solutions to tackle this exception.
1. **Explicitly wait for the element to be interactable. Try adding more conditions for the wait if one is not enough.**
```
from selenium.webdriver.support import expected_conditions as EC
WebDriverWait(driver, 10).until(EC.element_to_be_clickable(ELEMENT_LOCATOR))
```
```
from selenium.webdriver.support import expected_conditions as EC
WebDriverWait(driver, 10).until(EC.visibility_of_element_located(ELEMENT_LOCATOR) and EC.element_to_be_clickable(ELEMENT_LOCATOR))
```
2. **Scroll the element into viewport. If the element is not visible enough due to the position on the page, scroll it into the center of viewport.**
```
driver.execute_script("arguments[0].scrollIntoView();", element)
```
```
driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'center'});", star)
```
3. **Try different types of click method.**
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
&nbsp;
## How to Find an SVG Element with XPath
In order to interact with an SVG element via XPath in Selenium, `name()` or `local-name()` method should be called. 
```
//*[name()='svg' and query]
```
```
//*[local-name()='svg' and query]
```   
&nbsp;
## Challenges and Solutions
1. Markets page is not accessible from my location, South Korea presumably due to the geo restrictions
> **Solution**: Used VPN for testing. This resolved the access issue with Chrome browser  
> **Remaining issue**: Access issue still remains with Firefox browser and headless mode in both Chrome and Firefox even with VPN.
2. ElementNotInteractableException raised when clicking ZIL/USDT pair item
> **Solution**: Clicked the pair item with send_keys() method instead of click()
3. ElementNotInteractableException raised when clicking favorites star icon
> **Solution**: After scrolling the element into viewport, hard slept for 2 seconds for the element to be interactable. Although hard sleep is not recommended for efficient testing, there was no workable solution I could find other than this (explicit wait didn't work for this element)
4. Categories dropdown menu is not showing when clicked or mouse hovered
> **Solution**: No solution found yet. 
> 
> Tried explicit wait, hard sleep, ActionChain, and JavaScript to trigger the hover effect but none of it worked.
5. When tried to access footer Trade > Spot menu, the newly opened page is redirected to crypto.com/exchange again. Spot page is not accessible with footer navigation.
> **Solution**: No solution found yet. Tried to change the url again in the new window but didn't work.  
> 
&nbsp;
