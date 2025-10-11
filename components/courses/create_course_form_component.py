from dataclasses import dataclass

import allure
from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements.input import Input
from elements.textarea import Textarea

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

        self.title_input = Input(page, "create-course-form-title-input", "Title")
        self.estimated_time_input = Input(page, "create-course-form-estimated-time-input", "Estimate time")
        self.description_input = Textarea(page, "create-course-form-description-input", "Description")
        self.max_score_input = Input(page, "create-course-form-max-score-input", "Max Score")
        self.min_score_input = Input(page, "create-course-form-min-score-input", "Min Score")

    @allure.step('Checking visible create course form')
    def check_visible(self, **kwargs):
        params = CheckCreateCourseFormParams(**kwargs)

        self.title_input.fill(params.title)
        self.title_input.check_have_value(params.title)

        self.estimated_time_input.check_visible()
        self.estimated_time_input.check_have_value(params.estimate_time)

        self.description_input.check_visible()
        self.description_input.check_have_value(params.description)

        self.max_score_input.check_visible()
        self.max_score_input.check_have_value(params.max_score)

        self.min_score_input.check_visible()
        self.min_score_input.check_have_value(params.min_score)

    @allure.step('Fill create course form')
    def fill(self, **kwargs):
        params = CheckCreateCourseFormParams(**kwargs)
        title = params.title

        self.title_input.fill(title)
        self.title_input.check_have_value(title)

        self.estimated_time_input.fill(params.estimate_time)
        self.estimated_time_input.check_have_value(params.estimate_time)

        self.description_input.fill(params.description)
        self.description_input.check_have_value(params.description)

        self.max_score_input.fill(params.max_score)
        self.max_score_input.check_have_value(params.max_score)

        self.min_score_input.fill(params.min_score)
        self.min_score_input.check_have_value(params.min_score)

