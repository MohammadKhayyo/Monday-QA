import unittest
from Utils import users
from infra.infra_ui.browser_wrapper import WebDriverManager
from logic.logic_ui.login_page import LoginPage
from logic.logic_ui.Sprints_page import SprintsPage
from logic.logic_ui.Home_page import HomePage
from Utils import generate_string


class ParallelSprintsTests(unittest.TestCase):
    VALID_USERS = users.authentic_users

    def setUp(self):
        self.browser_wrapper = WebDriverManager()
        default_browser = 'chrome'
        self.browser = getattr(self.__class__, 'browser', default_browser)
        self.driver = self.browser_wrapper.initialize_web_driver(browser_name=self.browser)
        self.login_page = LoginPage(self.driver)
        user = self.VALID_USERS[0]
        self.login_page.login(user['email'], user['password'])
        self.sprints_Interface = SprintsPage(self.driver)
        self.home_page = HomePage(self.driver)
        self.home_page.changeEnvironment(environment_name="dev")

    def test_create_and_remove_sprint(self):
        sprint_name = generate_string.create_secure_string()
        creationStatus = self.sprints_Interface.createNewSprint(sprint_name)
        self.assertTrue(creationStatus, "Failed to create a new sprint.")
        deletionStatus = self.sprints_Interface.removeSprint(sprint_name)
        self.assertTrue(deletionStatus, "Failed to delete the sprint.")

    def test_find_sprints_by_name(self):
        search_result = self.sprints_Interface.findTasksByName(name="New sprint")
        self.assertTrue(search_result, "Failed to find the specified sprint")

    def tearDown(self):
        if self.driver:
            self.driver.quit()
