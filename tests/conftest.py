import pytest
from playwright.sync_api import sync_playwright, Page

@pytest.fixture # по умолчанию scope будет function если не пишем "()"
def chromium_page() -> Page:
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser.new_page()
