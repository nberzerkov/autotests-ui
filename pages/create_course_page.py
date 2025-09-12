from pages.base_page import BasePage
from playwright.sync_api import Page, expect
from components.views.empty_view_component import EmptyViewComponent
from components.views.img_upload_widget_component import ImgUploadWidgetComponent
from components.courses.create_course_exercise_form_component import CreateCourseExerciseFormComponent
from components.navigation.navbar_component import NavbarComponent
from components.navigation.sidebar_component import SidebarComponent

class CreateCoursePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.navbar = NavbarComponent(page)
        self.sidebar = SidebarComponent(page)
        self.create_course_exercise_form = CreateCourseExerciseFormComponent(page)
        self.exercises_empty_view = EmptyViewComponent(page, "create-course-exercises")
        self.img_upload_widget = ImgUploadWidgetComponent(page, "create-course-preview")

        # Заголовок и кнопка создания курса
        self.create_course_title = page.get_by_test_id("create-course-toolbar-title-text")
        self.create_course_btn = page.get_by_test_id("create-course-toolbar-create-course-button")

        # Поле с инпутами для заполнения инфо по курсу
        self.create_course_form_title_input = page.get_by_test_id("create-course-form-title-input").locator("input")
        self.create_course_form_estimated_time_input = page.get_by_test_id("create-course-form-estimated-time-input").locator("input")
        self.create_course_form_description_textarea = page.get_by_test_id("create-course-form-description-input").locator("textarea").first
        self.create_course_form_max_score_input = page.get_by_test_id("create-course-form-max-score-input").locator("input")
        self.create_course_form_min_score_input = page.get_by_test_id("create-course-form-min-score-input").locator("input")

        # Заголовок и кнопка создания упражнения
        self.exercise_title_text = page.get_by_test_id("create-course-exercises-box-toolbar-title-text")
        self.create_exercise_btn = page.get_by_test_id("create-course-exercises-box-toolbar-create-exercise-button")

    # Методы для заголовка и кнопки создания курса
    def check_visible_create_course_title(self):
        expect(self.create_course_title).to_be_visible()
        expect(self.create_course_title).to_have_text("Create course")

    def check_visible_create_course_disabled_btn(self):
        expect(self.create_course_btn).to_be_visible()

    def check_disabled_create_course_btn(self):
        self.create_course_btn.wait_for(state="attached")
        expect(self.create_course_btn).to_be_disabled()

    def click_create_course_btn(self):
        self.create_course_btn.click()

    # Проверка формы создания курса
    def check_visible_create_course_form(self,
                                         title: str = "", estimate_time: int = "", description: str = "",
                                         max_score: str = "0", min_score: str = "0"):
        expect(self.create_course_form_title_input).to_be_visible()
        expect(self.create_course_form_title_input).to_have_value(title)

        expect(self.create_course_form_estimated_time_input).to_be_visible()
        expect(self.create_course_form_estimated_time_input).to_have_value(estimate_time)

        expect(self.create_course_form_description_textarea).to_be_visible()
        expect(self.create_course_form_description_textarea).to_have_value(description)

        expect(self.create_course_form_max_score_input).to_be_visible()
        expect(self.create_course_form_max_score_input).to_have_value(max_score)

        expect(self.create_course_form_min_score_input).to_be_visible()
        expect(self.create_course_form_min_score_input).to_have_value(min_score)

    # Заполнение формы создания курса
    def fill_create_course_form(self, title: str = "", estimate_time: str = "", description: str = "", max_score: str = "0", min_score: str = "0"):

        self.create_course_form_title_input.fill(title)
        expect(self.create_course_form_title_input).to_have_value(title)

        self.create_course_form_estimated_time_input.fill(estimate_time)
        expect(self.create_course_form_estimated_time_input).to_have_value(estimate_time)

        self.create_course_form_description_textarea.fill(description)
        expect(self.create_course_form_description_textarea).to_have_value(description)

        self.create_course_form_max_score_input.fill(max_score)
        expect(self.create_course_form_max_score_input).to_have_value(max_score)

        self.create_course_form_min_score_input.fill(min_score)
        expect(self.create_course_form_min_score_input).to_have_value(min_score)

    # Заголовок и кнопка создания упражнения
    def check_visible_exercise_title(self):
        expect(self.exercise_title_text).to_be_visible()
        expect(self.exercise_title_text).to_have_text("Exercises")

    def check_visible_create_exercise_btn(self):
        expect(self.create_exercise_btn).to_be_visible()

    def click_create_exercise_btn(self):
        self.create_exercise_btn.click()

    # Блок с empty view упражнения
    def check_visible_exercise_empty_view(self):
        self.exercises_empty_view.check_visible(
            title="There is no exercises",
            description="Click on \"Create exercise\" button to create new exercise"
        )




