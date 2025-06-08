from playwright.sync_api import sync_playwright

login_page = 'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login'

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto(login_page)

    registration_link = page.get_by_test_id('login-page-registration-link')
    registration_link.hover()

    page.wait_for_timeout(3000)