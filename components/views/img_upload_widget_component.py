from playwright.sync_api import Page, expect
from components.base_component import BaseComponent
from components.views.empty_view_component import EmptyViewComponent


class ImgUploadWidgetComponent(BaseComponent):
    def __init__(self, page: Page, identifier: str):
        super().__init__(page)

        self.preview_empty_view = EmptyViewComponent(page, identifier)

        # Загруженный img в блоке preview
        self.preview_img = page.get_by_test_id(f"{identifier}-image-upload-widget-preview-image")

        # Блок загрузки фотографий с кнопкой upload и remove
        self.img_upload_info_icon = page.get_by_test_id(f"{identifier}-image-upload-widget-info-icon")
        self.img_upload_info_title = page.get_by_test_id(f"{identifier}-image-upload-widget-info-title-text")
        self.img_upload_info_description = page.get_by_test_id(f"{identifier}-image-upload-widget-info-description-text")
        self.upload_btn = page.get_by_test_id(f"{identifier}-image-upload-widget-input")
        self.remove_btn = page.get_by_test_id(f"{identifier}-image-upload-widget-remove-button")
        self.upload_input = page.get_by_test_id(f"{identifier}-image-upload-widget-input")

    # Методы для работы с блоком загрузки фото и проверка, что img загружен
    def check_visible(self, is_img_uploaded: bool = False):
        expect(self.img_upload_info_icon).to_be_visible()

        expect(self.img_upload_info_title).to_be_visible()
        expect(self.img_upload_info_title).to_have_text('Tap on "Upload image" button to select file')

        expect(self.img_upload_info_description).to_be_visible()
        expect(self.img_upload_info_description).to_have_text("Recommended file size 540X300")

        expect(self.upload_btn).to_be_visible()

        if is_img_uploaded:
            expect(self.remove_btn).to_be_visible()
            expect(self.preview_img).to_be_visible()

        if not is_img_uploaded:
            self.preview_empty_view.check_visible(title="No image selected", description="Preview of selected image will be displayed here")

    def click_remove_img_btn(self):
        self.remove_btn.click()

    def upload_preview_img(self, file: str):
        self.upload_input.set_input_files(file)
