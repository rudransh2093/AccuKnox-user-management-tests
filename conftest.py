# conftest.py
import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # <-- headless=False opens the browser
        page = browser.new_page()
        yield page
        browser.close()
