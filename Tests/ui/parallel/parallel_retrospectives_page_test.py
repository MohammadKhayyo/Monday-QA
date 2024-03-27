import random
import unittest
from Utils import users
from infra.infra_ui.browser_wrapper import WebDriverManager
from logic.logic_ui.login_page import LoginPage
from logic.logic_ui.Retrospectives_page import RetrospectivesPage
from logic.logic_ui.Home_page import HomePage
from Utils import generate_string
from Utils.error_handling import test_decorator

from parameterized import parameterized_class
from Utils.configurations import ConfigurationManager
from infra.infra_jira.jira_wrapper import JiraWrapper

config_manager = ConfigurationManager()
settings = config_manager.load_settings()
browser_types = [(browser,) for browser in settings["browser_types"]]


@parameterized_class(('browser',), browser_types)
class ParallelRetrospectivesTests(unittest.TestCase):
    VALID_USERS = users.authentic_users

    def setUp(self):
        self.browser_wrapper = WebDriverManager()
        default_browser = 'chrome'
        self.browser = getattr(self.__class__, 'browser', default_browser)
        self.driver = self.browser_wrapper.initialize_web_driver(browser_name=self.browser)
        self.login_page = LoginPage(self.driver)
        user = self.VALID_USERS[0]
        self.login_page.login(user['email'], user['password'])
        self.retrospective_Interface = RetrospectivesPage(self.driver)
        self.home_page = HomePage(self.driver)
        self.home_page.changeEnvironment(environment_name="dev")
        self.jira_client = JiraWrapper()
        self.test_failed = False
        self.error_msg = ""

    @test_decorator
    def test_bulk_delete_retrospectives_with_matching_name(self):
        unique_task_name = generate_string.create_secure_string()
        random_number = random.randint(2, 5)
        for i in range(random_number):
            creationStatus = self.retrospective_Interface.add_new_retrospective(unique_task_name)
            self.assertTrue(creationStatus, "Creation of a new retrospective failed")
        outcome = self.retrospective_Interface.bulkDeleteRetrospectives(unique_task_name, "all")
        self.assertTrue(outcome, "Failed to undo the bulk deletion of retrospectives.")

    @test_decorator
    def test_create_and_remove_retrospective(self):
        task_name = generate_string.create_secure_string()
        creationStatus = self.retrospective_Interface.add_new_retrospective(task_name)
        self.assertTrue(creationStatus, "Creation of a new retrospective failed")
        deletionStatus = self.retrospective_Interface.bulkDeleteRetrospectives(task_name)
        self.assertTrue(deletionStatus, "Deletion of the retrospective failed")

    # def test_find_sprints_by_name(self):
    #     search_result = self.retrospective_Interface.findTasksByName(name="New feedback")
    #     self.assertTrue(search_result, "Failed to find the specified retrospective")

    def tearDown(self):
        if self.driver:
            self.driver.quit()
        if self.test_failed:
            self.test_name = self.id().split('.')[-1]
            summary = f"{self.test_name} "
            description = f"{self.error_msg} browser {self.browser}"
            try:
                issue_key = self.jira_client.create_issue(summery=summary, description=description,
                                                          issue_type='Bug', project_key='KP')
                print(f"Jira issue created: {issue_key}")
            except Exception as e:
                print(f"Failed to create Jira issue: {e}")
