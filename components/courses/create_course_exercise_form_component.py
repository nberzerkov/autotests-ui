from playwright.sync_api import Page, expect
from components.base_component import BaseComponent
from elements.button import Button
from elements.text import Text
from elements.input import Input

class CreateCourseExerciseFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.title_input = Input(page, "create-course-exercise-form-title-{index}-input", "Title")
        self.subtitle_text = Text(page, "create-course-exercise-{index}-box-toolbar-subtitle-text", "Exercise subtitle")
        self.description_input = Input(page, "create-course-exercise-form-description-{index}-input", "Exercise description")
        self.delete_exercise_btn = Button(page, "create-course-exercise-{index}-box-toolbar-delete-exercise-button", "Delete exercise")

    def check_visible(self, index: int = 0, title: str = "", description: str = ""):
        self.subtitle_text.check_visible(index=index)
        self.subtitle_text.check_have_text(f"#{index + 1} Exercises", index=index)

        self.title_input.check_visible(index=index)
        self.title_input.check_have_value(title, index=index)

        self.description_input.check_visible(index=index)
        self.description_input.check_have_value(description, index=index)

    def fill_create_exercise_form(self, index: int = 0, title: str = "", description: str = ""):
        
        self.title_input.fill(title, index=index)
        self.title_input.check_have_text(title, index=index)

        self.description_input.fill(description, index=index)
        self.description_input.check_have_value(description, index=index)

    def click_delete_exercise_btn(self, index: int = 0):
        self.delete_exercise_btn.click(index=index)

