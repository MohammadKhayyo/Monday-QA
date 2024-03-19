import unittest
from Utils import users
from infra.infra_ui.browser_wrapper import WebDriverManager
from logic.logic_ui.login_page import LoginPage
from logic.logic_ui.Epics_page import EpicsPage
from logic.logic_ui.Home_page import HomePage


class SerialEpicsTests(unittest.TestCase):
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

    def test_bulk_epic_removal_by_name(self):
        operationStatus = self.epics_Page.bulkDeleteEpics("New epic", "all")
        self.assertTrue(operationStatus, "Bulk deletion of epics by name failed")

    def test_revert_bulk_epic_deletion(self):
        operationStatus = self.epics_Page.revertBulkDeletion()
        self.assertTrue(operationStatus, "Reverting bulk deletion of epics failed")

    def tearDown(self):
        if self.driver:
            self.driver.quit()
