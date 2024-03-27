import unittest
from infra.infra_api.api_wrapper import MondayApi
from logic.logic_api.work_space import WorkSpace
from logic.logic_api.board import Board
from logic.logic_api.group import Group
from logic.logic_api.item import Item
from logic.logic_api.column import Column
from Utils import generate_string
from infra.infra_jira.jira_wrapper import JiraWrapper
from Utils.error_handling import test_decorator


class ItemTest(unittest.TestCase):
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
        self.jira_client = JiraWrapper()
        self.test_failed = False
        self.error_msg = ""

    def tearDown(self):
        self.board.delete_board()
        if self.test_failed:
            self.test_name = self.id().split('.')[-1]
            summary = f"{self.test_name}"
            description = self.error_msg
            issue_key = self.jira_client.create_issue(summery=summary, description=description,
                                                      issue_type='Bug', project_key='KP')
            print(f"Jira issue created: {issue_key}" if issue_key else "Failed to create Jira issue")

    @test_decorator
    def test_upload_one_file(self):
        files_path = ["file1.txt"]  # , "../../file2.txt"
        data_column = {"title": "Attached Files", "column_type": "file", "description": "",
                       "files_paths": files_path}
        item_name = generate_string.create_secure_string()
        Column(board=self.board, title=data_column['title'], description=data_column['description'],
               column_type=data_column['column_type'])
        item = Item(group=self.group, item_name=item_name, exist=False)
        item.upload_files(column_title=data_column['title'], files_paths=data_column["files_paths"])
        item_details = item.get_item_via_key(key='title', value=data_column['title'], id=item.item_id)
        local_file_names = item.returning_local_file_names(files_path)
        website_file_names = item.returning_file_names_from_the_website(item_details['text'])
        self.assertListEqual(local_file_names, website_file_names)
