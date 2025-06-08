from playwright.sync_api import sync_playwright, expect

login_page = 'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login'

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto(login_page)

    login_btn = page.get_by_test_id('login-page-login-button')
    expect(login_btn).to_be_disabled()
