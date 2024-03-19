import requests
import json


class WorkSpace:
    def __init__(self, name, token, work_space_id=1482559):
        self.name = name
        self.token = token
        self.apiUrl = "https://api.monday.com/v2"
        self.headers = {"Authorization": self.token}
        self.work_space_id = work_space_id

    def post_request(self, query):
        data = {'query': query}
        response_str = requests.post(url=self.apiUrl, json=data, headers=self.headers).text
        response = json.loads(response_str)
        return response['data']


class Board:
    def __init__(self, ws, name):
        self.work_space = ws
        self.name = name
        query = 'mutation { create_board (board_name: "' + self.name + \
                '", board_kind: private, workspace_id: ' + str(self.work_space.work_space_id) + ') { id } }'
        print(query)
        self.board_id = self.work_space.post_request(query)['create_board']['id']


# api_key = "eyJhbGciOiJIUzI1NiJ9.eyJ0aWQiOjMzMzM1NjEzOSwiYWFpIjoxMSwidWlkIjo1NjkyNDM3MiwiaWFkIjoiMjAyNC0wMy0xNVQwNzo0MjowMS42NTZaIiwicGVyIjoibWU6d3JpdGUiLCJhY3RpZCI6MjE3NDM4ODMsInJnbiI6ImV1YzEifQ.sQXv-gJ59t13myfuIIrC7B3TLrcpcwV3O7lR2J0N-Dw"
# work_space = WorkSpace(name="MY_TEAM", token=api_key)
# my_board = Board(ws=work_space, name="My_terrific_board")
