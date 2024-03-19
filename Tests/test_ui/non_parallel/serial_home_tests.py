import unittest
from Utils import users
from infra.infra_ui.browser_wrapper import WebDriverManager
from logic.logic_ui.login_page import LoginPage
from logic.logic_ui.Home_page import HomePage


class SerialHomeTests(unittest.TestCase):
    VALID_USERS = users.authentic_users

    def setUp(self):
        self.browser_wrapper = WebDriverManager()
        default_browser = 'chrome'  # Specify your default browser here
        self.browser = getattr(self.__class__, 'browser', default_browser)
        self.driver = self.browser_wrapper.initialize_web_driver(browser_name=self.browser)
        self.login_page = LoginPage(self.driver)
        user = self.VALID_USERS[0]
        self.login_page.login(user['email'], user['password'])
        self.home_page = HomePage(self.driver)
        self.home_page.changeEnvironment(environment_name="dev")

    def test_environment_switching(self):
        environment = self.home_page.changeEnvironment(environment_name="sales CRM")
        self.assertEqual(environment, "sales CRM", "Failed to switch to the sales CRM environment")
        environment = self.home_page.changeEnvironment(environment_name="dev")
        self.assertEqual(environment, "dev", "Failed to switch back to the development environment")

    def test_sign_out(self):
        operationResult = self.home_page.sign_out()
        self.assertTrue(operationResult, "Logout process failed")

    def tearDown(self):
        if self.driver:
            self.driver.quit()
