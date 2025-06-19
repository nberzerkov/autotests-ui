import pytest
from playwright.sync_api import expect, Page

registration_url = 'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration'
dashboard_url = 'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard'
email_data = 'user.name@gmail.com'
username_data = 'username'
password_data = "password"

@pytest.mark.regression
@pytest.mark.registration
def test_successful_registration(chromium_page: Page):
        chromium_page.goto(registration_url)

        email_input = chromium_page.get_by_test_id('registration-form-email-input').locator('input')
        email_input.fill(email_data)

        username_input = chromium_page.get_by_test_id('registration-form-username-input').locator('input')
        username_input.fill(username_data)

        password_input = chromium_page.get_by_test_id('registration-form-password-input').locator('input')
        password_input.fill(password_data)

        registration_btn = chromium_page.get_by_test_id('registration-page-registration-button')
        registration_btn.click()

        dashboard_title = chromium_page.get_by_test_id('dashboard-toolbar-title-text')
        expect(dashboard_title).to_be_visible()


# @pytest.mark.regression
# @pytest.mark.registration
# def test_successful_registration(chromium_page: Page):
#     with sync_playwright() as p:
#         browser = p.chromium.launch(headless=False)
#         context = browser.new_context()
#         page = context.new_page()
#
#         page.goto(registration_url)
#
#         email_input = page.get_by_test_id('registration-form-email-input').locator('input')
#         email_input.fill(email_data)
#
#         username_input = page.get_by_test_id('registration-form-username-input').locator('input')
#         username_input.fill(username_data)
#
#         password_input = page.get_by_test_id('registration-form-password-input').locator('input')
#         password_input.fill(password_data)
#
#         registration_btn = page.get_by_test_id('registration-page-registration-button')
#         registration_btn.click()
#
#         context.storage_state(path='browser-state.json')
#
#     with sync_playwright() as p:
#         browser = p.chromium.launch(headless=False)
#         context = browser.new_context(storage_state="browser-state.json")
#         page = context.new_page()
#
#         page.goto(dashboard_url)