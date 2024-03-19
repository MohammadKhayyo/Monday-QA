import unittest
from Utils import users
from infra.infra_ui.browser_wrapper import WebDriverManager
from logic.logic_ui.login_page import LoginPage
from logic.logic_ui.Sprints_page import SprintsPage
from logic.logic_ui.Home_page import HomePage


class SerialSprintsTests(unittest.TestCase):
    VALID_USERS = users.authentic_users

    def setUp(self):
        self.browser_wrapper = WebDriverManager()
        default_browser = 'chrome'
        self.browser = getattr(self.__class__, 'browser', default_browser)
        self.driver = self.browser_wrapper.initialize_web_driver(browser_name=self.browser)
        self.login_page = LoginPage(self.driver)
        user = self.VALID_USERS[0]
        self.login_page.login(user['email'], user['password'])
        self.sprint_Interface = SprintsPage(self.driver)
        self.home_page = HomePage(self.driver)
        self.home_page.changeEnvironment(environment_name="dev")

    def test_purge_sprints_with_identical_names(self):
        operationOutcome = self.sprint_Interface.removeSprint("New sprint", "all")
        self.assertTrue(operationOutcome, "Delete all sprints that have the name did not succeed")

    def test_revert_sprint_deletions(self):
        operationOutcome = self.sprint_Interface.revertAllSprintDeletions()
        self.assertTrue(operationOutcome, "Failed to undo the deletion of all sprints.")

    def tearDown(self):
        if self.driver:
            self.driver.quit()
