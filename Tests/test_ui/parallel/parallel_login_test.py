import unittest
from Utils import users
from infra.infra_ui.browser_wrapper import WebDriverManager
from logic.logic_ui.login_page import LoginPage

from parameterized import parameterized_class
from Utils.configurations import ConfigurationManager

config_manager = ConfigurationManager()
settings = config_manager.load_settings()
browser_types = [(browser,) for browser in settings["browser_types"]]


@parameterized_class(('browser',), browser_types)
class ParallelLoginTests(unittest.TestCase):
    VALID_USERS = users.authentic_users

    def setUp(self):
        self.browser_wrapper = WebDriverManager()
        default_browser = "chrome"
        self.browser = getattr(self.__class__, 'browser', default_browser)
        self.driver = self.browser_wrapper.initialize_web_driver(browser_name=self.browser)
        self.login_page = LoginPage(self.driver)

    def test_authenticate_valid_users(self):
        for user in self.VALID_USERS:
            status = self.login_page.login(user['email'], user['password'])
            self.assertTrue(status)

    def tearDown(self):
        if self.driver:
            self.driver.quit()
