from playwright.sync_api import sync_playwright, expect

# переменные для удобства
registration_page = 'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration'
email_data = 'user.name@gmail.com'
username_data = 'username'
password_data = "password"

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto(registration_page)

    email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    email_input.fill(email_data)

    username_input = page.get_by_test_id('registration-form-username-input').locator('input')
    username_input.fill(username_data)

    password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    password_input.fill(password_data)

    registration_btn = page.get_by_test_id('registration-page-registration-button')
    registration_btn.click()

    dashboard_text = page.get_by_test_id('dashboard-toolbar-title-text')
    expect(dashboard_text).to_be_visible()
    expect(dashboard_text).to_have_text("Dashboard")
