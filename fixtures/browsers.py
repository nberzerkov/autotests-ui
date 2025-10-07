import pytest
from playwright.sync_api import Page, Playwright
from pages.authentication.registration_page import RegistrationPage

registration_url = 'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration'
courses_url = 'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses'
email_data = 'user.name@gmail.com'
username_data = 'nikita'
password_data = "password"

# Создаем новую страницу
@pytest.fixture
def chromium_page(playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=True)
    yield browser.new_page()
    browser.close()

# Инициализируем состояние входа через авторизацию и сохраняем контекст в browser-state.json
@pytest.fixture(scope='session')
def initialize_browser_state(playwright: Playwright):
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()

    registration_page = RegistrationPage(page=page)

    registration_page.visit(registration_url)

    registration_page.form.fill(email=email_data, username=username_data, password=password_data)
    registration_page.click_registration_btn()

    context.storage_state(path="browser-state.json")
    browser.close()

# Используем эту фикстуру уже с авторизованным состоянием на всех тестах где нужно быть уже авторизованным
@pytest.fixture
def chromium_page_with_state(initialize_browser_state, playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context(storage_state="browser-state.json")
    yield context.new_page()
    browser.close()
