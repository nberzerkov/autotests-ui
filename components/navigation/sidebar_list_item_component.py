from playwright.sync_api import Page
from components.base_component import BaseComponent
from re import Pattern
from elements.icon import Icon
from elements.button import Button
from elements.text import Text

class SideBarListItemComponent(BaseComponent):
    def __init__(self, page: Page, identifier: str):
        super().__init__(page)

        self.icon = Icon(page, f"{identifier}-drawer-list-item-icon", "Icon")
        self.title = Text(page, f"{identifier}-drawer-list-item-title-text", "Title")
        self.btn = Button(page, f"{identifier}-drawer-list-item-button", "Button")

    def check_visible(self, title: str):
        self.icon.check_visible()

        self.title.check_visible()
        self.title.check_have_text(title)

        self.btn.check_visible()

    def navigate_to(self, expected_url: Pattern[str]):
        self.btn.click()
        self.check_current_url(expected_url)
