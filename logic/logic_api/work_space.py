from infra.infra_api.api_wrapper import MondayApi


class WorkSpace:

    def __init__(self, work_space_id=None, work_space_name=None):
        # {'id': '1482559', 'name': 'MY_TEAM'}
        self.boards = dict()
        self.send_request = MondayApi()
        ws = None
        if work_space_id is not None:
            ws = self.check_workspace_via_key(work_space_id, 'id')
        elif work_space_name is not None:
            ws = self.check_workspace_via_key(work_space_name, 'name')
        if ws:
            self.name = ws['name']
            self.id = ws['id']
            self.folders = self.get_folders_in_work_space()
        else:
            raise Exception("")

    def get_monday_workspaces(self):
        query = """
        {
          workspaces {
            id
            name
          }
        }
        """
        return self.send_request.post_request(query=query)

    def check_workspace_via_key(self, workspace_key, key):
        workspaces_names = self.get_monday_workspaces()
        for workspace in workspaces_names['workspaces']:
            if workspace and key in workspace and type(workspace[key]) == str and workspace[
                key] == workspace_key:
                return workspace
        return None

    def get_boards_in_work_space(self, id_work_space=None, boards_limit=500):
        if id_work_space is None:
            id_work_space = self.id
        boards = dict()
        boards_names = self.send_request.post_request(query='{ boards (limit:' + str(boards_limit) +
                                                            ') {id name workspace {id name} }}')
        for board in boards_names['boards']:
            if not board['workspace'] or not board['workspace']['id'] == id_work_space:
                continue
            boards[board['id']] = board['name']
        return boards

    def get_board_via_id(self, value):
        boards = self.get_boards_in_work_space()
        for board_id, board_name in boards.items():
            if board_id == value:
                return board_id, board_name
        return None, None

    def get_folders_in_work_space(self, id_work_space=None):
        folders = dict()
        if id_work_space is None:
            id_work_space = self.id
        folders_names = self.send_request.post_request(query='{ folders (workspace_ids:' + str(id_work_space) +
                                                             ') {id name}}')
        for folder in folders_names['folders']:
            folders[folder['id']] = folder['name']
        return folders

    def get_folder_via_key(self, key, value):
        folders = self.get_folders_in_work_space()
        for folder_id, folder_name in folders.items():
            if key == 'id' and folder_id == value:
                return folder_id, folder_name
            elif key == 'name' and folder_name == value:
                return folder_id, folder_name
        return None, None

    def get_all_boards(self):
        boards_names = self.send_request.post_request(query='{ boards {id name workspace {id name} }}')
        return boards_names['boards']


# api_key = "eyJhbGciOiJIUzI1NiJ9.eyJ0aWQiOjMzMzM1NjEzOSwiYWFpIjoxMSwidWlkIjo1NjkyNDM3MiwiaWFkIjoiMjAyNC0wMy0xNVQwNzo0MjowMS42NTZaIiwicGVyIjoibWU6d3JpdGUiLCJhY3RpZCI6MjE3NDM4ODMsInJnbiI6ImV1YzEifQ.sQXv-gJ59t13myfuIIrC7B3TLrcpcwV3O7lR2J0N-Dw"
work_space = WorkSpace(work_space_name="MY_TEAM")
# # _work_space = WorkSpace(work_space_id="1482559")
# # work_space.get_boards_in_work_space()
print(work_space.get_folders_in_work_space())
print(work_space.get_folder_via_key(key='name', value="My Team"))
# print()
