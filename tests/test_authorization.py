import pytest
from pages.login_page import LoginPage

LOGIN_URL = 'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login'

authCreds = [
    ("nikita@mail.ru", "nikita123"),
    ("user.name@gmail.com", "  "),
    ("  ", "password")
]

@pytest.mark.regression
@pytest.mark.authorization
@pytest.mark.parametrize('email, password', authCreds)
def test_wrong_email_or_password_authorization(login_page: LoginPage, email: str, password: str) -> None:
    login_page.visit(LOGIN_URL)

    login_page.form.fill(email=email, password=password)
    login_page.click_login_btn()
    login_page.check_visible_wrong_email_or_password_alert()


