import allure

@allure.step("Opening browser")
def open_browser():
    with allure.step("Get browser"):
        ...
    with allure.step("Set browser"):
        ...


@allure.step("Creating title {description}")
def creating_course(title: str, description):
    with allure.step(f"Creating title {title}"):
        ...

@allure.step("Closing browser")
def close_browser():
    ...

def test_feature():
    open_browser()
    creating_course("Привет", "Как дела?")
    close_browser()
