from logic.logic_api.work_space import WorkSpace
from infra.infra_api.api_wrapper import MondayApi
from logic.logic_api.group import Group


class Board:
    def __init__(self, work_space, board_name=None, board_id=None, exists=False, folder_id=None, folder_name=None):
        if board_id is None and board_name is None:
            raise ValueError("")
        if type(work_space) is not WorkSpace:
            raise ValueError("")
        self.work_space = work_space
        self.send_request = MondayApi()
        self.board_name = board_name
        self.board_id = board_id
        self.folder_id = folder_id
        self.columns = {}
        self.groups = {}
        if not exists:
            if self.board_name is None:
                raise ValueError("")
            if self.folder_id is None and folder_name is not None:
                folder_id, folder_name = self.work_space.get_folder_via_key(key='name', value=folder_name)
                self.folder_id = folder_id
            self.board_id = self.create_board(folder_id=self.folder_id)
            groups = self.get_all_group()
            for group in groups:
                self.delete_group(group_id=group["id"])
        else:
            boards_names = self.work_space.get_boards_in_work_space()
            for board_id, board_name in boards_names.items():
                if self.board_id is not None and board_id != self.board_id:
                    continue
                if self.board_name is not None and board_name != self.board_name:
                    continue
                self.board_id = board_id
                self.board_name = board_name
                # groups = self.get_all_group()
                # for group in groups:
                #     self.delete_group(group_id=group["id"])
                # Group(board=self, group_id=group["id"], exist=True).delete_group()
                break
            if self.board_id is None or self.board_name is None:
                raise ValueError("")

    def create_board(self, folder_id=None):
        query = 'mutation { create_board (board_name: "' + self.board_name + \
                '", board_kind: private, workspace_id: ' + str(self.work_space.id)
        if folder_id and folder_id in self.work_space.folders:
            query += ', folder_id: ' + str(folder_id) + ''
        query += ') { id } }'
        board_id = self.send_request.post_request(query)['create_board']['id']
        return board_id

    def delete_board(self):
        query = 'mutation { delete_board(board_id: "' + self.board_id + '") { state } }'
        response = self.send_request.post_request(query)
        deleted_status = response['delete_board']['state'] == "deleted"
        return deleted_status

    def get_all_group(self):
        groups = \
            self.send_request.post_request(query='{ boards (ids: ' + self.board_id + ') {id groups{id title}} }')[
                'boards'][0]['groups']
        return groups

    def get_all_columns(self):
        columns = \
            self.send_request.post_request(
                query='{ boards (ids: ' + self.board_id + ') { id columns{ id title type description } } }')[
                'boards'][0]['columns']
        return columns

    def get_column_vai_id(self, column_id):
        columns = self.get_all_columns()
        for column in columns:
            if column['id'] == column_id:
                return column

        return None

    def create_group(self, group_name):
        group = Group(self, group_name=group_name, exist=False)
        self.groups[group.group_id] = group.group_name

    def delete_group(self, group_id=None, group_name=None):
        group = Group(self, group_id=group_id, group_name=group_name, exist=True)
        group.delete_group()

    def get_work_space_vai_board(self):
        return \
            self.send_request.post_request(query='{boards(ids:' + self.board_id + ') {workspace{id name}}}')['boards'][
                0][
                'workspace']
