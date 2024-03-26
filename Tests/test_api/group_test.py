import unittest
from infra.infra_api.api_wrapper import MondayApi
from logic.logic_api.work_space import WorkSpace
from logic.logic_api.board import Board
from logic.logic_api.group import Group
from Utils import generate_string


class GroupTest(unittest.TestCase):
    def setUp(self):
        self.send_request = MondayApi()
        self.work_space_name = "MY_TEAM"
        self.board_name = generate_string.create_secure_string()
        self.folder_id = "888640"
        self.folder_name = "My Team"
        self.group_name = generate_string.create_secure_string()
        self.work_space = WorkSpace(work_space_name=self.work_space_name)
        self.board = Board(work_space=self.work_space, board_name=self.board_name, folder_name=self.folder_name,
                           exists=False)

        self.group = Group(board=self.board, group_name=self.group_name, exist=False)

    def tearDown(self):
        self.board.delete_board()

    def test_get_group_via_title(self):
        group_details = self.group.check_group_via_key(key='title', value=self.group_name)
        self.assertEqual(group_details['id'], self.group.group_id)
        self.assertEqual(group_details['title'], self.group.group_name)

    def test_get_group_via_id(self):
        group_details = self.group.check_group_via_key(key='id', value=self.group.group_id)
        self.assertEqual(group_details['id'], self.group.group_id)
        self.assertEqual(group_details['title'], self.group.group_name)

    def test_create_and_delete_group(self):
        title = generate_string.create_secure_string()
        group = Group(board=self.board, group_name=title, exist=False)
        # group_details = self.group.check_group_via_key(key='title', value=title)
        # self.assertEqual(group_details['id'], group.group_id)
        # self.assertEqual(group_details['title'], group.group_name)
        delete_group_details = group.delete_group()
        delete_status = delete_group_details['delete_group']['deleted']
        group_details = group.check_group_via_key(key='title', value=title)
        self.assertIsNone(group_details)
        self.assertTrue(delete_status)

    def test_items_in_new_group(self):
        items = self.group.get_all_items_in_the_group()
        self.assertEqual(len(items), 0)
