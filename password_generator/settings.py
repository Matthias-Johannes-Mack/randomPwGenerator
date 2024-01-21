import json


class Settings:
    
    @staticmethod
    def read_settings_json(file_path):
        """Read settings from a JSON file."""
        try:
            with open(file_path, "r") as file:
                settings = json.load(file)
            return settings
        except FileNotFoundError:
            print("JSON file not found! " + file_path)
            return {}

    @staticmethod
    def write_settings_json(file_path, settings):
        """Write settings to a JSON file."""
        with open(file_path, "w") as file:
            json.dump(settings, file, indent=4)
