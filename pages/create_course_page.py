from playwright.sync_api import Page, expect
from pages.base_page import BasePage
from dataclasses.check_visible_course_card_params import CourseCardParams

class CreateCoursePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        # Заголовок и кнопка создания курса
        self.create_course_title = page.get_by_test_id("create-course-toolbar-title-text")
        self.create_course_btn = page.get_by_test_id("create-course-toolbar-create-course-button")

        # Блок отображения превью когда картинка не загружена и когда картинка загружена
        self.preview_empty_view_icon = page.get_by_test_id("create-course-preview-empty-view-icon")
        self.preview_empty_view_title = page.get_by_test_id("create-course-preview-empty-view-title-text")
        self.preview_empty_view_description = page.get_by_test_id("create-course-preview-empty-view-description-text")
        self.preview_img_view = page.get_by_test_id("create-course-preview-image-upload-widget-preview-image")

        # Блок загрузки фотографий с кнопкой upload и remove
        self.preview_img_upload_icon = page.get_by_test_id("create-course-preview-image-upload-widget-info-icon")
        self.preview_img_upload_title = page.get_by_test_id("create-course-preview-image-upload-widget-info-title-text")
        self.preview_img_upload_description = page.get_by_test_id("create-course-preview-image-upload-widget-info-description-text")
        self.preview_img_upload_btn = page.get_by_test_id("create-course-preview-image-upload-widget-upload-button")
        self.preview_img_remove_btn = page.get_by_test_id("create-course-preview-image-upload-widget-remove-button")

        # Поле с инпутами для заполнения инфо по курсу
        self.create_course_form_title_input = page.get_by_test_id("create-course-form-title-input").locator("input")
        self.create_course_form_estimated_time_input = page.get_by_test_id("create-course-form-estimated-time-input").locator("input")
        self.create_course_form_description_textarea = page.get_by_test_id("create-course-form-description-input").locator("textarea").first
        self.create_course_form_max_score_input = page.get_by_test_id("create-course-form-max-score-input").locator("input")
        self.create_course_form_min_score_input = page.get_by_test_id("create-course-form-min-score-input").locator("input")

        # Заголовок и кнопка создания упражнения
        self.exercise_title_text = page.get_by_test_id("create-course-exercises-box-toolbar-title-text")
        self.create_exercise_btn = page.get_by_test_id("create-course-exercises-box-toolbar-create-exercise-button")

        # Блок с empty view упражнения
        self.exercise_empty_view_icon = page.get_by_test_id("create-course-exercises-empty-view-icon")
        self.exercise_empty_view_title_text = page.get_by_test_id("create-course-exercises-empty-view-title-text")
        self.exercise_empty_view_description = page.get_by_test_id("create-course-exercises-empty-view-description-text")

    # Методы для заголовка и кнопки создания курса
    def check_visible_create_course_title(self):
        expect(self.create_course_title).to_be_visible()
        expect(self.create_course_title).to_have_text("Create course")

    def check_visible_create_course_disabled_btn(self):
        expect(self.create_course_btn).to_be_visible()

    def check_disabled_create_course_btn(self):
        expect(self.create_course_btn).to_be_disable()

    def click_create_course_btn(self):
        self.create_course_btn.click()

    # Блок для пустого превью img
    def check_visible_img_preview_empty_view(self):
        expect(self.preview_empty_view_icon).to_be_visible()

        expect(self.preview_empty_view_title).to_be_visible()
        expect(self.preview_empty_view_title).to_have_text("No image selected")

        expect(self.preview_empty_view_description).to_be_visible()
        expect(self.preview_empty_view_description).to_have_text("Preview of selected image will be displayed here")

    # Методы для работы с блоком загрузки фото и проверка, что img загружен
    def check_visible_image_upload_view(self, is_img_uploaded: bool = False):
        expect(self.preview_img_upload_icon).to_be_visible()

        expect(self.preview_img_upload_title).to_be_visible()
        expect(self.preview_img_upload_title).to_have_text('Tap on "Upload image" button to select file')

        expect(self.preview_img_upload_description).to_be_visible()
        expect(self.preview_img_upload_description).to_have_text("Recommended file size 540X300")

        expect(self.preview_img_upload_btn).to_be_visible()

        if is_img_uploaded:
            expect(self.preview_img_remove_btn).to_be_visible()

    def check_visible_preview_img(self):
        expect(self.preview_img_view).to_be_visible()

    def click_remove_img_btn(self):
        self.preview_img_remove_btn.click()

    def upload_preview_img(self, file: str):
        self.preview_img_upload_btn.set_input_files(file)

    # Проверка формы создания курса
    def check_visible_create_course_form(self, params: CourseCardParams):
        expect(self.create_course_form_title_input).to_be_visible()
        expect(self.create_course_form_title_input).to_have_value(params.title)

        expect(self.create_course_form_estimated_time_input).to_be_visible()
        expect(self.create_course_form_estimated_time_input).to_have_value(params.estimate_time)

        expect(self.create_course_form_description_textarea).to_be_visible()
        expect(self.create_course_form_description_textarea).to_have_value(params.description)

        expect(self.create_course_form_max_score_input).to_be_visible()
        expect(self.create_course_form_max_score_input).to_have_value(params.max_score)

        expect(self.create_course_form_min_score_input).to_be_visible()
        expect(self.create_course_form_min_score_input).to_have_value(params.min_score)

    # Заполнение формы создания курса
    def fill_create_course_form(self, params: CourseCardParams):
        self.create_course_form_title_input.fill(params.title)
        expect(self.create_course_form_title_input).to_have_value(params.title)

        self.create_course_form_estimated_time_input.fill(params.estimate_time)
        expect(self.create_course_form_estimated_time_input).to_have_value(params.estimate_time)

        self.create_course_form_description_textarea.fill(params.description)
        expect(self.create_course_form_description_textarea).to_have_value(params.description)

        self.create_course_form_max_score_input.fill(params.max_score)
        expect(self.create_course_form_max_score_input).to_have_value(params.max_score)

        self.create_course_form_min_score_input.fill(params.min_score)
        expect(self.create_course_form_min_score_input).to_have_value(params.min_score)

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
        expect(self.exercise_empty_view_icon).to_be_visible()

        expect(self.exercise_empty_view_title_text).to_be_visible()
        expect(self.exercise_empty_view_title_text).to_have_text("There is no exercises")

        expect(self.exercise_empty_view_description).to_be_visible()
        expect(self.exercise_empty_view_description).to_have_text('Click on "Create exercise" button to create new exercise')

    # Блок с созданием динамических упражнений (#1 Exercise)
    def check_visible_exercise_form(self, params: CourseCardParams):
        exercise_subtitle_text = self.page.get_by_test_id(f"create-course-exercise-{params.index}-box-toolbar-subtitle-text")
        exercise_form_title_input = self.page.get_by_test_id(f"create-course-exercise-form-title-{params.index}-input")
        exercise_form_description_input = self.page.get_by_test_id(
            f"create-course-exercise-form-description-{params.index}-input")

        expect(exercise_subtitle_text).to_be_visible()
        expect(exercise_subtitle_text).to_have_text(f"#{params.index + 1} Exercises")

        expect(exercise_form_title_input).to_be_visible()
        expect(exercise_form_title_input).to_have_value(params.title)

        expect(exercise_form_description_input).to_be_visible()
        expect(exercise_form_description_input).to_have_value(params.description)

    def fill_create_exercise_form(self, params: CourseCardParams):
        exercise_form_title_input = self.page.get_by_test_id(f"create-course-exercise-form-title-{params.index}-input")
        exercise_form_description_input = self.page.get_by_test_id(
            f"create-course-exercise-form-description-{params.index}-input")

        expect(exercise_form_title_input).fill(params.title)
        expect(exercise_form_title_input).to_have_text(params.title)

        expect(exercise_form_description_input).fill(params.description)
        expect(exercise_form_description_input).to_have_value(params.description)

    def click_delete_exercise_btn(self, params: CourseCardParams):
        delete_exercise_btn = self.page.get_by_test_id(
            f"create-course-exercise-{params.index}-box-toolbar-delete-exercise-button")

        delete_exercise_btn.click()


