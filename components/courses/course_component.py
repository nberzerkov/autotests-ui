from playwright.sync_api import Page, expect
from components.base_component import BaseComponent
from components.courses.course_view_menu_component import CourseViewMenuComponent

class CourseViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.menu = CourseViewMenuComponent(page)

        self.title = page.get_by_test_id("course-widget-title-text")
        self.img = page.get_by_test_id("course-preview-image")
        self.max_score_text = page.get_by_test_id("course-max-score-info-row-view-text")
        self.min_score_text = page.get_by_test_id("course-min-score-info-row-view-text")
        self.estimate_time_text = page.get_by_test_id("course-estimated-time-info-row-view-text")

    def check_visible(self, index: int, title: str, estimate_time: str, max_score: str, min_score: str):
        expect(self.img.nth(index)).to_be_visible()

        expect(self.title.nth(index)).to_be_visible()
        expect(self.title.nth(index)).to_have_text(title)

        expect(self.max_score_text.nth(index)).to_be_visible()
        expect(self.max_score_text.nth(index)).to_have_text(f"Max score: {max_score}")

        expect(self.min_score_text.nth(index)).to_be_visible()
        expect(self.min_score_text.nth(index)).to_have_text(f"Min score: {min_score}")

        expect(self.estimate_time_text.nth(index)).to_be_visible()
        expect(self.estimate_time_text.nth(index)).to_have_text(f"Estimated time: {estimate_time}")

