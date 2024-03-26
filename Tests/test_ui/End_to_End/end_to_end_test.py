import unittest
from Utils import users
from infra.infra_ui.browser_wrapper import WebDriverManager
from logic.logic_ui.login_page import LoginPage
from logic.logic_ui.Tasks_page import TasksPage
from logic.logic_ui.Home_page import HomePage
from Utils import generate_string
from infra.infra_jira.jira_wrapper import JiraWrapper


# import pytest
# from parameterized import parameterized_class
# from Utils.configurations import ConfigurationManager
#
# config_manager = ConfigurationManager()
# settings = config_manager.load_settings()
# browser_types = [(browser,) for browser in settings["browser_types"]]
#
#
# @pytest.mark.serial
# @parameterized_class(('browser',), [
#     ('chrome',),
# ])
class EndToEnd(unittest.TestCase):
    VALID_USERS = users.authentic_users

    def setUp(self):
        self.browser_wrapper = WebDriverManager()
        default_browser = 'chrome'
        self.browser = getattr(self.__class__, 'browser', default_browser)
        self.driver = self.browser_wrapper.initialize_web_driver(browser_name=self.browser)
        self.login_page = LoginPage(self.driver)
        user = self.VALID_USERS[0]
        self.login_page.login(user['email'], user['password'])
        self.tasks_Interface = TasksPage(self.driver)
        self.home_page = HomePage(self.driver)
        self.home_page.changeEnvironment(environment_name="dev")
        self.jira_client = JiraWrapper()
        self.test_failed = False

    def test_create_and_remove_task(self):
        try:
            # self.assertFalse(True)
            unique_task_name = generate_string.create_secure_string()
            creation_success = self.tasks_Interface.create_task(unique_task_name)
            self.assertTrue(creation_success, "Failed to create and then delete the task.")
            deletion_success = self.tasks_Interface.remove_task(task_name=unique_task_name)
            self.assertTrue(deletion_success, "Task deletion did not proceed as expected.")
            self.tasks_Interface.click_undo_delete_button()
            list_all_elements_in_task_in_search = self.tasks_Interface.get_all_elements_in_task_in_search()
            self.assertEqual(len(list_all_elements_in_task_in_search), 1)
            self.assertEqual(list_all_elements_in_task_in_search[0], unique_task_name)
            self.tasks_Interface.click_on_the_big_X()
            self.tasks_Interface.clear_search_the_small_x()
            deletion_success = self.tasks_Interface.remove_task(task_name=unique_task_name)
            self.assertTrue(deletion_success, "Task deletion did not proceed as expected.")
            list_all_elements_in_task_in_search = self.tasks_Interface.get_all_elements_in_task_in_search()
            self.assertEqual(len(list_all_elements_in_task_in_search), 0)
            operationResult = self.home_page.sign_out()
            self.assertTrue(operationResult, "Logout process failed")
        except AssertionError as e:
            self.test_failed = True
            self.error_msg = str(e)
            raise

    def tearDown(self):

        if self.driver:
            self.driver.quit()

        self.test_name = self.id().split('.')[-1]
        if self.test_failed:
            summary = f"Test failed: {self.test_name} "
            description = f"{self.error_msg} browser {self.browser}"
            try:
                issue_key = self.jira_client.create_issue(summery=summary, description=description,
                                                          issue_type='Bug', project_key='KP')
                print(f"Jira issue created: {issue_key}")
            except Exception as e:
                print(f"Failed to create Jira issue: {e}")
