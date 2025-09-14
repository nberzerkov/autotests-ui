from pages.base_page import BasePage
from playwright.sync_api import Page
from components.navigation.navbar_component import NavbarComponent
from components.navigation.sidebar_component import SidebarComponent
from components.views.empty_view_component import EmptyViewComponent
from components.courses.create_course_toolbar_view_component import CreateCourseToolbarViewComponent
from components.views.img_upload_widget_component import ImgUploadWidgetComponent
from components.courses.create_course_form_component import CreateCourseFormComponent
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
        self.form = CreateCourseFormComponent(page)
        
    # Блок с empty view упражнения
    def check_visible_exercise_empty_view(self):
        self.exercises_empty_view.check_visible(
            title="There is no exercises",
            description="Click on \"Create exercise\" button to create new exercise"
        )




