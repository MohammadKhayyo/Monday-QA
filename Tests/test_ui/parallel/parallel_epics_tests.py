import unittest
from Utils import users
from infra.infra_ui.browser_wrapper import WebDriverManager
from logic.logic_ui.login_page import LoginPage
from logic.logic_ui.Epics_page import EpicsPage
from logic.logic_ui.Home_page import HomePage
from Utils import generate_string


class ParallelEpicsTests(unittest.TestCase):
    VALID_USERS = users.authentic_users

    def setUp(self):
        self.browser_wrapper = WebDriverManager()
        default_browser = 'firefox'  # Specify your default browser here
        self.browser = getattr(self.__class__, 'browser', default_browser)
        self.driver = self.browser_wrapper.initialize_web_driver(browser_name=self.browser)
        self.login_page = LoginPage(self.driver)
        user = self.VALID_USERS[0]
        self.login_page.login(user['email'], user['password'])
        self.epics_Page = EpicsPage(self.driver)
        self.home_page = HomePage(self.driver)
        self.home_page.changeEnvironment(environment_name="dev")

    def test_create_and_remove_epic(self):
        epic_name = generate_string.create_secure_string()
        creationOutcome = self.epics_Page.add_new_epic(epic_name)  # Use a unique name to ensure the test is reliable
        self.assertTrue(creationOutcome, "Failed to create a new epic")
        deletionOutcome = self.epics_Page.bulkDeleteEpics(epic_name)
        self.assertTrue(deletionOutcome, "Failed to delete the epic")

    def test_find_sprints_by_name(self):
        search_result = self.epics_Page.findTasksByName(name="New epic")
        self.assertTrue(search_result, "Failed to find the specified epic")

    def tearDown(self):
        if self.driver:
            self.driver.quit()
