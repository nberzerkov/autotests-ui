from pages.base_page import BasePage
from playwright.sync_api import Page, expect
from components.authentication.registration_form_component import RegistrationFormComponent

class RegistrationPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.form = RegistrationFormComponent(page)

        self.registration_btn = page.get_by_test_id('registration-page-registration-button')
        self.login_link = page.get_by_test_id('registration-page-login-link')
        self.course_title = page.get_by_test_id('authentication-ui-course-title-text')

    def click_registration_btn(self):
        expect(self.registration_btn).to_be_visible()
        self.registration_btn.click()

    def click_login_link(self):
        expect(self.click_login_link).to_be_visible()
        self.login_link.click()