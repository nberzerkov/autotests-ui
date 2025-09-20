from pages.base_page import BasePage
from playwright.sync_api import Page
from components.authentication.registration_form_component import RegistrationFormComponent
from elements.button import Button
from elements.link import Link
from elements.text import Text


class RegistrationPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.form = RegistrationFormComponent(page)

        self.registration_btn = Button(page, 'registration-page-registration-button', "Registration")
        self.login_link = Link(page, 'registration-page-login-link', "Login")
        self.course_title = Text(page, 'authentication-ui-course-title-text', "Title")

    def click_registration_btn(self):
        self.registration_btn.check_visible()
        self.registration_btn.click()

    def click_login_link(self):
        self.login_link.check_visible()
        self.login_link.click()
