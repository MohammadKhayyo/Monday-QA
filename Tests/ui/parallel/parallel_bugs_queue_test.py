import random
import unittest
from Utils import users
from infra.infra_ui.browser_wrapper import WebDriverManager
from logic.logic_ui.login_page import LoginPage
from logic.logic_ui.Bugs_Queue_page import BugsQueuePage
from logic.logic_ui.Home_page import HomePage
from Utils import generate_string
from infra.infra_jira.jira_wrapper import JiraWrapper
import pytest
from parameterized import parameterized_class
from Utils.configurations import ConfigurationManager
from Utils.error_handling import test_decorator

config_manager = ConfigurationManager()
settings = config_manager.load_settings()
browser_types = [(browser,) for browser in settings["browser_types"]]


@parameterized_class(('browser',), browser_types)
class ParallelBugsQueueTests(unittest.TestCase):
    VALID_USERS = users.authentic_user

    def setUp(self):
        self.browser_wrapper = WebDriverManager()
        default_browser = 'chrome'
        self.browser = getattr(self.__class__, 'browser', default_browser)
        self.driver = self.browser_wrapper.initialize_web_driver(browser_name=self.browser)
        self.login_page = LoginPage(self.driver)
        user = self.VALID_USERS[0]
        self.login_page.login(user['email'], user['password'])
        self.bugs_queue_page = BugsQueuePage(self.driver)
        self.home_page = HomePage(self.driver)
        self.home_page.changeEnvironment(environment_name="dev")
        self.jira_client = JiraWrapper()
        self.test_failed = False
        self.error_msg = ""

    @test_decorator
    def test_bulk_delete_bugs_with_matching_name(self):
        unique_bug_name = generate_string.create_secure_string()
        random_number = random.randint(2, 5)
        for i in range(random_number):
            creationSuccess = self.bugs_queue_page.add_new_bugs_queue(unique_bug_name)
            self.assertTrue(creationSuccess, "Failed to add a new bug to the queue")
        operationOutcome = self.bugs_queue_page.bulkDeleteBugs(unique_bug_name, "all")
        self.assertTrue(operationOutcome, "Bulk deletion of bugs by name failed")

    @test_decorator
    def test_add_retrospectives_and_and_delete_it(self):
        unique_bug_name = generate_string.create_secure_string()
        creationSuccess = self.bugs_queue_page.add_new_bugs_queue(unique_bug_name)
        self.assertTrue(creationSuccess, "Failed to add a new bug to the queue")
        deletionSuccess = self.bugs_queue_page.bulkDeleteBugs(unique_bug_name)
        self.assertTrue(deletionSuccess, "Failed to remove the bug from the queue")

    # def test_find_sprints_by_name(self):
    #     search_result = self.bugs_queue_page.findTasksByName(name="Birthday notification")
    #     self.assertTrue(search_result, "Failed to find the specified bug")

    def tearDown(self):
        if self.driver:
            self.driver.quit()
        if self.test_failed:
            self.test_name = self.id().split('.')[-1]
            summary = f"{self.test_name}"
            description = f"{self.error_msg} browser {self.browser}"
            try:
                issue_key = self.jira_client.create_issue(summery=summary, description=description,
                                                          issue_type='Bug', project_key='KP')
                print(f"Jira issue created: {issue_key}")
            except Exception as e:
                print(f"Failed to create Jira issue: {e}")
