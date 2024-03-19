import unittest
from Utils import users
from infra.infra_ui.browser_wrapper import WebDriverManager
from logic.logic_ui.login_page import LoginPage
from logic.logic_ui.Tasks_page import TasksPage
from logic.logic_ui.Home_page import HomePage


class SerialTasksTests(unittest.TestCase):
    VALID_USERS = users.authentic_users

    def setUp(self):
        self.browser_wrapper = WebDriverManager()
        default_browser = 'chrome'
        self.browser = getattr(self.__class__, 'browser', default_browser)
        self.driver = self.browser_wrapper.initialize_web_driver(browser_name=self.browser)
        self.login_page = LoginPage(self.driver)
        user = self.VALID_USERS[0]
        self.login_page.login(user['email'], user['password'])
        self.task_Interface = TasksPage(self.driver)
        self.home_page = HomePage(self.driver)
        self.home_page.changeEnvironment(environment_name="dev")

    def test_purge_duplicate_tasks(self):
        operationSuccess = self.task_Interface.remove_task("New task", "all")
        self.assertTrue(operationSuccess, "Failed to purge all tasks with the same name.")

    def test_mass_undo_task_deletions(self):
        operationSuccess = self.task_Interface.revertAllTaskDeletions()
        self.assertTrue(operationSuccess, "Failed to undo the deletion of all tasks.")

    def tearDown(self):
        if self.driver:
            self.driver.quit()
