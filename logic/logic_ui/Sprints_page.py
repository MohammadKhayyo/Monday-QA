from selenium.webdriver.common.by import By
from infra.infra_ui.page_base import BasePage


class SprintsPage(BasePage):
    SPRINT_ELEMENT = (By.XPATH,
                      '/html/body/div[1]/div[4]/div[3]/div[1]/div/div/div/div[2]/div[2]/div/div[2]/div/div/div/div/div/div/div[1]/div/div[3]/div/div/div/div/div')
    NEW_SPRINT_ELEMENT = (By.XPATH, '//*[@id="board-header-view-bar"]/div/div[2]/div/div[1]/button')
    TEXT_NEW_SPRINT = (By.XPATH,
                       "//*[starts-with(@id, 'row-pulse---') and contains(@id, '-notplaceholder-focus-name-')]/div/div[3]/div/div[2]/div/input")
    NAME_NEW_SPRINT = (By.XPATH,
                       "//*[starts-with(@id, 'row-pulse---') and contains(@id, '-notplaceholder-focus-name-')]/div/div[3]/div/div[2]/div/div/span")

    def __init__(self, driver):
        super().__init__(driver)

    def createNewSprint(self, sprint_name="New Sprint"):
        return self.add_new(name=sprint_name, ELEMENT=self.SPRINT_ELEMENT, NEW_ELEMENT=self.NEW_SPRINT_ELEMENT,
                            TEXT_NEW=self.TEXT_NEW_SPRINT, NAME_NEW=self.NAME_NEW_SPRINT, name_new="New Sprint")

    def removeSprint(self, sprint_name="New Sprint", select_Type="first"):
        return self.delete_equal(name=sprint_name, ELEMENT=self.SPRINT_ELEMENT, select_Type=select_Type)

    def delete_all_sprint(self):
        return self.delete_all(self.SPRINT_ELEMENT, NAME_NEW=self.NAME_NEW_SPRINT)

    def revertAllSprintDeletions(self):
        _elements = self.delete_all_sprint()
        return self.UNDO_DELETE(list_all_element=_elements, NAME_NEW=self.NAME_NEW_SPRINT)

    def findTasksByName(self, name="New sprint"):
        return self.check_search(ELEMENT=self.SPRINT_ELEMENT, name=name)
