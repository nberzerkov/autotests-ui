from dataclasses import dataclass
from playwright.sync_api import Page, expect
from components.base_component import BaseComponent

@dataclass
class CheckCreateCourseFormParams:
    title: str = ""
    estimate_time: str = ""
    description: str = ""
    max_score: str = "0"
    min_score: str = "0"

class CreateCourseFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.title_input = page.get_by_test_id("create-course-form-title-input").locator("input")
        self.estimated_time_input = page.get_by_test_id("create-course-form-estimated-time-input").locator("input")
        self.description_input = page.get_by_test_id("create-course-form-description-input").locator("textarea").first
        self.max_score_input = page.get_by_test_id("create-course-form-max-score-input").locator("input")
        self.min_score_input = page.get_by_test_id("create-course-form-min-score-input").locator("input")

    def check_visible(self, **kwargs):
        params = CheckCreateCourseFormParams(**kwargs)

        expect(self.title_input).to_be_visible()
        expect(self.title_input).to_have_value(params.title)

        expect(self.estimated_time_input).to_be_visible()
        expect(self.estimated_time_input).to_have_value(params.estimate_time)

        expect(self.description_input).to_be_visible()
        expect(self.description_input).to_have_value(params.description)

        expect(self.max_score_input).to_be_visible()
        expect(self.max_score_input).to_have_value(params.max_score)

        expect(self.min_score_input).to_be_visible()
        expect(self.min_score_input).to_have_value(params.min_score)

    def fill(self, **kwargs):
        params = CheckCreateCourseFormParams(**kwargs)

        self.title_input.fill(params.title)
        expect(self.title_input).to_have_value(params.title)

        self.estimated_time_input.fill(params.estimate_time)
        expect(self.estimated_time_input).to_have_value(params.estimate_time)

        self.description_input.fill(params.description)
        expect(self.description_input).to_have_value(params.description)

        self.max_score_input.fill(params.max_score)
        expect(self.max_score_input).to_have_value(params.max_score)

        self.min_score_input.fill(params.min_score)
        expect(self.min_score_input).to_have_value(params.min_score)
