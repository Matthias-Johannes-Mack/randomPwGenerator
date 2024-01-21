import locale
from settings import Settings
import os
import sys

def restart_application():
    """Restart the current Python script."""
    python = sys.executable
    os.execl(python, python, *sys.argv)


def get_current_country_code():
    current_locale = locale.getlocale()

    if current_locale[0]:  # Check if language code is not empty
        _, country_code = current_locale[0].split("_")
        return country_code.lower()
    return None


def load_settings():
    # Instantiate the Settings class
    settings_manager = Settings()
    settings_file_path = "settings.json"
    settings = settings_manager.read_settings_json(settings_file_path)
    return settings_manager.read_settings_json(settings_file_path)


def store_locale(new_locale):
    settings_manager = Settings()
    settings_file_path = "settings.json"
    settings = load_settings()
    settings["locale"] = new_locale
    settings_manager.write_settings_json(settings_file_path, settings)