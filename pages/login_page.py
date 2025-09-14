from playwright.sync_api import Page, expect
from pages.base_page import BasePage
from components.authentication.login_form_component import LoginFormComponent

class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.form = LoginFormComponent(page)

        self.wrong_email_or_password_alert = page.get_by_test_id("login-page-wrong-email-or-password-alert")
        self.login_btn = page.get_by_test_id("login-page-login-button")
        self.registration_link = page.get_by_test_id("login-page-registration-link")

    def click_login_btn(self):
        expect(self.login_btn).to_be_visible()
        self.login_btn.click()

    def click_registration_link(self):
        expect(self.registration_link).to_be_visible()
        self.registration_link.click()

    def check_visible_wrong_email_or_password_alert(self):
        expect(self.wrong_email_or_password_alert).to_be_visible()
        expect(self.wrong_email_or_password_alert).to_have_text("Wrong email or password")