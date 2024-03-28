import unittest
from infra.infra_api.api_wrapper import MondayApi
from logic.logic_api.work_space import WorkSpace
from logic.logic_api.board import Board
from logic.logic_api.group import Group
from Utils import generate_string
from infra.infra_jira.jira_wrapper import JiraWrapper
from Utils.error_handling import test_decorator
from Utils.upload_file_helper import upload_file_helper, returning_local_file_names, \
    returning_file_names_from_the_website, get_item_details
from time import sleep

time_sleep = 10


class ItemTest(unittest.TestCase):
    def setUp(self):
        self.send_request = MondayApi()
        self.work_space_name = "MY_TEAM"
        self.board_name = generate_string.create_secure_string()
        self.folder_name = "My Team"
        self.group_name = generate_string.create_secure_string()
        self.item_name = generate_string.create_secure_string()
        self.work_space = WorkSpace(work_space_name=self.work_space_name)
        sleep(time_sleep)
        self.board = Board(work_space=self.work_space, board_name=self.board_name, folder_name=self.folder_name,
                           exists=False)
        sleep(time_sleep)
        self.group = Group(board=self.board, group_name=self.group_name, exist=False)
        sleep(time_sleep)
        self.jira_client = JiraWrapper()
        self.test_failed = False
        self.error_msg = ""

    def tearDown(self):
        self.board.delete_board()
        if self.test_failed:
            self.test_name = self.id().split('.')[-1]
            summary = f"{self.test_name}"
            description = self.error_msg
            self.jira_client.create_issue(summary, description)

    @test_decorator
    def test_upload_file(self):
        files_path = ["file1.txt"]  # , "../../file2.txt"
        data_column = {"title": "Attached Files", "column_type": "file", "description": "",
                       "files_paths": files_path}
        sleep(time_sleep)
        item = upload_file_helper(self.item_name, self.board, self.group, data_column)
        website_files_details = get_item_details(item, data_column)
        website_file_names = returning_file_names_from_the_website(website_files_details)
        local_file_names = returning_local_file_names(files_path)
        sleep(time_sleep)

        self.assertListEqual(local_file_names, website_file_names,
                             "The file names retrieved from the website do not match the file names uploaded from the local system.")
