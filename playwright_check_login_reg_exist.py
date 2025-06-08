from playwright.sync_api import sync_playwright, expect

login_page = 'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login'

with sync_playwright() as playwright:
    browser_chromium = playwright.chromium.launch(headless=False)
    page = browser_chromium.new_page()

    # Страница авторизации
    page.goto(login_page)

    login_email_input = page.get_by_test_id('login-form-email-input').locator('input')
    expect(login_email_input).to_be_visible()

    login_password_input = page.get_by_test_id('login-form-password-input').locator('input')
    expect(login_password_input).to_be_visible()

    login_btn = page.get_by_test_id('login-page-login-button')
    expect(login_btn).to_be_visible()

    # Страница регистрации
    registration_btn = page.get_by_test_id('login-page-registration-link')
    registration_btn.click()

    reg_email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    expect(reg_email_input).to_be_visible()

    reg_password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    expect(reg_password_input).to_be_visible()

    registration_btn = page.get_by_test_id('registration-page-registration-button')
    expect(registration_btn).to_be_visible()