import unittest
from infra.infra_api.api_wrapper import MondayApi
from logic.logic_api.work_space import WorkSpace
from logic.logic_api.board import Board
from logic.logic_api.group import Group
from logic.logic_api.item import Item
from logic.logic_api.column import Column


class ItemTest(unittest.TestCase):
    def setUp(self):
        self.send_request = MondayApi()
        self.work_space_name = "MY_TEAM"
        self.board_name = "MY_BOARD"
        self.folder_id = "888640"
        self.folder_name = "My Team"
        self.group_name = "MY_GROUP"
        self.work_space = WorkSpace(work_space_name=self.work_space_name)
        self.board = Board(work_space=self.work_space, board_name=self.board_name, folder_name=self.folder_name,
                           exists=False)
        self.group = Group(board=self.board, group_name=self.group_name, exist=False)

    def tearDown(self):
        self.board.delete_board()

    def test_create_item(self):
        item = Item(group=self.group, item_name="new_item_1", exist=False)
        item_details = item.get_item_via_key(key='title', value='Name', id=item.item_id)
        self.assertIsNone(item_details)

    def test_add_value_into_one_column(self):
        test_cases = [
            {"title": "Date", "column_type": "date", "description": "When the row was added to the board",
             "value": "2024-03-24"},
            {"title": "Favourite color", "column_type": "text", "description": "the favourite color of the row",
             "value": "blue"}
        ]
        for case in test_cases:
            with self.subTest(title=case["title"], column_type=case["column_type"], description=case["description"]):
                Column(board=self.board, title=case["title"], column_type=case["column_type"],
                       description=case["description"], exist=False)

            item = Item(group=self.group, item_name="new_item_1", exist=False,
                        columns_values=[(case['title'], case['value'])])

            item_details = item.get_item_via_key(key='title', value=case['title'], id=item.item_id)
            self.assertEqual(item_details['id'], item.item_id)
            self.assertEqual(item_details['column']['type'], case['column_type'])
            self.assertEqual(item_details['column']['title'], case['title'])
            self.assertEqual(item_details['column']['description'], case['description'])
            self.assertEqual(item_details['text'], case['value'])
            self.assertEqual(item_details['name'], item.item_name)

    def test_add_value_into_multiple_column(self):
        data_columns = [
            {"title": "Date", "column_type": "date", "description": "When the row was added to the board",
             "value": "2024-03-24"},
            {"title": "Favourite color", "column_type": "text", "description": "the favourite color of the row",
             "value": "blue"}
        ]
        columns_values = list()
        for data_column in data_columns:
            Column(board=self.board, title=data_column["title"], column_type=data_column["column_type"],
                   description=data_column["description"], exist=False)
            columns_values.append((data_column["title"], data_column["value"]))

        item = Item(group=self.group, item_name="new_item_1", exist=False,
                    columns_values=columns_values)
        for data_column in data_columns:
            item_details = item.get_item_via_key(key='title', value=data_column['title'], id=item.item_id)
            self.assertEqual(item_details['id'], item.item_id)
            self.assertEqual(item_details['column']['type'], data_column['column_type'])
            self.assertEqual(item_details['column']['title'], data_column['title'])
            self.assertEqual(item_details['column']['description'], data_column['description'])
            self.assertEqual(item_details['text'], data_column['value'])
            self.assertEqual(item_details['name'], item.item_name)

    def test_upload_one_file(self):
        data_column = {"title": "Attached Files", "column_type": "file", "description": "",
                       "files_paths": ["file1.txt"]}
        Column(board=self.board, title=data_column['title'], description=data_column['description'],
               column_type=data_column['column_type'])
        item = Item(group=self.group, item_name="new_item_1", exist=False)
        item.upload_files(column_title=data_column['title'], files_paths=data_column["files_paths"])
        item_details = item.get_item_via_key(key='title', value=data_column['title'], id=item.item_id)
        self.assertEqual(item_details['id'], item.item_id)
        self.assertEqual(item_details['column']['type'], data_column['column_type'])
        self.assertEqual(item_details['column']['title'], data_column['title'])
        self.assertEqual(item_details['column']['description'], data_column['description'])
        self.assertIsNotNone(item_details['text'])
        self.assertIn(data_column['files_paths'][0], item_details['text'])
        self.assertEqual(item_details['name'], item.item_name)

    def test_upload_multiple_files(self):
        data_column = {"title": "Attached Files", "column_type": "file", "description": "",
                       "files_paths": ["file1.txt", "file2.txt"]}
        Column(board=self.board, title=data_column['title'], description=data_column['description'],
               column_type=data_column['column_type'])
        item = Item(group=self.group, item_name="new_item_1", exist=False)
        item.upload_files(column_title=data_column['title'], files_paths=data_column["files_paths"])
        item_details = item.get_item_via_key(key='title', value=data_column['title'], id=item.item_id)
        self.assertEqual(item_details['id'], item.item_id)
        self.assertEqual(item_details['column']['type'], data_column['column_type'])
        self.assertEqual(item_details['column']['title'], data_column['title'])
        self.assertEqual(item_details['column']['description'], data_column['description'])
        self.assertIsNotNone(item_details['text'])
        for i in range(0, len(data_column['files_paths'])):
            self.assertIn(data_column['files_paths'][i], item_details['text'].split()[i])
            self.assertIn(data_column['files_paths'][i], item_details['text'].split()[i])
        self.assertEqual(item_details['name'], item.item_name)

    def test_add_link(self):
        data_column = {"title": "Link", "column_type": "link", "description": "A link to a website",
                       "link": "www.google.com", "placeholder": "search with google"}
        Column(board=self.board, title=data_column['title'], description=data_column['description'],
               column_type=data_column['column_type'])
        item = Item(group=self.group, item_name="new_item_1", exist=False)
        item.add_link(column_title=data_column['title'], link=data_column['link'],
                      description=data_column['placeholder'])
        item_details = item.get_item_via_key(key='title', value=data_column['title'], id=item.item_id)
        self.assertEqual(item_details['id'], item.item_id)
        self.assertEqual(item_details['column']['type'], data_column['column_type'])
        self.assertEqual(item_details['column']['title'], data_column['title'])
        self.assertEqual(item_details['column']['description'], data_column['description'])
        self.assertIsNotNone(item_details['text'])
        self.assertIn(data_column['link'], item_details['text'])
        self.assertIn(data_column['placeholder'], item_details['text'])
        self.assertEqual(item_details['name'], item.item_name)

    def test_set_rating(self):
        data_column = {"title": "Rating", "column_type": "rating", "description": "",
                       "value": "5"}
        Column(board=self.board, title=data_column['title'], description=data_column['description'],
               column_type=data_column['column_type'])
        item = Item(group=self.group, item_name="new_item_1", exist=False)
        item.set_rating(column_title=data_column['title'], value=data_column['value'])
        item_details = item.get_item_via_key(key='title', value=data_column['title'], id=item.item_id)
        self.assertEqual(item_details['id'], item.item_id)
        self.assertEqual(item_details['column']['type'], data_column['column_type'])
        self.assertEqual(item_details['column']['title'], data_column['title'])
        self.assertEqual(item_details['column']['description'], data_column['description'])
        self.assertIsNotNone(item_details['text'])
        self.assertEqual(data_column['value'], item_details['text'])
        self.assertEqual(item_details['name'], item.item_name)
