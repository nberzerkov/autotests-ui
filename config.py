import os
from enum import Enum
from typing_extensions import Self

from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import EmailStr, FilePath, HttpUrl, DirectoryPath, BaseModel

# если env var в CONFIG_FILE не задан, то по дефолту берёт значение из ".env.local"
# если нужно на одну команду поменять окружение - CONFIG_FILE=.env.{name_env} python -m config
# если на сессию, то export CONFIG_FILE=.env.{name_env} и потом python -m config
config_file = os.getenv("CONFIG_FILE", ".env.local")

class Browser(str, Enum):
    CHROMIUM = "chromium"
    FIREFOX = "firefox"
    WEBKIT = "webkit"

class TestUser(BaseModel):
    email: EmailStr
    username: str
    password: str

class TestData(BaseModel):
    image_png_file: FilePath

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=(".env", config_file),
        env_file_encoding='utf-8',
        env_nested_delimiter='.',
    )

    app_url: HttpUrl
    headless: bool
    browser: list[Browser]
    test_user: TestUser
    test_data: TestData
    videos_dir: DirectoryPath
    tracing_dir: DirectoryPath
    browser_state_file: FilePath

    # если не хочешь морочиться с этим билдером, то просто создай необходимые папки, файлы и создай в них .gitkeep
    @classmethod
    def initialize(cls) -> Self:
        videos_dir = DirectoryPath("./videos")
        tracing_dir = DirectoryPath("./tracing")
        browser_state_file = FilePath("browser_state.json")

        # автоматически создаем необходимые файлы и папки чтобы не было ошибок при запуске
        videos_dir.mkdir(exist_ok=True)
        tracing_dir.mkdir(exist_ok=True)
        browser_state_file.touch(exist_ok=True)

        return Settings(
            videos_dir=videos_dir,
            tracing_dir=tracing_dir,
            browser_state_file=browser_state_file
        )


settings = Settings.initialize()
# print(Settings.initialize())
print("Loaded config file:", config_file)


















