from infra.infra_ui.page_base import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    URL_BOARD = "https://mkhayyo7.monday.com"
    LOGIN = (By.XPATH, '//*[@id="login-monday-container"]/div/div[2]/div/div[1]/div/div[4]/div/button')
    EMAIL = (By.XPATH, '//*[@id="user_email"]')
    PASSWORD = (By.XPATH, '//*[@id="user_password"]')
    ENTER = LOGIN
    switcher_button = (By.XPATH, '//*[@id="product-switcher-button-id"]')

    def __init__(self, driver):
        super().__init__(driver)

    def login(self, email, password):
        """Login method to enter credentials and navigate to the board."""
        try:
            self.navigate_to(self.URL_BOARD)
            self.click_when_clickable(self.LOGIN)
            self.enter_text(self.EMAIL, email)
            self.enter_text(self.PASSWORD, password)
            self.click_when_clickable(self.ENTER)
            self.wait_for_url_change(self.URL_BOARD)
            self.clickable_element(self.switcher_button)
            return True
        except Exception as E:
            print(E)
            return False
