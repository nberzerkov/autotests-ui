import pytest
from playwright.sync_api import expect, Page

from pages.create_course_page import CreateCoursePage
from pages.courses_list_page import CoursesListPage

COURSES_URL = 'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses'
CREATE_COURSE_URL = "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create"

@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(courses_list_page: CoursesListPage):
    courses_list_page.visit(COURSES_URL)

    courses_list_page.navbar.check_visible("nikita")
    courses_list_page.sidebar.check_visible()

    courses_list_page.check_visible_courses_title()
    courses_list_page.check_visible_empty_view()
    courses_list_page.check_visible_create_course_btn()

@pytest.mark.courses
@pytest.mark.regression
def test_create_course(create_course_page: CreateCoursePage, courses_list_page: CoursesListPage):
    create_course_page.visit(CREATE_COURSE_URL)

    create_course_page.check_visible_create_course_title()

    create_course_page.check_visible_create_course_disabled_btn()
    create_course_page.check_disabled_create_course_btn()

    create_course_page.check_visible_img_preview_empty_view()

    create_course_page.check_visible_image_upload_view(is_img_uploaded=False)

    create_course_page.check_visible_create_course_form()

    create_course_page.check_visible_exercise_title()
    create_course_page.check_visible_create_exercise_btn()
    create_course_page.check_visible_exercise_empty_view()

    create_course_page.upload_preview_img("./testdata/files/image.png")
    create_course_page.check_visible_image_upload_view(is_img_uploaded=True)

    create_course_page.fill_create_course_form("Playwright", "2 week", "Playwright", "100", "10" )
    create_course_page.check_visible_create_exercise_btn()
    create_course_page.click_create_course_btn()

    courses_list_page.check_visible_courses_title()
    courses_list_page.check_visible_create_course_btn()
    courses_list_page.check_visible_course_card(0, "Playwright", "2 week", "100", "10")
