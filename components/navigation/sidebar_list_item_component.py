from playwright.sync_api import Page, expect
from components.base_component import BaseComponent
from re import Pattern

class SideBarListItemComponent(BaseComponent):
    def __init__(self, page: Page, identifier: str):
        super().__init__(page)

        self.icon = page.get_by_test_id(f"{identifier}-drawer-list-item-icon")
        self.title = page.get_by_test_id(f"{identifier}-drawer-list-item-title-text")
        self.btn = page.get_by_test_id(f"{identifier}-drawer-list-item-button")

    def check_visible(self, title: str):
        expect(self.icon).to_be_visible()

        expect(self.title).to_be_visible()
        expect(self.title).to_have_text(title)

        expect(self.btn).to_be_visible()

    def navigate_to(self, expected_url: Pattern[str]):
        self.btn.click()
        self.check_current_url(expected_url)