from playwright.sync_api import Page, expect
from pages.base_page import BasePage

class CoursesListPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        # Заголовок и кнопка создания курса
        self.courses_title = page.get_by_test_id("courses-list-toolbar-title-text")
        self.create_course_btn = page.get_by_test_id("courses-list-toolbar-create-course-button")

        # Пустой блок при отсутствии курсов
        self.empty_view_icon = page.get_by_test_id("courses-list-empty-view-icon")
        self.empty_view_title = page.get_by_test_id("courses-list-empty-view-title-text")
        self.empty_view_description = page.get_by_test_id("courses-list-empty-view-description-text")

        # Карточка курса
        self.course_title = page.get_by_test_id("course-widget-title-text")
        self.course_img = page.get_by_test_id("course-preview-image")
        self.course_max_score = page.get_by_test_id("course-max-score-info-row-view-text")
        self.course_min_score = page.get_by_test_id("course-min-score-info-row-view-text")
        self.course_estimate_time = page.get_by_test_id("course-estimated-time-info-row-view-text")

        # Меню карточки курса
        self.course_menu_btn = page.get_by_test_id("course-view-menu-button")
        self.course_edit_btn = page.get_by_test_id("course-view-edit-menu-item")
        self.course_delete_btn = page.get_by_test_id("course-view-delete-menu-item-text")

    def check_visible_courses_title(self):
        expect(self.courses_title).to_be_visible()
        expect(self.courses_title).to_have_text("Courses")

    def check_visible_create_course_btn(self):
        expect(self.create_course_btn).to_be_visible()

    def click_create_course_btn(self):
        self.create_course_btn.click()

    def check_visible_empty_view(self):
        expect(self.empty_view_icon).to_be_visible()

        expect(self.empty_view_title).to_be_visible()
        expect(self.empty_view_title).to_have_text("There is no results")

        expect(self.empty_view_description).to_be_visible()
        expect(self.empty_view_description).to_have_text("Results from the load test pipeline will be displayed here")

    def check_visible_course_card(
            self, index: int, title: str = "", estimate_time: int = 0, max_score: str = "", min_score: str = ""):
        expect(self.course_title.nth(index)).to_be_visible()
        expect(self.course_title).to_have_text(title)

        expect(self.course_img.nth(index)).to_be_visible()

        expect(self.course_max_score.nth(index)).to_be_visible()
        expect(self.course_max_score.nth(index)).to_have_text(f"Max score: {max_score}")

        expect(self.course_min_score.nth(index)).to_be_visible()
        expect(self.course_min_score.nth(index)).to_have_text(f"Min score: {min_score}")

        expect(self.course_estimate_time.nth(index)).to_be_visible()
        expect(self.course_estimate_time.nth(index)).to_have_text(f"Estimated time: {estimate_time}")

    def click_edit_course(self, index: int):
        expect(self.course_menu_btn.nth(index)).to_be_visible()
        self.course_menu_btn.nth(index).click()

        expect(self.course_edit_btn.nth(index)).to_be_visible()
        self.course_edit_btn.nth(index).click()

    def click_delete_course(self, index: int):
        expect(self.course_menu_btn.nth(index)).to_be_visible()
        self.course_menu_btn.nth(index).click()

        expect(self.course_delete_btn.nth(index)).to_be_visible()
        self.course_delete_btn.nth(index).click()















