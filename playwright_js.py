from playwright.sync_api import sync_playwright

login_page = 'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login'

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto(login_page, wait_until='networkidle')


    my_name = 'Nikita Enduraev Automation'
    page.evaluate(
    """
    (text) => {
        const title = document.getElementById('authentication-ui-course-title-text');
        title.textContent = text
    }   
    
    """,
    my_name
    )

    page.wait_for_timeout(2000)
