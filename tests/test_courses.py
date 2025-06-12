from playwright.sync_api import sync_playwright, expect

registration_url = 'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration'
courses_url = 'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses'
email_data = 'user.name@gmail.com'
username_data = 'username'
password_data = "password"

def test_empty_courses_list():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        page.goto(registration_url)

        email_input = page.get_by_test_id('registration-form-email-input').locator('input')
        email_input.fill(email_data)

        username_input = page.get_by_test_id('registration-form-username-input').locator('input')
        username_input.fill(username_data)

        password_input = page.get_by_test_id('registration-form-password-input').locator('input')
        password_input.fill(password_data)

        registration_btn = page.get_by_test_id('registration-page-registration-button')
        registration_btn.click()

        context.storage_state(path="browser-state.json")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(storage_state="browser-state.json")
        page = context.new_page()

        page.goto(courses_url)

        courses_toolbar_title = page.get_by_test_id('courses-list-toolbar-title-text')
        expect(courses_toolbar_title).to_be_visible()
        expect(courses_toolbar_title).to_have_text('Courses')

        courses_empty_icon = page.get_by_test_id('courses-list-empty-view-icon')
        expect(courses_empty_icon).to_be_visible()

        courses_empty_title_text = page.get_by_test_id('courses-list-empty-view-title-text')
        expect(courses_empty_title_text).to_be_visible()
        expect(courses_empty_title_text).to_have_text('There is no results')

        courses_empty_description_text = page.get_by_test_id('courses-list-empty-view-description-text')
        expect(courses_empty_description_text).to_be_visible()
        expect(courses_empty_description_text).to_have_text('Results from the load test pipeline will be displayed here')
