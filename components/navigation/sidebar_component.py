import re

import allure
from playwright.sync_api import Page

from components.base_component import BaseComponent
from components.navigation.sidebar_list_item_component import SideBarListItemComponent

class SidebarComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.dashboard_list_item = SideBarListItemComponent(page, "dashboard")
        self.courses_list_item = SideBarListItemComponent(page, "courses")
        self.logout_list_item = SideBarListItemComponent(page, "logout")

    @allure.step('Check visible sidebar')
    def check_visible(self):
        self.dashboard_list_item.check_visible("Dashboard")
        self.courses_list_item.check_visible("Courses")
        self.logout_list_item.check_visible("Logout")

    @allure.step('Click dashboard on sidebar')
    def click_dashboard(self):
        self.dashboard_list_item.navigate_to(re.compile(r".*/#/dashboard"))

    @allure.step('Click course on sidebar')
    def click_courses(self):
        self.courses_list_item.navigate_to(re.compile(r".*/#/courses"))

    @allure.step('Click logout on sidebar')
    def click_logout(self):
        self.logout_list_item.navigate_to(re.compile(r".*/#/auth/login"))


