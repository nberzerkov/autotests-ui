from playwright.sync_api import sync_playwright, expect

registration_page = 'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration'
email_data = 'user.name@gmail.com'
username_data = 'username'
password_data = 'password'

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto(registration_page)

    registration_btn = page.get_by_test_id('registration-page-registration-button')
    expect(registration_btn).to_be_disabled()

    email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    email_input.fill(email_data)

    username_input = page.get_by_test_id('registration-form-username-input').locator('input')
    username_input.fill(username_data)

    password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    password_input.fill(password_data)

    expect(registration_btn).to_be_enabled()
    registration_btn.click()