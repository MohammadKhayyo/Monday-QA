import json
import os
from os.path import dirname, join, abspath


class ConfigurationManager:
    def __init__(self):
        # The root of the project is assumed to be two levels up from this file
        self.project_root = dirname(dirname(abspath(__file__)))

    def get_filename(self, filename):
        # Construct the path to the filename in the config directory
        output = join(self.project_root, 'configs', filename)
        return output

    def load_settings(self, file_name="config_ui.json"):
        """Loads configuration settings from a JSON file."""
        file_path = self.get_filename(file_name)
        with open(file_path, 'r') as file:
            config = json.load(file)
        return config
