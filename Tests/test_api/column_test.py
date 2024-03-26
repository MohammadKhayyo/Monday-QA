import unittest
from infra.infra_api.api_wrapper import MondayApi
from logic.logic_api.work_space import WorkSpace
from logic.logic_api.board import Board
from logic.logic_api.column import Column
from Utils import generate_string


class ColumnTest(unittest.TestCase):
    def setUp(self):
        self.send_request = MondayApi()
        self.work_space_name = "MY_TEAM"
        unique_name = generate_string.create_secure_string()
        self.board_name = unique_name
        self.folder_id = "888640"
        self.folder_name = "My Team"
        self.work_space = WorkSpace(work_space_name=self.work_space_name)
        self.board = Board(work_space=self.work_space, board_name=self.board_name, folder_name=self.folder_name,
                           exists=False)

    def tearDown(self):
        self.board.delete_board()

    def test_create_and_delete_columns(self):
        test_cases = [
            {"title": "Date", "column_type": "date", "description": "When the row was added to the board"},
            {"title": "Favourite color", "column_type": "text", "description": "the favourite color of the row"},
            {"title": "Link", "column_type": "link", "description": "A link to a website"},
            {"title": "Attached Files", "column_type": "file", "description": ""},
            {"title": "Rating", "column_type": "rating", "description": ""}
        ]
        for case in test_cases:
            with self.subTest(title=case["title"], column_type=case["column_type"], description=case["description"]):
                column = Column(board=self.board, title=case["title"], column_type=case["column_type"],
                                description=case["description"], exist=False)
                column_details = self.board.get_column_vai_id(column_id=column.column_id)
                self.assertIsNotNone(column_details)
                self.assertEqual(column_details['id'], column.column_id)
                self.assertEqual(column_details['title'], column.column_name)

        for case in test_cases:
            with self.subTest(title=case["title"], column_type=case["column_type"], description=case["description"]):
                column = Column(board=self.board, title=case["title"], column_type=case["column_type"],
                                description=case["description"], exist=True)
                id_deleted_column = column.delete_column()
                self.assertEqual(id_deleted_column, column.column_id)
                column_details = self.board.get_column_vai_id(column_id=column.column_id)
                self.assertIsNone(column_details)
