import unittest
from logic.logic_api.Rankings_api import RankingsApi
from infra.infra_jira.jira_wrapper import JiraWrapper
from Utils import error_handling


class TestRankingsApi(unittest.TestCase):

    def setUp(self):
        """Setup for test cases; runs before each test method."""
        self.rankings_api = RankingsApi()
        self.year = 2021
        self.week = 3
        self.season_type = "regular"
        self.jira = JiraWrapper()
        self.test_name = self.id().split('.')[-1]
        self.summary = f"{self.test_name}"
        self.project_key = "KP"  # Adjust to your JIRA project key
        self._test_errors = None  # Initialize error tracking

    def test_rank_ascending_order(self):
        """
        test_ui that ranks are in ascending order.
        """
        # Arrange
        params = {'year': self.year, 'week': self.week, 'season_type': self.season_type}

        # Act
        response = self.rankings_api.get_rankings(**params)

        # Assert
        error_handling.assertAndCapture(self, self.assertTrue, self.rankings_api.is_rank_ascending(response),
                                        "Ranks should be in ascending order.")

    def tearDown(self):
        error_handling.report_status(self)
        super().tearDown()


if __name__ == '__main__':
    unittest.main()
