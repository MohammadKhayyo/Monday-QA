import unittest
from logic.logic_api.Teams_api import TeamsApi
from infra.infra_jira.jira_wrapper import JiraWrapper
from Utils import error_handling


class TestTeamsApi(unittest.TestCase):

    def setUp(self):
        self.team = 'Clemson'
        self.teams_api = TeamsApi()
        self.jira = JiraWrapper()
        self.test_name = self.id().split('.')[-1]
        self.summary = f"{self.test_name}"
        self.project_key = "KP"  # Adjust to your JIRA project key
        self._test_errors = None  # Initialize error tracking

    def test_get_team_roster(self):
        # Arrange
        params = {'team': self.team}

        # Act
        response = self.teams_api.get_roster(**params)

        # Assert
        error_handling.assertAndCapture(self, self.assertTrue, response)
        error_handling.assertAndCapture(self, self.assertTrue, all(
            getattr(player, 'team') == self.team for player in response), "Roster does not match the team.")

    def tearDown(self):
        error_handling.report_status(self)
        super().tearDown()


if __name__ == '__main__':
    unittest.main()
