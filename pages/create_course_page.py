from pages.base_page import BasePage
from playwright.sync_api import Page, expect
from components.navigation.navbar_component import NavbarComponent
from components.navigation.sidebar_component import SidebarComponent
from components.views.empty_view_component import EmptyViewComponent
from components.views.img_upload_widget_component import ImgUploadWidgetComponent
from components.courses.create_course_toolbar_view_component import CreateCourseToolbarViewComponent
from components.courses.create_course_exercise_form_component import CreateCourseExerciseFormComponent
from components.courses.create_course_exercises_toolbar_view_component import CreateCourseExercisesToolbarViewComponent

class CreateCoursePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.navbar = NavbarComponent(page)
        self.sidebar = SidebarComponent(page)
        self.create_exercise_form = CreateCourseExerciseFormComponent(page)
        self.exercises_empty_view = EmptyViewComponent(page, "create-course-exercises")
        self.img_upload_widget = ImgUploadWidgetComponent(page, "create-course-preview")
        self.toolbar = CreateCourseToolbarViewComponent(page)
        self.exercises_toolbar = CreateCourseExercisesToolbarViewComponent(page)

        # Поле с инпутами для заполнения инфо по курсу
        self.create_course_form_title_input = page.get_by_test_id("create-course-form-title-input").locator("input")
        self.create_course_form_estimated_time_input = page.get_by_test_id("create-course-form-estimated-time-input").locator("input")
        self.create_course_form_description_textarea = page.get_by_test_id("create-course-form-description-input").locator("textarea").first
        self.create_course_form_max_score_input = page.get_by_test_id("create-course-form-max-score-input").locator("input")
        self.create_course_form_min_score_input = page.get_by_test_id("create-course-form-min-score-input").locator("input")

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
        
    # Блок с empty view упражнения
    def check_visible_exercise_empty_view(self):
        self.exercises_empty_view.check_visible(
            title="There is no exercises",
            description="Click on \"Create exercise\" button to create new exercise"
        )




