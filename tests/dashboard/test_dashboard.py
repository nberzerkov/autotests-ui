import pytest
import allure
from pages.dashboard.dashboard_page import DashboardPage
from tools.allure.tags import AllureTag
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory

DASHBOARD_URL = "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard"

@pytest.mark.dashboard
@pytest.mark.regression
@allure.tag(AllureTag.DASHBOARD, AllureTag.REGRESSION)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.DASHBOARD)
@allure.story(AllureStory.DASHBOARD)
@allure.parent_suite(AllureEpic.LMS)
@allure.suite(AllureFeature.DASHBOARD)
@allure.sub_suite(AllureStory.DASHBOARD)
class TestDashboard:
    @allure.title("Check displaying of dashboard page")
    def test_dashboard_displaying(self, dashboard_page_with_state: DashboardPage):
        dashboard_page_with_state.visit(DASHBOARD_URL)

        dashboard_page_with_state.navbar.check_visible("nikita")
        dashboard_page_with_state.sidebar.check_visible()

        dashboard_page_with_state.toolbar.check_visible()
        dashboard_page_with_state.students_chart.check_visible("Students")
        dashboard_page_with_state.activities_chart.check_visible("Activities")
        dashboard_page_with_state.courses_chart.check_visible("Courses")
        dashboard_page_with_state.scores_chart.check_visible("Scores")
