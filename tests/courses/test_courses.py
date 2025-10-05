import re
import pytest
import allure
from pages.courses.create_course_page import CreateCoursePage
from pages.courses.courses_list_page import CoursesListPage
from tools.allure.tags import AllureTag
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory

COURSES_URL = 'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses'
CREATE_COURSE_URL = "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create"

@pytest.mark.courses
@pytest.mark.regression
@allure.tag(AllureTag.COURSES, AllureTag.REGRESSION)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.COURSES)
@allure.story(AllureStory.COURSES)
class TestCourses:
    @allure.title("Check displaying of empty courses list")
    def test_empty_courses_list(self, courses_list_page: CoursesListPage):
        courses_list_page.visit(COURSES_URL)

        courses_list_page.navbar.check_visible("nikita")
        courses_list_page.sidebar.check_visible()

        courses_list_page.toolbar.check_visible()
        courses_list_page.check_visible_empty_view()

    @allure.title("Create course")
    def test_create_course(self, create_course_page: CreateCoursePage, courses_list_page: CoursesListPage):
        create_course_page.visit(CREATE_COURSE_URL)

        create_course_page.toolbar.check_visible(is_create_course_disabled=True)

        create_course_page.img_upload_widget.check_visible(is_img_uploaded=False)

        create_course_page.form.check_visible()

        create_course_page.exercises_toolbar.check_visible()
        create_course_page.check_visible_exercise_empty_view()

        create_course_page.img_upload_widget.upload_preview_img("./testdata/files/image.png")
        create_course_page.img_upload_widget.check_visible(is_img_uploaded=True)

        create_course_page.form.fill(title="Playwright", estimate_time="2 week", description="Playwright",
                                     max_score="100", min_score="10")
        create_course_page.toolbar.check_visible(is_create_course_disabled=False)
        create_course_page.toolbar.click_create_course_btn()

        courses_list_page.toolbar.check_visible()
        courses_list_page.toolbar.check_current_url(re.compile(".*/#/courses"))
        courses_list_page.course_view.check_visible(index=0, title="Playwright", estimate_time="2 week",
                                                    max_score="100", min_score="10")

    @allure.title("Edit course")
    def test_edit_course(self, create_course_page: CreateCoursePage, courses_list_page: CoursesListPage):
        create_course_page.visit(CREATE_COURSE_URL)

        create_course_page.form.check_visible()
        create_course_page.form.fill(title="Playwright", estimate_time="2 week", description="Playwright",
                                     max_score="100", min_score="10")

        create_course_page.img_upload_widget.upload_preview_img("./testdata/files/image.png")
        create_course_page.img_upload_widget.check_visible(is_img_uploaded=True)

        create_course_page.toolbar.click_create_course_btn()

        courses_list_page.check_current_url(re.compile(".*/#/courses"))
        courses_list_page.course_view.check_visible(index=0, title="Playwright", estimate_time="2 week",
                                                    max_score="100", min_score="10")

        courses_list_page.course_view.menu.click_edit(index=0)
        create_course_page.toolbar.check_visible(is_create_course_disabled=False, title_text="Update course")
        create_course_page.form.fill(title="UserCourse", estimate_time="1 week", description="course",
                                     max_score="200", min_score="50")
        create_course_page.toolbar.click_create_course_btn()

        courses_list_page.check_current_url(re.compile(".*/courses"))
        courses_list_page.course_view.check_visible(index=0, title="UserCourse", estimate_time="1 week",
                                                    max_score="200", min_score="50")
