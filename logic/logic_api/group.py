from infra.infra_api.api_wrapper import MondayApi


class Group:
    """
        Represents a group of a board.
    """

    def __init__(self, board, group_id=None, group_name=None, exist=False):
        if group_id is None and group_name is None:
            raise TypeError("")
        self.send_request = MondayApi()
        self.board = board
        self.items = {}
        if exist is False:
            if group_name is None:
                raise ValueError("")
            self.group_name = group_name
            self.create_group()
        else:
            group_details = None
            if group_id:
                group_details = self.check_group_via_key(key='id', value=group_id)
            elif group_name:
                group_details = self.check_group_via_key(key='title', value=group_name)
            if group_details is None:
                raise TypeError("")
            self.group_id = group_details['id']
            self.group_name = group_details['title']

    def create_group(self):
        group_details = self.send_request.post_request(
            query='mutation { create_group (board_id: ' + self.board.board_id + ', group_name: "' +
                  self.group_name + '") { id title} }')['create_group']
        self.group_id = group_details['id']
        self.group_name = group_details['title']

    def get_id(self, title):
        groups = \
            self.send_request.post_request(
                query='{ boards (ids: ' + self.board.board_id + ') {id groups {id title}}}')[
                'boards'][0]['groups']
        for group in groups:
            if group['title'] == title:
                return group['id']
        return ''

    def check_group_via_key(self, key, value):
        groups = self.board.get_all_group()

        for group in groups:
            if group[key] == value:
                return group
        return None

    def delete_group(self):
        return self.send_request.post_request(
            query='mutation { delete_group (board_id: ' + self.board.board_id + ', group_id: "' + self.group_id + '") { id deleted } }')

    def get_all_items_in_the_group(self):
        items = self.send_request.post_request(
            query='{ boards(ids:' + self.board.board_id + '){ groups(ids:"' + self.group_id + '"){ items_page{ items { id name } } } } }'
        )['boards'][0]['groups'][0]['items_page']['items']
        return items

# work_space = WorkSpace(work_space_name="MY_TEAM")
# print(work_space.id)
# board = Board(work_space=work_space, board_name="My_test_board", folder_id="873267", exists=False)
# group = Group(board=board, group_name="hi", exist=False)
# print(board.delete_board())
