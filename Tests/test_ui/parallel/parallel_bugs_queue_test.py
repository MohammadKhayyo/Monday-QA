import unittest
from Utils import users
from infra.infra_ui.browser_wrapper import WebDriverManager
from logic.logic_ui.login_page import LoginPage
from logic.logic_ui.Bugs_Queue_page import BugsQueuePage
from logic.logic_ui.Home_page import HomePage
from Utils import generate_string


class ParallelBugsQueueTests(unittest.TestCase):
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

    def test_add_retrospectives_and_and_delete_it(self):
        unique_bug_name = generate_string.create_secure_string()
        creationSuccess = self.bugs_queue_page.add_new_bugs_queue(unique_bug_name)
        self.assertTrue(creationSuccess, "Failed to add a new bug to the queue")
        deletionSuccess = self.bugs_queue_page.bulkDeleteBugs(unique_bug_name)
        self.assertTrue(deletionSuccess, "Failed to remove the bug from the queue")

    def test_find_sprints_by_name(self):
        search_result = self.bugs_queue_page.findTasksByName(name="Birthday notification")
        self.assertTrue(search_result, "Failed to find the specified bug")

    def tearDown(self):
        if self.driver:
            self.driver.quit()
