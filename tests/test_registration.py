import re
import pytest
from pages.dashboard_page import DashboardPage
from pages.registration_page import RegistrationPage

REGISTRATION_URL = "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration"

email_data = "user.name@gmail.com"
username_data = "username"
password_data = "password"

@pytest.mark.regression
@pytest.mark.registration
def test_successful_registration(registration_page: RegistrationPage, dashboard_page: DashboardPage):
        registration_page.visit(REGISTRATION_URL)

        registration_page.form.fill(email=email_data, username=username_data, password=password_data)
        registration_page.click_registration_btn()

        dashboard_page.toolbar.check_visible()
        dashboard_page.toolbar.check_current_url(re.compile(".*/#/dashboard"))

