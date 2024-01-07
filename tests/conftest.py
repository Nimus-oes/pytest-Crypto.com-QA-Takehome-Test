"""
This module contains shared fixtures.
This test does not support headless browsers due to the access restriction over VPN
"""

import pytest
import selenium.webdriver


@pytest.fixture
def browser():
    b = selenium.webdriver.Chrome()
    # The default browser size is desktop
    b.set_window_size(1200, 891)
    yield b
    b.quit()
