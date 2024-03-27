import unittest
from Utils import users
from infra.infra_ui.browser_wrapper import WebDriverManager
from logic.logic_ui.login_page import LoginPage
from logic.logic_ui.Home_page import HomePage
from infra.infra_jira.jira_wrapper import JiraWrapper
import pytest
from parameterized import parameterized_class
from Utils.configurations import ConfigurationManager
from Utils.error_handling import test_decorator

config_manager = ConfigurationManager()
settings = config_manager.load_settings()
browser_types = [(browser,) for browser in settings["browser_types"]]


@pytest.mark.serial
@parameterized_class(('browser',), browser_types)
class SerialHomeTests(unittest.TestCase):
    VALID_USERS = users.authentic_user

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
        self.jira_client = JiraWrapper()
        self.test_failed = False
        self.error_msg = ""

    @test_decorator
    def test_environment_switching(self):
        environment = self.home_page.changeEnvironment(environment_name="sales CRM")
        self.assertEqual(environment, "sales CRM", "Failed to switch to the sales CRM environment")
        environment = self.home_page.changeEnvironment(environment_name="dev")
        self.assertEqual(environment, "dev", "Failed to switch back to the development environment")

    @test_decorator
    def test_sign_out(self):
        operationResult = self.home_page.sign_out()
        self.assertTrue(operationResult, "Logout process failed")

    def tearDown(self):
        if self.driver:
            self.driver.quit()
        if self.test_failed:
            self.test_name = self.id().split('.')[-1]
            summary = f"{self.test_name} "
            description = f"{self.error_msg} browser {self.browser}"
            try:
                issue_key = self.jira_client.create_issue(summery=summary, description=description,
                                                          issue_type='Bug', project_key='KP')
                print(f"Jira issue created: {issue_key}")
            except Exception as e:
                print(f"Failed to create Jira issue: {e}")
