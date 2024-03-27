import unittest
from infra.infra_api.api_wrapper import MondayApi
from logic.logic_api.work_space import WorkSpace


class WorkSpaceTest(unittest.TestCase):
    def setUp(self):
        self.send_request = MondayApi()
        self.work_space_name = "MY_TEAM"
        self.folder_id = "888640"
        self.folder_name = "My Team"
        self.work_space = WorkSpace(work_space_name="MY_TEAM")

    def test_get_work_space(self):
        work_space_details = self.work_space.check_workspace_via_key(self.work_space_name, "name")
        self.assertIsNotNone(work_space_details)
        self.assertEqual(self.work_space_name, work_space_details["name"])

    def test_get_folder_vai_id(self):
        folder_id, folder_name = self.work_space.get_folder_via_key(key='id', value=self.folder_id)
        self.assertEqual(folder_id, self.folder_id)
        self.assertEqual(folder_name, self.folder_name)

    def test_get_folder_vai_name(self):
        folder_id, folder_name = self.work_space.get_folder_via_key(key='name', value=self.folder_name)
        self.assertEqual(folder_id, self.folder_id)
        self.assertEqual(folder_name, self.folder_name)
