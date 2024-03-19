import unittest
from Utils import users
from infra.infra_ui.browser_wrapper import WebDriverManager
from logic.logic_ui.login_page import LoginPage
from logic.logic_ui.Retrospectives_page import RetrospectivesPage
from logic.logic_ui.Home_page import HomePage


class SerialRetrospectivesTests(unittest.TestCase):
    VALID_USERS = users.authentic_users

    def setUp(self):
        self.browser_wrapper = WebDriverManager()
        default_browser = 'firefox'
        self.browser = getattr(self.__class__, 'browser', default_browser)
        self.driver = self.browser_wrapper.initialize_web_driver(browser_name=self.browser)
        self.login_page = LoginPage(self.driver)
        user = self.VALID_USERS[0]
        self.login_page.login(user['email'], user['password'])
        self.retrospective_Interface = RetrospectivesPage(self.driver)
        self.home_page = HomePage(self.driver)
        self.home_page.changeEnvironment(environment_name="dev")

    def test_bulk_delete_retrospectives_with_matching_name(self):
        outcome = self.retrospective_Interface.bulkDeleteRetrospectives("New feedback", "all")
        self.assertTrue(outcome, "Failed to undo the bulk deletion of retrospectives.")

    def test_revert_bulk_deletion_of_retrospectives(self):
        outcome = self.retrospective_Interface.revertBulkDeletion()
        self.assertTrue(outcome, "Failed to undo the bulk deletion of retrospectives.")

    def tearDown(self):
        if self.driver:
            self.driver.quit()
