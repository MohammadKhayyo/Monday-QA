from selenium.webdriver.common.by import By
from infra.infra_ui.page_base import BasePage


class RetrospectivesPage(BasePage):
    RETROSPECTIVES_ELEMENT = (By.XPATH,
                              '/html/body/div[1]/div[4]/div[3]/div[1]/div/div/div/div[2]/div[2]/div/div[2]/div/div/div/div/div/div/div[1]/div/div[7]/div/div/div/div/div')
    NEW_RETROSPECTIVES_ELEMENT = (By.XPATH, '//*[@id="board-header-view-bar"]/div/div[2]/div/div[1]/button')
    TEXT_NEW_RETROSPECTIVES = (By.XPATH,
                               "//*[starts-with(@id, 'row-pulse---') and contains(@id, '-notplaceholder-focus-name-')]/div/div[3]/div/div[2]/div/input")
    NAME_NEW_RETROSPECTIVES = (By.XPATH,
                               "//*[starts-with(@id, 'row-pulse---') and contains(@id, '-notplaceholder-focus-name-')]/div/div[3]/div/div[2]/div/div/span")

    def __init__(self, driver):
        super().__init__(driver)

    def add_new_retrospective(self, sprint_name="New feedback"):
        return self.add_new(name=sprint_name, ELEMENT=self.RETROSPECTIVES_ELEMENT,
                            NEW_ELEMENT=self.NEW_RETROSPECTIVES_ELEMENT,
                            TEXT_NEW=self.TEXT_NEW_RETROSPECTIVES, NAME_NEW=self.NAME_NEW_RETROSPECTIVES,
                            name_new="New feedback")

    def bulkDeleteRetrospectives(self, sprint_name="New feedback", select_Type="first"):
        return self.delete_equal(name=sprint_name, ELEMENT=self.RETROSPECTIVES_ELEMENT, select_Type=select_Type)

    def delete_all_retrospectives(self):
        return self.delete_all(self.RETROSPECTIVES_ELEMENT, NAME_NEW=self.NAME_NEW_RETROSPECTIVES)

    def revertBulkDeletion(self):
        _elements = self.delete_all_retrospectives()
        return self.UNDO_DELETE(list_all_element=_elements, NAME_NEW=self.NAME_NEW_RETROSPECTIVES)

    def findTasksByName(self, name="New feedback"):
        return self.check_search(ELEMENT=self.RETROSPECTIVES_ELEMENT, name=name)
