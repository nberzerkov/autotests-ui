import sys
import platform

from config import settings

def create_allure_environment_file():
    setting_items = [f'{key}={value}' for key, value in settings.model_dump().items()]
    os_info = f'os_info={platform.system()}, {platform.release()}'

    python_ver_str = sys.version.replace("\n", " ")
    python_version = f"python_version={python_ver_str}"

    all_items = setting_items + [os_info, python_version]

    properties = '\n'.join(all_items)

    with open(settings.allure_results_dir.joinpath('environment.properties'), 'w+') as file:
        file.write(properties)
