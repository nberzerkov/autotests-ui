import pytest
from playwright.sync_api import expect, Page

login_page = 'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login'
email = 'user.name@gmail.com'
password = 'password'

@pytest.mark.regression
@pytest.mark.authorization
def test_wrong_email_or_password_authorization(chromium_page: Page):
        chromium_page.goto(login_page)

        email_input = chromium_page.get_by_test_id('login-form-email-input').locator('input')
        email_input.fill(email)

        password_input = chromium_page.get_by_test_id('login-form-password-input').locator('input')
        password_input.fill(password)

        login_btn = chromium_page.get_by_test_id('login-page-login-button')
        login_btn.click()

        wrong_email_or_password_alert = chromium_page.get_by_test_id('login-page-wrong-email-or-password-alert')
        expect(wrong_email_or_password_alert).to_be_visible()
        expect(wrong_email_or_password_alert).to_have_text("Wrong email or password")
