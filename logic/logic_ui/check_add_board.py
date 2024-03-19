from selenium.webdriver.common.by import By
from infra.infra_ui.page_base import BasePage
from selenium.webdriver.support.ui import WebDriverWait


class CheckAddBoard(BasePage):
    switcher_button = (By.XPATH, '//*[@id="product-switcher-button-id"]')
    DIV_BUTTON = (By.XPATH, '//*[@id="main"]/span/div/div/div/div[1]/div[2]/div[3]/div/clickable/div[1]')
    SALES_CRM = (By.XPATH, '//*[@id="main"]/span/div/div/div/div[1]/div[2]/div[2]/div/clickable/div[1]')
    environment_name = (By.XPATH, '//*[@id="mf-topbar"]/div/div/div[1]/div[2]/h1/span[2]')
    DROP_DOWN_LIST = (By.XPATH, '//*[@id="surface-avatar-menu-component"]/div/div/div/img')
    SIGN_OUT = (
        By.XPATH, "//div[contains(@class, 'monday-deprecated-menu-item') and .//span[contains(text(), 'Log out')]]")
    LOGIN = (By.XPATH, '//*[@id="login-monday-container"]/div/div[2]/div/div[1]/div/div[4]/div/button')
    BOARD_NAME = (By.XPATH, "//*[starts-with(@id, 'board_item_')]/div[2]/div/div[1]/div/span")

    def __init__(self, driver):
        super().__init__(driver)

    def _add_board(self, _name="My_terrific_board"):
        self.navigate_to("https://mkhayyo7.monday.com/workspaces/1482559")
        return self.check_add_board(_name="My_terrific_board")
