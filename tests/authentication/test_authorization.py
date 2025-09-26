import pytest
from pages.authentication.login_page import LoginPage
from pages.authentication.registration_page import RegistrationPage
from pages.dashboard.dashboard_page import DashboardPage

LOGIN_URL = 'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login'
REGISTRATION_URL = 'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration'

authCredsParams = [
    ("nikita@mail.ru", "nikita123"),
    ("user.name@gmail.com", "  "),
    ("  ", "password")
]

@pytest.mark.regression
@pytest.mark.authorization
class TestAuthorization:
    @pytest.mark.parametrize('email, password', authCredsParams)
    def test_wrong_email_or_password_authorization(self, login_page: LoginPage, email: str, password: str) -> None:
        login_page.visit(LOGIN_URL)

        login_page.form.fill(email=email, password=password)
        login_page.click_login_btn()
        login_page.check_visible_wrong_email_or_password_alert()

    def test_successful_authorization(self, registration_page: RegistrationPage, dashboard_page: DashboardPage, login_page: LoginPage) -> None:
        registration_page.visit(REGISTRATION_URL)

        registration_page.form.fill(email="testuser@mail.ru", username="user123", password="password")
        registration_page.click_registration_btn()

        dashboard_page.toolbar.check_visible()
        dashboard_page.navbar.check_visible("user123")
        dashboard_page.sidebar.check_visible()
        dashboard_page.sidebar.click_logout()

        login_page.form.check_visible()
        login_page.form.fill(email="testuser@mail.ru", password="password")
        login_page.click_login_btn()

        dashboard_page.toolbar.check_visible()
        dashboard_page.navbar.check_visible("user123")
        dashboard_page.sidebar.check_visible()

    def test_navigate_from_authorization_to_registration(self, login_page: LoginPage, registration_page: RegistrationPage) -> None:
        login_page.visit(LOGIN_URL)

        login_page.click_registration_link()
        registration_page.form.check_visible()










