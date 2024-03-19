from selenium.webdriver.common.by import By
from infra.infra_ui.page_base import BasePage


class TasksPage(BasePage):
    TASK_ELEMENT = (By.XPATH,
                    '/html/body/div[1]/div[4]/div[3]/div[1]/div/div/div/div[2]/div[2]/div/div[2]/div/div/div/div/div/div/div[1]/div/div[4]/div/div/div/div/div')
    NEW_TASK_ELEMENT = (By.XPATH,
                        '/html/body/div[1]/div[4]/div[3]/div[2]/div[3]/div/div/div/div[1]/div[2]/div/div/div/div[3]/div/div[2]/div/div[1]/button')
    TEXT_NEW_TASK = (By.XPATH,
                     "//*[starts-with(@id, 'row-pulse---') and contains(@id, '-notplaceholder-focus-name-')]/div/div[3]/div/div[2]/div/input")
    NAME_NEW_TASK = (By.XPATH,
                     "//*[starts-with(@id, 'row-pulse---') and contains(@id, '-notplaceholder-focus-name-')]/div/div[3]/div/div[2]/div/div/span")

    def __init__(self, driver):
        super().__init__(driver)

    def create_task(self, task_name="New task"):
        return self.add_new(name=task_name, ELEMENT=self.TASK_ELEMENT, NEW_ELEMENT=self.NEW_TASK_ELEMENT,
                            TEXT_NEW=self.TEXT_NEW_TASK, NAME_NEW=self.NAME_NEW_TASK, name_new="New task", Task=True)

    def remove_task(self, task_name="New task", select_Type="first"):
        return self.delete_equal(name=task_name, ELEMENT=self.TASK_ELEMENT, select_Type=select_Type, Task=True)

    def delete_all_tasks(self):
        return self.delete_all(self.TASK_ELEMENT, NAME_NEW=self.NAME_NEW_TASK, Task=True)

    def revertAllTaskDeletions(self):
        _elements = self.delete_all_tasks()
        return self.UNDO_DELETE(list_all_element=_elements, NAME_NEW=self.NAME_NEW_TASK)

    def findTasksByName(self, name="New sprint"):
        return self.check_search(ELEMENT=self.TASK_ELEMENT, name=name)
