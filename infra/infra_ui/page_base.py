from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

BOARD_NAME = (By.XPATH, "//*[starts-with(@id, 'board_item_')]/div[2]/div/div[1]/div/span")


class BasePage():
    NAV_NUTRITION_TARGETS = (By.XPATH, "//a[@type='button']/span[text()='Nutrition Targets']")
    BTN_MENU = (By.XPATH, "//button[@title='Open Menu']")
    NAV_DIET_NUTRITION = (By.XPATH, "//button/svg[text()='Diet & Nutrition']")
    TAB_MAIN_TABLE = (By.XPATH, "//button[.//span[contains(text(), 'Main Table')]]")
    BTN_MAIN_TABLE_TASKS = (By.XPATH, '//*[@id="board-header"]/div/div/div[2]/div[2]/div[4]/button')
    HEADER_BOARD = (
        By.XPATH,
        "//*[starts-with(@id, 'row-header-currentBoard-') and contains(@id, '-notfloating-focus-name-')]/div[3]")
    BTN_FILTER_SEARCH = (
        By.XPATH, '//*[@id="board-header-view-bar"]/div/div[3]/div[1]/div/div[2]/div/div/span/button')
    TXT_ITEM_NAME_FILTER = (By.XPATH,
                            "//*[starts-with(@id, 'row-pulse---') and contains(@id, '-notplaceholder-focus-name-')]/div/div[3]/div/div[2]/div")
    CHK_BOX_ITEM = (
        By.XPATH, "//*[starts-with(@id, 'row-pulse---') and contains(@id, '-notplaceholder-focus-name-')]/div/div[2]")
    PAGE_COLUMN_SELECTION = (By.XPATH, '//*[@id="main"]/span/div/div/div')
    TXT_COLUMN_COUNT = (By.XPATH, '//*[@id="main"]/span/div/div/div/div[3]/div[1]/label[2]')
    BTN_SELECT_ALL_COLUMNS = (By.XPATH, '//*[@id="main"]/span/div/div/div/div[3]/div[1]/label[1]')
    BTN_COLUMN_NAME = (By.XPATH, '//*[@id="main"]/span/div/div/div/div[3]/div[2]/label')
    BTN_DELETE = (By.XPATH, '//*[@id="board-wrapper-first-level-content"]/div[4]/div/div/div/div[7]')
    BTN_CONFIRM_DELETE = (By.XPATH, '//*[@id="main"]/*/div/div/div/div/div/span/button[2]')
    SEARCH_WITHOUT_CLICK = (By.XPATH, '//*[@id="board-header-view-bar"]/div[1]/div[3]/div[1]')
    SEARCH_WITH_CLICK = (By.XPATH, '//*[@id="board-header-view-bar"]/div[1]/div[3]/div[1]/div/div[1]/input')
    X_SEARCH = (By.XPATH, '//*[@id="board-header-view-bar"]/div[1]/div[3]/div[1]/div/div[2]/span/button')
    ALL_CHECK_BOX_ = (By.XPATH,
                      "//*[starts-with(@id, 'row-header-currentBoard-') and contains(@id, '-notfloating-focus-name-')]/div[2]")
    UNDO = (By.XPATH, '//*[@id="main"]/div[24]/div[1]/div/div[2]/button')
    switcher_button = (By.XPATH, '//*[@id="product-switcher-button-id"]')
    DELETE_ANYWAY_BUTTON_fire_fox = BTN_CONFIRM_DELETE
    TXT_DESCRIPTION = (By.XPATH, '//*[@id="board-header"]/div/div/div[1]/div/div[1]/div/div[2]/span/button')

    SEARCH_MY_TEAM = (By.XPATH, '//*[@id="boards-list-search-input"]')
    tmp = (By.XPATH, '//*[@id="first-level-content"]/div/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/div/button')
    BOARD_NAME = (By.XPATH, "//*[starts-with(@id, 'board_item_')]/div[2]/div/div[1]/div/span")
    Attached_Files_field = (By.XPATH,
                            "//*[starts-with(@id, 'row-pulse---') and contains(@id, '-notplaceholder-focus-attached_files-')]/div/div/div")

    text_in_Attached_Files_field = (
        By.XPATH, "//*[starts-with(@id, 'pdf_asset_id_') and contains(@id, '_page_2')]/div[2]/div[1]/span")

    group = (By.XPATH,
             "//*[starts-with(@id, 'row-header-currentBoard-') and contains(@id, 'notfloating-focus-group_title-')]/span[2]/div/div/h4")

    link_column = (By.XPATH,
                   "//*[starts-with(@id, 'row-header-currentBoard-') and contains(@id, 'notfloating-focus-link-')]/span/div/div/h6")

    link_field = (By.XPATH,
                  "//*[starts-with(@id, 'row-pulse---') and contains(@id, 'notplaceholder-focus-link-')]/div/div/div/a")
    add_item_in_my_board = (By.XPATH, '//*[@id="board-header-view-bar"]/div/div[2]/div/div[1]/button')
    The_Big_X = (By.XPATH, '//*[@id="board-wrapper-first-level-content"]/div[4]/div/div/div/div[11]')
    number_of_item_selected = (By.XPATH, '//*[@id="board-wrapper-first-level-content"]/div[4]/div/div/div/div[2]/div')

    def __init__(self, driver):
        self._driver = driver

    def click_when_clickable(self, locator, time_out=30):
        self.wait_for_element(locator, time_out=time_out)
        self.wait_for_visibility_of_element_located(locator, time_out=time_out)
        element = WebDriverWait(self._driver, time_out).until(EC.element_to_be_clickable(locator))
        element.click()
        return element

    def wait_for_element(self, locator, time_out=30):
        return WebDriverWait(self._driver, time_out).until(EC.presence_of_element_located(locator))

    def wait_for_visibility_of_element_located(self, locator, time_out=30):
        return WebDriverWait(self._driver, time_out).until(EC.visibility_of_element_located(locator))

    def enter_text(self, locator, text):
        field = self.wait_for_element(locator)
        field.clear()
        field.send_keys(text)

    def navigate_to(self, url):
        self._driver.get(url)

    def wait_for_url_change(self, url):
        WebDriverWait(self._driver, 30).until(lambda driver: url in driver.current_url)

    def wait_for_text(self, url):
        WebDriverWait(self._driver, 30).until(lambda driver: url in driver.current_url)

    def clickable_element(self, locator, time_out=30):
        """Wait for an element to be clickable and then click."""
        try:
            self.wait_for_visibility_of_element_located(locator, time_out=time_out)
        except:
            pass

        try:
            self.wait_for_element(locator, time_out=time_out)
        except:
            pass

        element = WebDriverWait(self._driver, time_out).until(EC.element_to_be_clickable(locator))
        return element

    def switch_and_click(self, ELEMENT, tab):
        try:
            self.wait_for_visibility_of_element_located(self.SEARCH_MY_TEAM)
            self.wait_for_element(self.SEARCH_MY_TEAM)
            self.clickable_element(self.SEARCH_MY_TEAM)
            self.clickable_element(ELEMENT)
            self.click_when_clickable(ELEMENT)
            self.clickable_element(tab)
            self.click_when_clickable(tab)
        except:
            try:
                self.wait_for_visibility_of_element_located(ELEMENT, time_out=3)
            except:
                pass
            try:
                self.wait_for_element(ELEMENT, time_out=3)
            except:
                pass
            try:
                self.clickable_element(ELEMENT, time_out=3)
            except:
                pass
            try:
                self.click_when_clickable(ELEMENT, time_out=3)
            except:
                pass
            try:
                self.wait_for_element(tab, time_out=3)
            except:
                pass
            try:
                self.wait_for_visibility_of_element_located(tab, time_out=3)
            except:
                pass
            try:
                self.clickable_element(tab, time_out=3)
            except:
                pass
            try:
                self.click_when_clickable(tab, time_out=3)
            except:
                pass

    def switch_to_tab(self, tab):
        try:
            self.clickable_element(self.SEARCH_MY_TEAM)
            self.clickable_element(tab)
            self.click_when_clickable(tab)
        except:
            self.clickable_element(tab)
            self.click_when_clickable(tab)

    def add_new(self, name, ELEMENT, NEW_ELEMENT, TEXT_NEW, NAME_NEW, name_new, Task=False):
        self.switch_and_click(ELEMENT, self.TAB_MAIN_TABLE)
        # if Task:
        #     self.clickable_element(self.Main_table_Tasks)
        #     self.click_when_clickable(self.Main_table_Tasks)
        # self.switch_and_click(ELEMENT, self.Main_table_Tasks)
        self.click_when_clickable(NEW_ELEMENT, time_out=3)
        try:
            self.wait_for_element(TEXT_NEW, time_out=3)
            self.wait_for_visibility_of_element_located(TEXT_NEW, time_out=3)
            name_field = self.clickable_element(TEXT_NEW, time_out=3)
        except:
            self.wait_for_element(NAME_NEW, time_out=3)
            self.wait_for_visibility_of_element_located(NAME_NEW, time_out=3)
            names = self._driver.find_elements(*NAME_NEW)
            for element in names:
                if element.text.lower() == name_new.lower():
                    element.click()
                    break
            try:
                self.wait_for_element(TEXT_NEW, time_out=3)
                self.wait_for_visibility_of_element_located(TEXT_NEW, time_out=3)
                name_field = self.clickable_element(TEXT_NEW, time_out=3)
            except:
                return False
        name_field.send_keys(Keys.CONTROL + "a")
        name_field.send_keys(Keys.DELETE)
        name_field.send_keys(name)
        name_field.send_keys(Keys.ENTER)
        return True

    def select(self, select_Type, names, check_boxes, name):
        count = 0
        list_EM = list()
        actions = ActionChains(self._driver)
        board = self._driver.find_elements(*self.HEADER_BOARD)
        board[0].click()
        for index, _name in enumerate(names):
            if _name.text.lower() == name.lower():
                count += 1
                list_EM.append(_name)
                not_click = True
                while not_click:
                    try:
                        check_boxes[index].click()
                        not_click = False
                    except:
                        actions.send_keys(Keys.ARROW_DOWN * 3).perform()
                if select_Type == 'first':
                    break
        return list_EM, count

    def search(self, ELEMENT=None, name="", Task=False):
        if ELEMENT is None:
            self.switch_and_click(ELEMENT, self.TAB_MAIN_TABLE)
        # if Task:
        #     self.clickable_element(self.Main_table_Tasks)
        #     self.click_when_clickable(self.Main_table_Tasks)
        self.click_when_clickable(self.SEARCH_WITHOUT_CLICK)
        _input = self.wait_for_element(self.SEARCH_WITH_CLICK)
        _input.send_keys(Keys.CONTROL + "a")
        _input.send_keys(Keys.DELETE)
        _input.send_keys(name)
        _input.send_keys(Keys.ENTER)
        WebDriverWait(self._driver, 30).until(lambda driver: _input.get_attribute("value") == name)
        self.filter_in_search_By_column_only(self.BTN_COLUMN_NAME)
        self.clickable_element(self.X_SEARCH)
        self.clickable_element(self.BTN_FILTER_SEARCH)
        try:
            self.clickable_element(self.TXT_ITEM_NAME_FILTER)
            names = self._driver.find_elements(*self.TXT_ITEM_NAME_FILTER)
            check_boxes = self._driver.find_elements(*self.CHK_BOX_ITEM)
            return names, check_boxes
        except:
            return None, None

    def filter_in_search_By_column_only(self, column_name):
        self.click_when_clickable(self.BTN_FILTER_SEARCH)
        WebDriverWait(self._driver, 30).until(EC.presence_of_element_located(self.PAGE_COLUMN_SELECTION))
        _text = WebDriverWait(self._driver, 30).until(EC.presence_of_element_located(self.TXT_COLUMN_COUNT))
        _text = _text.text
        if _text != "0 selected":
            self.click_when_clickable(self.BTN_SELECT_ALL_COLUMNS)
        _text = WebDriverWait(self._driver, 30).until(EC.presence_of_element_located(self.TXT_COLUMN_COUNT))
        _text = _text.text
        self.click_when_clickable(column_name)
        self.click_when_clickable(self.BTN_FILTER_SEARCH)

    def check_search(self, ELEMENT, name="New task", Task=False):
        names, check_boxes = self.search(ELEMENT=ELEMENT, name=name, Task=Task)
        if names is None or len(names) == 0:
            return True
        try:
            EM_names = self._driver.find_elements(*self.TXT_ITEM_NAME_FILTER)
        except:
            if names is None:
                return True
            else:
                return False
        board = self._driver.find_elements(*self.HEADER_BOARD)
        board[0].click()
        count = 0
        actions = ActionChains(self._driver)
        for _name in EM_names:
            count += 1
            actions.send_keys(Keys.ARROW_DOWN).perform()
        if count == len(names):
            return True
        else:
            return False

    def delete_equal(self, name, ELEMENT, select_Type="first", Task=False):
        try:
            names, check_boxes = self.search(ELEMENT=ELEMENT, name=name, Task=Task)
            if names is None or len(names) == 0:
                return True
            list_EM, count = self.select(select_Type=select_Type, name=name, names=names, check_boxes=check_boxes)
            if (len(list_EM) != 0 and count == 0) or (count != 0 and len(list_EM) == 0):
                return False
            if count == 0:
                return True
            self.wait_for_element(self.BTN_DELETE)
            self.wait_for_visibility_of_element_located(self.BTN_DELETE)
            self.clickable_element(self.BTN_DELETE)
            self.click_when_clickable(self.BTN_DELETE)
            self.wait_for_element(self.BTN_CONFIRM_DELETE)
            self.wait_for_visibility_of_element_located(self.BTN_CONFIRM_DELETE)
            self.clickable_element(self.BTN_CONFIRM_DELETE)
            self.click_when_clickable(self.BTN_CONFIRM_DELETE)

            return True
        except:
            return False

    def delete_all(self, ELEMENT, NAME_NEW, Task=False):
        # self.switch_and_click(ELEMENT, self.Main_table)
        # if Task:
        #     self.clickable_element(self.Main_table_Tasks)
        #     self.click_when_clickable(self.Main_table_Tasks)
        try:
            self.switch_and_click(ELEMENT, self.TAB_MAIN_TABLE)
            # self.clickable_element(NAME_NEW)
            # self.clickable_element(NAME_NEW)
        except:
            return list()
        self.clickable_element(ELEMENT)
        self.clickable_element(self.HEADER_BOARD)
        self.click_when_clickable(self.HEADER_BOARD)
        # WebDriverWait(self._driver, 30).until(EC.presence_of_all_elements_located(NAME_NEW))
        try:
            self.wait_for_visibility_of_element_located(NAME_NEW)
            names = self._driver.find_elements(*NAME_NEW)
        except:
            self.wait_for_element(NAME_NEW)
            names = self._driver.find_elements(*NAME_NEW)
        if names is None or len(names) == 0:
            return list()
        list_all_element = list()
        for name in names:
            list_all_element.append(name.text)
        self.clickable_element(ELEMENT)
        # self.click_when_clickable(ELEMENT)
        count = 0
        try:
            # WebDriverWait(self._driver, 30).until(EC.presence_of_all_elements_located(self.ALL_CHECK_BOX_))
            elements = self._driver.find_elements(*self.ALL_CHECK_BOX_)
        except:
            return None
        for element in elements:
            try:
                element.click()
                count += 1
            except:
                pass
        if count == 0:
            return list_all_element
        self.clickable_element(self.BTN_DELETE)
        self.click_when_clickable(self.BTN_DELETE)
        self.clickable_element(self.BTN_CONFIRM_DELETE)
        self.click_when_clickable(self.BTN_CONFIRM_DELETE)

        # for element in elements:
        #     try:
        #         element.click()
        #     except:
        #         pass
        return list_all_element

    def UNDO_DELETE(self, list_all_element, NAME_NEW):
        if not list_all_element or len(list_all_element) == 0:
            return True
        self.click_when_clickable(self.UNDO)
        self.clickable_element(NAME_NEW, time_out=10)
        names = self._driver.find_elements(*NAME_NEW)
        # number_selected = self.wait_for_visibility_of_element_located(self.number_of_item_selected).text
        # if number_selected.isnumeric():
        #     number_selected = int(number_selected)
        #     if 0 < len(list_all_element) <= number_selected and number_selected > 0:
        #         return True
        if len(list_all_element) != len(names):
            return False
        sorted_names = list()
        for name in names:
            sorted_names.append(name.text)
        sorted_names = sorted(sorted_names)
        sorted_list_all_element = sorted(list_all_element)
        for i in range(len(sorted_names)):
            if sorted_names[i] != sorted_list_all_element[i]:
                return False
        return True

    def click_undo_delete_button(self):
        self.click_when_clickable(self.UNDO)

    def get_all_elements_in_task_in_search(self):
        try:
            self.clickable_element(self.switcher_button)
            self.clickable_element(self.add_item_in_my_board)
            self.clickable_element(self.X_SEARCH)
            self.clickable_element(self.add_item_in_my_board)
            self.wait_for_visibility_of_element_located(self.TXT_ITEM_NAME_FILTER, time_out=5)
            names = self._driver.find_elements(*self.TXT_ITEM_NAME_FILTER)
            list_all_elements = list()
            for name in names:
                list_all_elements.append(name.text)
            return list_all_elements
        except:
            return list()

    def check_add_board(self, _name="MY_BOARD"):
        self.clickable_element(self.switcher_button)
        # self.clickable_element(self.tmp)
        names = self._driver.find_elements(*self.BOARD_NAME)
        for name in names:
            if name.text == _name:
                return True
        return False

    def switch_board(self, _name="MY_BOARD"):
        self.clickable_element(self.switcher_button)
        # self.clickable_element(self.tmp)
        names = self._driver.find_elements(*self.BOARD_NAME)
        for name in names:
            if name.text == _name:
                # self.switch_to_tab(tab=self.TAB_MAIN_TABLE)
                name.click()
                # self.switch_to_tab(tab=self.TAB_MAIN_TABLE)
                return True
        return False

    def click_Attached_Files(self, name_item="new_item_1"):
        self.search(self, name=name_item)
        self.clickable_element(self.add_item_in_my_board)
        names = self._driver.find_elements(*self.Attached_Files_field)
        for name in names:
            name.click()
        text_element = self.wait_for_visibility_of_element_located(self.text_in_Attached_Files_field)
        text = text_element.text
        return text

    def get_all_group(self):
        self.clickable_element(self.add_item_in_my_board)
        self.switch_to_tab(tab=self.TAB_MAIN_TABLE)
        self.clickable_element(self.add_item_in_my_board)
        groups = self._driver.find_elements(*self.group)
        groups_list_names = list()
        for group in groups:
            if group.text:
                groups_list_names.append(group.text)
        return groups_list_names

    def get_all_links(self):
        self.clickable_element(self.add_item_in_my_board)
        self.switch_to_tab(tab=self.TAB_MAIN_TABLE)
        self.clickable_element(self.add_item_in_my_board)
        links = self._driver.find_elements(*self.link_field)
        links_list_names = list()
        for link in links:
            links_list_names.append({'text': link.text, 'href': link.get_attribute('href')})
        return links_list_names

    def click_on_the_big_X(self):
        self.wait_for_visibility_of_element_located(self.The_Big_X)
        self.click_when_clickable(self.The_Big_X)

    def clear_search_the_small_x(self):
        self.wait_for_visibility_of_element_located(self.X_SEARCH)
        self.click_when_clickable(self.X_SEARCH)
