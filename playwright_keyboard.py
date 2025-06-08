from time import sleep
from playwright.sync_api import sync_playwright, expect

login_page = 'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login'

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto(login_page)

    email_input = page.get_by_test_id('login-form-email-input').locator('input')
    email_input.focus()

    for char in 'user@gmail.com':
        page.keyboard.type(char, delay=200)

    page.keyboard.press("ControlOrMeta+A")
    page.keyboard.press("Backspace")

    page.wait_for_timeout(3000)