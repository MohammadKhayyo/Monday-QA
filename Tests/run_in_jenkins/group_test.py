import unittest
import pytest
from infra.infra_api.api_wrapper import MondayApi
from logic.logic_api.work_space import WorkSpace
from logic.logic_api.board import Board
from logic.logic_api.group import Group
from Utils import generate_string
from infra.infra_jira.jira_wrapper import JiraWrapper
from Utils.error_handling import test_decorator
from parameterized import parameterized_class
from Utils.configurations import ConfigurationManager
from Utils.error_handling import test_decorator

config_manager = ConfigurationManager()
settings = config_manager.load_settings()
browser_types = [('chrome',)]


@pytest.mark.serial
@parameterized_class(('chrome',), browser_types)
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
        self.jira_client = JiraWrapper()
        self.test_failed = False
        self.error_msg = ""

    def tearDown(self):
        self.board.delete_board()
        if self.test_failed:
            self.test_name = self.id().split('.')[-1]
            summary = f"{self.test_name}"
            description = self.error_msg
            try:
                issue_key = self.jira_client.create_issue(summery=summary, description=description,
                                                          issue_type='Bug', project_key='KP')
                print(f"Jira issue created: {issue_key}")
            except Exception as e:
                print(f"Failed to create Jira issue: {e}")

    @test_decorator
    def test_create_and_delete_group(self):
        title = generate_string.create_secure_string()
        group = Group(board=self.board, group_name=title, exist=False)

        delete_group_details = group.delete_group()
        delete_status = delete_group_details['delete_group']['deleted']
        group_details = group.check_group_via_key(key='title', value=title)

        self.assertIsNone(group_details,
                          "Expected the group to be non-existent after deletion, but found details indicating it still exists.")
        self.assertTrue(delete_status,
                        "Expected the group deletion to be reported as successful, but the API response indicated failure.")
