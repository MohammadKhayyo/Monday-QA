import cfbd
from Utils.configurations import ConfigurationManager
import json
from typing import List, Any, Callable


class APIWrapper:
    """
    APIWrapper serves as a utility class to interact with the college football data API.
    It simplifies fetching data and handling API responses.
    """

    def __init__(self):
        """
        Initializes the APIWrapper with API keys loaded from the configuration.
        """
        configuration = cfbd.Configuration()
        config_manager = ConfigurationManager()
        config_data = config_manager.load_settings("config_api.json")
        for key in config_data:
            configuration.api_key[key] = config_data[key]
        self.client = cfbd.ApiClient(configuration)

    @staticmethod
    def check_response_content(response_json, **kwargs):
        """
        Validates that all items in a JSON response match the specified key-value pairs.

        :param response_json: A JSON object or list of objects to check.
        :param kwargs: Key-value pairs to check against the JSON objects.
        :return: True if all items match, False otherwise.
        """
        if isinstance(response_json, str):
            try:
                response_json = json.loads(response_json)
            except json.JSONDecodeError:
                print("Failed to parse JSON.")
                return False
        elif not isinstance(response_json, list):
            print("Response is neither a JSON string nor a list.")
            return False
        for game in response_json:
            match = True
            for key, value in kwargs.items():
                if not hasattr(game, key) or getattr(game, key) != value:
                    match = False
                    break
            if match:
                return True

        return False

    def fetch_data(self, fetch_function: Callable, **kwargs) -> List[Any]:
        """
        Fetches data from the college football data API using the specified callable.

        :param fetch_function: The callable that makes the API call.
        :param kwargs: Keyword arguments to pass to the callable.
        :return: A list of data items fetched from the API.
        """
        try:
            data = fetch_function(**kwargs)
            print(f"Retrieved {len(data)} items.")
            return data
        except cfbd.ApiException as api_error:
            print(f"API exception occurred: {api_error}")
            raise
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            raise
