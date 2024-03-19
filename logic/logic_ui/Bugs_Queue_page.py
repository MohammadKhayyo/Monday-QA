from selenium.webdriver.common.by import By
from infra.infra_ui.page_base import BasePage


class BugsQueuePage(BasePage):
    BUGS_QUEUE_ELEMENT = (By.XPATH,
                          '/html/body/div[1]/div[4]/div[3]/div[1]/div/div/div/div[2]/div[2]/div/div[2]/div/div/div/div/div/div/div[1]/div/div[6]/div/div/div/div/div')
    NEW_BUGS_QUEUE_ELEMENT = (By.XPATH, '//*[@id="board-header-view-bar"]/div/div[2]/div/div[1]/button')
    TEXT_NEW_BUGS_QUEUE = (By.XPATH,
                           "//*[starts-with(@id, 'row-pulse---') and contains(@id, '-notplaceholder-focus-name-')]/div/div[3]/div/div[2]/div/input")
    NAME_NEW_BUGS_QUEUE = (By.XPATH,
                           "//*[starts-with(@id, 'row-pulse---') and contains(@id, '-notplaceholder-focus-name-')]/div/div[3]/div/div[2]/div/div/span")

    def __init__(self, driver):
        super().__init__(driver)

    def add_new_bugs_queue(self, bugs_queue_name="New bug"):
        return self.add_new(name=bugs_queue_name, ELEMENT=self.BUGS_QUEUE_ELEMENT,
                            NEW_ELEMENT=self.NEW_BUGS_QUEUE_ELEMENT,
                            TEXT_NEW=self.TEXT_NEW_BUGS_QUEUE, NAME_NEW=self.NAME_NEW_BUGS_QUEUE,
                            name_new="New bug")

    def bulkDeleteBugs(self, bugs_queue_name="New bug", select_Type="first"):
        return self.delete_equal(name=bugs_queue_name, ELEMENT=self.BUGS_QUEUE_ELEMENT, select_Type=select_Type)

    def delete_all_bugs_queue(self):
        return self.delete_all(self.BUGS_QUEUE_ELEMENT, NAME_NEW=self.NAME_NEW_BUGS_QUEUE)

    def revertBulkBugDeletion(self):
        _elements = self.delete_all_bugs_queue()
        return self.UNDO_DELETE(list_all_element=_elements, NAME_NEW=self.NAME_NEW_BUGS_QUEUE)

    def findTasksByName(self, name="New bug"):
        return self.check_search(ELEMENT=self.BUGS_QUEUE_ELEMENT, name=name)
