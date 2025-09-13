from playwright.sync_api import expect
from components.base_component import BaseComponent

class CreateCourseExerciseFormComponent(BaseComponent):

    def check_visible(self, index: int = 0, title: str = "", description: str = ""):
        subtitle_text = self.page.get_by_test_id(f"create-course-exercise-{index}-box-toolbar-subtitle-text")
        title_input = self.page.get_by_test_id(f"create-course-exercise-form-title-{index}-input")
        description_input = self.page.get_by_test_id(
            f"create-course-exercise-form-description-{index}-input")

        expect(subtitle_text).to_be_visible()
        expect(subtitle_text).to_have_text(f"#{index + 1} Exercises")

        expect(title_input).to_be_visible()
        expect(title_input).to_have_value(title)

        expect(description_input).to_be_visible()
        expect(description_input).to_have_value(description)

    def fill_create_exercise_form(self, index: int = 0, title: str = "", description: str = ""):
        title_input = self.page.get_by_test_id(f"create-course-exercise-form-title-{index}-input")
        description_input = self.page.get_by_test_id(
            f"create-course-exercise-form-description-{index}-input")

        expect(title_input).fill(title)
        expect(title_input).to_have_text(title)

        expect(description_input).fill(description)
        expect(description_input).to_have_value(description)

    def click_delete_exercise_btn(self, index: int = 0):
        delete_btn = self.page.get_by_test_id(
            f"create-course-exercise-{index}-box-toolbar-delete-exercise-button")

        delete_btn.click()
