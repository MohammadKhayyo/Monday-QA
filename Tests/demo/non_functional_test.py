import unittest
from infra.infra_api.api_wrapper import MondayApi
from logic.logic_api.work_space import WorkSpace
from Utils import generate_string
from Utils.hadling_error_429 import create_board, delete_board
from infra.infra_jira.jira_wrapper import JiraWrapper
from Utils.error_handling import test_decorator


class BoardTest(unittest.TestCase):
    def setUp(self):
        self.send_request = MondayApi()
        self.work_space_name = "MY_TEAM"
        self.folder_id = "888640"
        self.folder_name = "My Team"
        self.work_space = WorkSpace(work_space_name=self.work_space_name)
        self.work_space_id = self.work_space.id
        self.jira_client = JiraWrapper()
        self.test_failed = False
        self.error_msg = ""

    def tearDown(self):
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
    def test_reach_error_429(self):
        unique_name = generate_string.create_secure_string()
        try:
            while True:
                board_id = create_board(self.work_space_id, unique_name)
                delete_board(board_id)
        except Exception as e:
            print(e)
