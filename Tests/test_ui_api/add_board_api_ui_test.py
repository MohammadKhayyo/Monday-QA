import os
import unittest
from Utils import users
from infra.infra_ui.browser_wrapper import WebDriverManager
from logic.logic_ui.login_page import LoginPage
from logic.logic_ui.check_add_board import CheckAddBoard
from logic.logic_api.add_board import Board, WorkSpace
from dotenv import load_dotenv
from logic.logic_ui.Home_page import HomePage

load_dotenv("..\\..\\configs\\.env")


class AddBoardTests(unittest.TestCase):
    VALID_USERS = users.authentic_users

    def setUp(self):
        self.api_key = os.getenv("API_MONDAY")
        self.browser_wrapper = WebDriverManager()
        default_browser = 'chrome'
        self.browser = getattr(self.__class__, 'browser', default_browser)
        self.driver = self.browser_wrapper.initialize_web_driver(browser_name=self.browser)
        self.login_page = LoginPage(self.driver)
        user = self.VALID_USERS[0]
        self.login_page.login(user['email'], user['password'])
        self.check_add_board = CheckAddBoard(self.driver)
        self.home_page = HomePage(self.driver)
        self.home_page.changeEnvironment(environment_name="dev")

    def test_add_board(self):
        work_space = WorkSpace(name="MY_TEAM", token=self.api_key)
        my_board = Board(ws=work_space, name="My_terrific_board")
        status = self.check_add_board._add_board(_name="My_terrific_board")
        self.assertTrue(status)

    def tearDown(self):
        if self.driver:
            self.driver.quit()
