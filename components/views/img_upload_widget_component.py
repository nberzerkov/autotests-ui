from playwright.sync_api import Page
from components.base_component import BaseComponent
from components.views.empty_view_component import EmptyViewComponent
from elements.image import Image
from elements.text import Text
from elements.file_input import FileInput
from elements.button import Button
from elements.icon import Icon

class ImgUploadWidgetComponent(BaseComponent):
    def __init__(self, page: Page, identifier: str):
        super().__init__(page)

        self.preview_empty_view = EmptyViewComponent(page, identifier)

        # Загруженный img в блоке preview
        self.preview_img = Image(page, f"{identifier}-image-upload-widget-preview-image", "Image")

        # Блок загрузки фотографий с кнопкой upload и remove
        self.img_upload_info_icon = Icon(page, f"{identifier}-image-upload-widget-info-icon", "Upload Icon")
        self.img_upload_info_title = Text(page, f"{identifier}-image-upload-widget-info-title-text", "Title")
        self.img_upload_info_description = Text(page, f"{identifier}-image-upload-widget-info-description-text", "Description")
        self.upload_btn = Button(page, f"{identifier}-image-upload-widget-input", "Upload btn")
        self.remove_btn = Button(page, f"{identifier}-image-upload-widget-remove-button", "Remove btn")
        self.upload_input = FileInput(page, f"{identifier}-image-upload-widget-input", "Upload input")

    # Методы для работы с блоком загрузки фото и проверка, что img загружен
    def check_visible(self, is_img_uploaded: bool = False):
        self.img_upload_info_icon.check_visible()

        self.img_upload_info_title.check_visible()
        self.img_upload_info_title.check_have_text('Tap on "Upload image" button to select file')

        self.img_upload_info_description.check_visible()
        self.img_upload_info_description.check_have_text("Recommended file size 540X300")

        self.upload_btn.check_visible()

        if is_img_uploaded:
            self.remove_btn.check_visible()
            self.preview_img.check_visible()

        if not is_img_uploaded:
            self.preview_empty_view.check_visible(title="No image selected", description="Preview of selected image will be displayed here")

    def click_remove_img_btn(self):
        self.remove_btn.click()

    def upload_preview_img(self, file: str):
        self.upload_input.set_input_files(file)
