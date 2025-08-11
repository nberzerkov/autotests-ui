import pytest
from playwright.sync_api import Page, Playwright

registration_url = 'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration'
courses_url = 'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses'
email_data = 'user.name@gmail.com'
username_data = 'username'
password_data = "password"

@pytest.fixture
def chromium_page(playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=False)
    yield browser.new_page()
    browser.close()

@pytest.fixture(scope='session')
def initialize_browser_state(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto(registration_url)

    email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    email_input.fill(email_data)

    username_input = page.get_by_test_id('registration-form-username-input').locator('input')
    username_input.fill(username_data)

    password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    password_input.fill(password_data)

    registration_btn = page.get_by_test_id('registration-page-registration-button')
    registration_btn.click()

    context.storage_state(path="browser-state.json")
    browser.close()

@pytest.fixture
def chromium_page_with_state(initialize_browser_state, playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state="browser-state.json")
    yield context.new_page()
    browser.close()
