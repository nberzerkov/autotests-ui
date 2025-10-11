import allure
from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements.text import Text
from elements.button import Button


class CreateCourseExercisesToolbarViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.title = Text(page, "create-course-exercises-box-toolbar-title-text", "Title")
        self.create_exercise_btn = Button(page, "create-course-exercises-box-toolbar-create-exercise-button", "Create Exercise btn")

    @allure.step('Checking visible create course exercise toolbar view')
    def check_visible(self):
        self.title.check_visible()
        self.title.check_have_text("Exercises")

        self.create_exercise_btn.check_visible()
        self.create_exercise_btn.check_enabled()

    def click_create_exercise_btn(self):
        self.create_exercise_btn.click()
