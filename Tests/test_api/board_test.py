import unittest
from infra.infra_api.api_wrapper import MondayApi
from logic.logic_api.work_space import WorkSpace
from logic.logic_api.board import Board
from logic.logic_api.group import Group


class BoardTest(unittest.TestCase):
    def setUp(self):
        self.send_request = MondayApi()
        self.work_space_name = "MY_TEAM"
        self.board_name = "MY_BOARD"
        self.folder_id = "888640"
        self.folder_name = "My Team"
        self.work_space = WorkSpace(work_space_name=self.work_space_name)
        self.board = Board(work_space=self.work_space, board_name=self.board_name, folder_name=self.folder_name,
                           exists=False)

    def tearDown(self):
        self.board.delete_board()

    def test_get_board(self):
        board_id, board_name = self.work_space.get_board_via_id(value=self.board.board_id)
        self.assertEqual(board_id, self.board.board_id)
        self.assertEqual(board_name, self.board.board_name)

    def test_get_groups(self):
        groups = self.board.get_all_group()
        self.assertEqual(len(groups), 1)
        self.assertEqual(groups[0]['title'], 'Group Title')

    def test_get_columns(self):
        columns = self.board.get_all_columns()
        self.assertEqual(len(columns), 1)
        self.assertEqual(columns[0]['title'], 'Name')

    def test_get_items(self):
        group_details = self.board.get_all_group()
        group = Group(board=self.board, group_id=group_details[0]['id'], exist=True)
        items = group.get_all_items_in_the_group()
        self.assertEqual(len(items), 1)
        self.assertEqual(items[0]['name'], 'Task 1')

    def test_get_workspace(self):
        work_space_details = self.board.get_work_space_vai_board()
        self.assertEqual(self.work_space_name, work_space_details['name'])

    def test_delete_the_only_one_group(self):
        group_details = self.board.get_all_group()
        group = Group(board=self.board, group_id=group_details[0]['id'], exist=True)
        delete_group_details = group.delete_group()
        # group_details = group.check_group_via_key(key='title', value=group.group_name)
        self.assertEqual(delete_group_details['error_code'], 'DeleteLastGroupException')
        self.assertEqual(delete_group_details['status_code'], 409)
        # self.assertIsNotNone(group_details)
        # self.assertEqual(group_details['title'], group.group_name)
        # self.assertEqual(group_details['id'], group.group_id)
