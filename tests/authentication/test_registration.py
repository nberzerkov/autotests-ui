import re
import pytest
import allure
from pages.dashboard.dashboard_page import DashboardPage
from pages.authentication.registration_page import RegistrationPage
from tools.allure.tags import AllureTag
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory

REGISTRATION_URL = "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration"

email_data = "user.name@gmail.com"
username_data = "username"
password_data = "password"

@pytest.mark.regression
@pytest.mark.registration
@allure.tag(AllureTag.REGRESSION, AllureTag.REGISTRATION)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.AUTHENTICATION)
@allure.story(AllureStory.REGISTRATION)
class TestRegistration:
        @allure.title("Registration with correct email, username and password")
        def test_successful_registration(self, registration_page: RegistrationPage, dashboard_page: DashboardPage):
                registration_page.visit(REGISTRATION_URL)

                registration_page.form.fill(email=email_data, username=username_data, password=password_data)
                registration_page.click_registration_btn()

                dashboard_page.toolbar.check_visible()
                dashboard_page.toolbar.check_current_url(re.compile(".*/#/dashboard"))

