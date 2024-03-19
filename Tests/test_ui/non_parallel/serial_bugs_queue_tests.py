import unittest
from Utils import users
from infra.infra_ui.browser_wrapper import WebDriverManager
from logic.logic_ui.login_page import LoginPage
from logic.logic_ui.Bugs_Queue_page import BugsQueuePage
from logic.logic_ui.Home_page import HomePage


class BugsQueueTests(unittest.TestCase):
    VALID_USERS = users.authentic_users

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

    def test_bulk_delete_bugs_with_matching_name(self):
        operationOutcome = self.bugs_queue_page.bulkDeleteBugs("New bug", "all")
        self.assertTrue(operationOutcome, "Bulk deletion of bugs by name failed")

    def test_revert_bulk_deletion_of_bugs(self):
        operationOutcome = self.bugs_queue_page.revertBulkBugDeletion()
        self.assertTrue(operationOutcome, "Reverting bulk deletion of bugs failed")

    def tearDown(self):
        if self.driver:
            self.driver.quit()
