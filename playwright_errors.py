from playwright.sync_api import sync_playwright, expect

login_page = 'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login'

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto(login_page, wait_until='networkidle')

    # h6 = page.get_by_test_id('authentication-ui-course-title-text')
    # expect(h6).to_be_visible()

    # login_btn = page.get_by_test_id('login-page-login-button')
    # login_btn.fill('unknown')

    # page.evaluate(
    #     """
    #         const title = document.getElementById('authentication-ui-course-title-text');
    #         title.textContent = 'Hello';
    #     """
    # )

