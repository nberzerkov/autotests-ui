import pytest
from playwright.sync_api import expect

registration_url = 'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration'
courses_url = 'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses'
email_data = 'user.name@gmail.com'
username_data = 'username'
password_data = "password"


@pytest.mark.regression
@pytest.mark.courses
def test_empty_courses_list(chromium_page_with_state):
    chromium_page_with_state.goto(courses_url)

    courses_toolbar_title = chromium_page_with_state.get_by_test_id('courses-list-toolbar-title-text')
    expect(courses_toolbar_title).to_be_visible()
    expect(courses_toolbar_title).to_have_text('Courses')

    courses_empty_icon = chromium_page_with_state.get_by_test_id('courses-list-empty-view-icon')
    expect(courses_empty_icon).to_be_visible()

    courses_empty_title_text = chromium_page_with_state.get_by_test_id('courses-list-empty-view-title-text')
    expect(courses_empty_title_text).to_be_visible()
    expect(courses_empty_title_text).to_have_text('There is no results')

    courses_empty_description_text = chromium_page_with_state.get_by_test_id('courses-list-empty-view-description-text')
    expect(courses_empty_description_text).to_be_visible()
    expect(courses_empty_description_text).to_have_text('Results from the load test pipeline will be displayed here')
