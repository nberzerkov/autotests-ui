import re
import pytest
import allure

from config import settings

from tools.routes import AppRoute
from tools.allure.tags import AllureTag
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory

from pages.dashboard.dashboard_page import DashboardPage
from pages.authentication.registration_page import RegistrationPage

@pytest.mark.regression
@pytest.mark.registration
@allure.tag(AllureTag.REGRESSION, AllureTag.REGISTRATION)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.AUTHENTICATION)
@allure.story(AllureStory.REGISTRATION)
@allure.parent_suite(AllureEpic.LMS)
@allure.suite(AllureFeature.AUTHENTICATION)
@allure.sub_suite(AllureStory.REGISTRATION)
class TestRegistration:
        @allure.title("Registration with correct email, username and password")
        def test_successful_registration(self, registration_page: RegistrationPage, dashboard_page: DashboardPage):
                registration_page.visit(AppRoute.REGISTRATION)

                registration_page.form.fill(
                        email=settings.test_user.email,
                        username=settings.test_user.username,
                        password=settings.test_user.password)

                # registration_page.page.wait_for_timeout(50000)
                registration_page.click_registration_btn()

                dashboard_page.toolbar.check_visible()
                dashboard_page.toolbar.check_current_url(re.compile(".*/#/dashboard"))

