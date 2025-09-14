import pytest
from pages.dashboard_page import DashboardPage

DASHBOARD_URL = "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard"

@pytest.mark.dashboard
@pytest.mark.regression
def test_dashboard_displaying(dashboard_page_with_state: DashboardPage):
    dashboard_page_with_state.visit(DASHBOARD_URL)

    dashboard_page_with_state.navbar.check_visible("nikita")
    dashboard_page_with_state.sidebar.check_visible()

    dashboard_page_with_state.toolbar.check_visible()
    dashboard_page_with_state.students_chart.check_visible("Students")
    dashboard_page_with_state.activities_chart.check_visible("Activities")
    dashboard_page_with_state.courses_chart.check_visible("Courses")
    dashboard_page_with_state.scores_chart.check_visible("Scores")
