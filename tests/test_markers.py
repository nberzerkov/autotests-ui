import pytest

@pytest.mark.smoke
def test_smoke_case():
    pass

@pytest.mark.regression
def test_regression_case():
    pass

@pytest.mark.regression
class TestUserAuthentication:
    @pytest.mark.smoke
    def test_login(self):
        pass

    # @pytest.mark.slow
    def test_password_reset(self):
        pass

    # @pytest.mark.fast
    def test_logout(self):
        pass


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.critical
# @pytest.mark.authentication
def test_critical_login():
    pass

@pytest.mark.ui
class TestUserInterface:
    @pytest.mark.smoke
    @pytest.mark.critical
    def test_login_btn(self):
        pass

    @pytest.mark.regression
    def test_forgot_password_link(self):
        pass

    @pytest.mark.smoke
    def test_signup_form(self):
        pass