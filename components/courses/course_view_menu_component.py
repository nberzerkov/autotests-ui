from playwright.sync_api import Page, expect
from components.base_component import BaseComponent

class CourseViewMenuComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.menu_btn = page.get_by_test_id("course-view-menu-button")
        self.edit_menu_item = page.get_by_test_id("course-view-edit-menu-item")
        self.delete_menu_item = page.get_by_test_id("course-view-delete-menu-item")

    def check_visible(self, index: int):
        expect(self.menu_btn.nth(index)).to_be_visible()
        self.menu_btn.nth(index).click()

        expect(self.edit_menu_item.nth(index)).to_be_visible()
        expect(self.delete_menu_item.nth(index)).to_be_visible()

    def click_edit(self, index: int):
        self.menu_btn.nth(index).click()

        self.edit_menu_item.nth(index).click()

    def click_delete(self, index: int):
        self.menu_btn.nth(index).click()

        self.delete_menu_item.nth(index).click()

