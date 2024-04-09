from selenium import webdriver
from Utils.configurations import ConfigurationManager


class WebDriverManager:

    def __init__(self):
        self.driver = None
        config_manager = ConfigurationManager()
        self.settings = config_manager.load_settings()

    def create_options(self, browser_type):
        if browser_type.lower() == 'chrome':
            options = webdriver.ChromeOptions()
        elif browser_type.lower() == 'firefox':
            options = webdriver.FirefoxOptions()
        elif browser_type.lower() == 'edge':
            options = webdriver.EdgeOptions()
        else:
            raise ValueError(f"Unsupported browser type: {browser_type}")
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        return options

    def initialize_web_driver(self, browser_name):
        if self.settings["grid"]:
            options = self.set_up_capabilities(browser_name)
            self.driver = webdriver.Remote(command_executor=self.settings["hub"], options=options)
        else:
            options = self.create_options(browser_name)
            if browser_name.lower() == 'chrome':
                self.driver = webdriver.Chrome(options=options)
            elif browser_name.lower() == 'firefox':
                self.driver = webdriver.Firefox(options=options)
            elif browser_name.lower() == 'edge':
                self.driver = webdriver.Edge(options=options)

        self.driver.get(self.settings["url"])
        self.driver.maximize_window()
        # self.driver.fullscreen_window()
        return self.driver

    def set_up_capabilities(self, browser_type):
        options = None
        if browser_type.lower() == 'chrome':
            options = webdriver.ChromeOptions()
        elif browser_type.lower() == 'firefox':
            options = webdriver.FirefoxOptions()
        elif browser_type.lower() == 'edge':
            options = webdriver.EdgeOptions()
        if options is not None:
            platform_name = self.settings["platform"]
            options.add_argument(f'--platformName={platform_name}')
            options.add_argument("--headless")
            options.add_argument("--no-sandbox")  # This line is often necessary in CI environments
            options.add_argument("--disable-dev-shm-usage")  # This can help in environments with limited resources
            return options
        else:
            raise ValueError("Unsupported browser type")

    def create_local_driver(self, browser_name):
        browser_name_lower = browser_name.lower()
        if browser_name_lower == 'chrome':
            return webdriver.Chrome()
        elif browser_name_lower == 'firefox':
            return webdriver.Firefox()
        elif browser_name_lower == 'edge':
            return webdriver.Edge()
        else:
            raise ValueError("Browser type not supported")

    def navigate_to_url(self, url):
        self.driver.get(url)

    def maximize_browser_window(self):
        self.driver.maximize_window()
