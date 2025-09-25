import re
from playwright.sync_api import Page
from components.base_component import BaseComponent
from components.navigation.sidebar_list_item_component import SideBarListItemComponent

class SidebarComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.dashboard_list_item = SideBarListItemComponent(page, "dashboard")
        self.courses_list_item = SideBarListItemComponent(page, "courses")
        self.logout_list_item = SideBarListItemComponent(page, "logout")

    def check_visible(self):
        self.dashboard_list_item.check_visible("Dashboard")
        self.courses_list_item.check_visible("Courses")
        self.logout_list_item.check_visible("Logout")

    def click_dashboard(self):
        self.dashboard_list_item.navigate_to(re.compile(r".*/#/dashboard"))

    def click_courses(self):
        self.courses_list_item.navigate_to(re.compile(r".*/#/courses"))

    def click_logout(self):
        self.logout_list_item.navigate_to(re.compile(r".*/#/auth/login"))


