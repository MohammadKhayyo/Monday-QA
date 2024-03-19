import unittest
from Utils import users
from infra.infra_ui.browser_wrapper import WebDriverManager
from logic.logic_ui.login_page import LoginPage
from logic.logic_ui.Tasks_page import TasksPage
from logic.logic_ui.Home_page import HomePage
from Utils import generate_string


class ParallelTasksTests(unittest.TestCase):
    VALID_USERS = users.authentic_users

    def setUp(self):
        self.browser_wrapper = WebDriverManager()
        default_browser = 'chrome'
        browser = getattr(self.__class__, 'browser', default_browser)
        self.driver = self.browser_wrapper.initialize_web_driver(browser_name=browser)
        self.login_page = LoginPage(self.driver)
        user = self.VALID_USERS[0]
        self.login_page.login(user['email'], user['password'])
        self.tasks_Interface = TasksPage(self.driver)
        self.home_page = HomePage(self.driver)
        self.home_page.changeEnvironment(environment_name="dev")

    def test_create_and_remove_task(self):
        unique_task_name = generate_string.create_secure_string()
        creation_success = self.tasks_Interface.create_task(unique_task_name)
        self.assertTrue(creation_success, "Failed to create and then delete the task.")
        deletion_success = self.tasks_Interface.remove_task(task_name=unique_task_name)
        self.assertTrue(deletion_success, "Task deletion did not proceed as expected.")

    def test_find_tasks_by_name(self):
        search_result = self.tasks_Interface.findTasksByName(name="New task")
        self.assertTrue(search_result, "Failed to find the specified task")

    def tearDown(self):
        if self.driver:
            self.driver.quit()
