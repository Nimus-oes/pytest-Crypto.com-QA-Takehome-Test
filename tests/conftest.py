"""
This module contains shared fixtures.
This test does not support headless browsers due to the access restriction over VPN
"""

import pytest
import selenium.webdriver


@pytest.fixture
def browser():
    b = selenium.webdriver.Chrome()
    yield b
    b.quit()
