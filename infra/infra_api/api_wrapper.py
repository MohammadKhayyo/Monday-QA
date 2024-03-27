import json
from time import sleep
import os
import requests
from dotenv import load_dotenv
from Utils.configurations import ConfigurationManager

load_dotenv()


class MondayApi:
    def __init__(self, print_api_protocol=True):
        api_key = os.getenv("API_MONDAY")
        self.token = api_key
        self.print_api_protocol = print_api_protocol
        config_manager = ConfigurationManager()
        self.settings = config_manager.load_settings("config_api.json")
        self.apiUrl = self.settings["URL"]
        self.headers = {"Authorization": self.token}

    def send_request(self, query):
        data = {'query': query}
        if self.print_api_protocol:
            print("sending:", query)
        response_str = requests.post(url=self.apiUrl, json=data, headers=self.headers).text
        response = json.loads(response_str)
        return response

    def post_request(self, query, until_status_code_429=False):
        while True:
            response = self.send_request(query)
            if self.handle_response_errors(response=response, until_status_code_429=False):
                break
        try:
            if self.print_api_protocol:
                print("received:", response)
                print()
            return response['data']
        except:
            if self.print_api_protocol:
                print("untracked error in post request:")
                print("query:", query)
                print("error: ", response)
                print()
            return response

    def handle_response_errors(self, response, until_status_code_429=False):
        #  "status_code" in response and response["status_code"] == 429 and
        if 'errors' in response:
            print('errors:', response['errors'])
            errors = response['errors']
            for error in errors:
                if 'message' in error:
                    error_message = error['message']
                else:
                    error_message = error
                if 'Complexity budget exhausted' in error_message:
                    seconds_to_rest = 5
                    if 'reset in ' in error_message:
                        seconds_to_rest = error_message.split('reset in ')[1][:2]
                        seconds_to_rest = seconds_to_rest.strip()
                        if seconds_to_rest.isdigit():
                            seconds_to_rest = int(seconds_to_rest) + 1
                        else:
                            seconds_to_rest = 5
                    print("waiting for ", seconds_to_rest)
                    if until_status_code_429:
                        raise Exception("Too Many request")
                    sleep(seconds_to_rest)
                    return False
                else:
                    with open("../../errors.txt", "a") as file1:
                        file1.write(error_message)
            return False
        return True
