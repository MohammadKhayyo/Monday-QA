import requests
import json
from infra.infra_api.api_wrapper import MondayApi


class Item:
    """
        Represents an item of a group.
    """

    def __init__(self, group, item_name=None, item_id=None, columns_values=[], exist=False):
        self.group = group
        self.item_id = item_id
        self.item_name = item_name
        self.columns_values = {}
        self.send_request = MondayApi()

        # The item already exists in monday.
        if exist is False:
            if item_name is None:
                raise ValueError("")
            self.create_item(columns_values)
        else:
            item_details = None
            if item_id:
                item_details = self.check_item_via_key(key='id', value=item_id)
            elif item_name:
                item_details = self.check_item_via_key(key='name', value=item_name)
            if item_details is None:
                raise TypeError("")
            self.item_id = item_details['id']
            self.item_name = item_details['name']
            # self.create_item(columns_values)

    def check_item_via_key(self, key, value):
        items = self.group.get_all_items_in_the_group()

        for item in items:
            if item[key] == value:
                return item
        return None

    def create_item(self, columns_values):
        columns_values_json = '{'

        for column_title, value in columns_values:
            if type(value) is str:
                columns_values_json += '\\\"' + self.group.board.columns[
                    column_title].column_id + '\\\": \\\"' + value + '\\\"' + ', '
            elif type(value) is dict:
                columns_values_json += '\\\"' + self.group.board.columns[
                    column_title].column_id + '\\\": ' + json.dumps(value) + ', '

        # Remove the last ,.
        if len(columns_values_json) > 1:
            columns_values_json = columns_values_json[:-2]

        columns_values_json += '}'

        # Add the item to monday and save its id.
        self.item_id = self.send_request.post_request(
            query='mutation {create_item (board_id: ' + self.group.board.board_id + ', group_id: "' +
                  self.group.group_id + '", item_name: "' + self.item_name + '", column_values: "' +
                  columns_values_json + '") { id } }')['create_item']['id']

    def upload_files(self, column_title, files_paths):
        for file_path in files_paths:
            self.upload_file(column_title=column_title, file_path=file_path)

    def upload_file(self, column_title, file_path):
        query = 'mutation ($file: File!) { add_file_to_column (file: $file, item_id: ' + self.item_id + \
                ', column_id: "' + self.group.board.columns[column_title].column_id + '") {id }}'
        files = [('variables[file]', (file_path, open(file_path, 'rb'), 'multipart/form-data'))]
        data = {'query': query}
        if self.send_request.print_api_protocol:
            print("sending:", query)
        response_str = requests.post(url="https://api.monday.com/v2/file",
                                     headers={'Authorization': self.send_request.token}, data=data,
                                     files=files).text
        response = json.loads(response_str)

        # Check if any errors occurred.
        if not self.send_request.handle_response_errors(response=response):
            # An error occurred, try to upload the file again.
            return self.upload_file(column_title=column_title, file_path=file_path)

        if self.send_request.print_api_protocol:
            print("response:", response)

    def add_link(self, column_title, link, description=''):
        if not description:
            description = link
        query = 'mutation { change_column_value (board_id: ' + self.group.board.board_id + ', item_id: ' + \
                self.item_id + ', column_id: "' + \
                self.group.board.columns[
                    column_title].column_id + '", value: "{\\\"url\\\":\\\"' + link + '\\\",\\\"text\\\":\\\"' + \
                description + '\\\"}") { id } }'

        # Execute.
        self.send_request.post_request(query=query)

    def set_rating(self, column_title, value):
        query = 'mutation { change_column_value (board_id: ' + self.group.board.board_id + ', item_id: ' + \
                self.item_id + ', column_id: "' + \
                self.group.board.columns[
                    column_title].column_id + '", value: "{\\\"rating\\\":' + value + '}") { id } }'

        # Execute.
        self.send_request.post_request(query=query)

    def get_item_via_key(self, id, key, value):
        items_details = self.send_request.post_request(
            query='{ boards(ids: ' + self.group.board.board_id + ') { groups(ids: ' + '"' + str(
                self.group.group_id) + '"' + ') { items_page { items { id name column_values { column { id type title description } id text } } } } } }')[
            'boards'][0]['groups'][0]['items_page']['items']
        for item_details in items_details:
            if item_details['id'] != id:
                continue
            column_values = item_details['column_values']
            for column in column_values:
                column_details = column['column']
                if key in column_details and column_details[key] == value:
                    column['id'] = item_details['id']
                    column['name'] = item_details['name']
                    return column
            return None

    def returning_local_file_names(self, files_names):
        local_file_names = list()
        for i in range(0, len(files_names)):
            local_file_names.append(files_names[i].split('/')[-1])
        local_file_names.sort()
        return local_file_names

    def returning_file_names_from_the_website(self, files_names):
        website_file_names = list()
        files_names = files_names.split(',')
        for i in range(0, len(files_names)):
            website_file_names.append(files_names[i].split('/')[-1])
        website_file_names.sort()
        return website_file_names
