import unittest
from logic.logic_api.Games_api import GamesApi
from infra.infra_api.api_wrapper import APIWrapper
from infra.infra_jira.jira_wrapper import JiraWrapper
from Utils import error_handling


class TestGameAPI(unittest.TestCase):

    def setUp(self):
        super().setUp()  # Call the base class setup
        self.year = 2021
        self.game_id = 401309866  # Example game ID
        self.team = 'Clemson'
        self.games_api = GamesApi()
        self.API_wrapper = APIWrapper()
        self.jira = JiraWrapper()
        self.project_key = "KP"  # Adjust to your JIRA project key
        self._test_errors = None
        self.summary = f"{self.id().split('.')[-1]}"

    def tearDown(self):
        error_handling.report_status(self)
        super().tearDown()

    # Now use assertAndCapture for each assertion in your test methods
    def test_get_games(self):
        # Arrange
        params = {'year': self.year}

        # Act
        response = self.games_api.get_games(**params)

        # Assert
        error_handling.assertAndCapture(self, self.assertTrue, response, "The response should not be empty.")
        params['season'] = params.pop('year')
        status = self.API_wrapper.check_response_content(response_json=response, **params)
        error_handling.assertAndCapture(self, self.assertTrue, status,
                                        "The status should be True indicating correct response content.")

    def test_get_game_media(self):
        """test_ui case for getting game media information for a specific year."""
        # Arrange
        year = 2021
        media_type = 'web'
        params = {'year': year, 'media_type': media_type}

        # Act
        response = self.games_api.get_game_media(**params)

        # Assert
        error_handling.assertAndCapture(self, self.assertTrue, response, "The response should not be empty.")

        params['season'] = params.pop('year')
        status = self.API_wrapper.check_response_content(response_json=response, **params)
        error_handling.assertAndCapture(self, self.assertTrue, status,
                                        "The status should be True indicating correct response content.")

    def test_get_player_game_stats(self):
        """
        test_ui case to ensure the API can fetch player game stats for a specified year and game ID.
        - Uses 'year' and 'game_id' parameters to fetch stats.
        - Asserts that the response is a list, which is the expected data type for player game stats.
        """
        # Arrange
        params = {'year': self.year, 'game_id': self.game_id}

        # Act
        response = self.games_api.get_player_game_stats(**params)

        # Assert
        error_handling.assertAndCapture(self, self.assertIsInstance, response, list)
        error_handling.assertAndCapture(self, self.assertEqual, getattr(response[0], 'id'), self.game_id)

    def test_get_game_by_id(self):
        """
        test_ui case to verify that the Games API can retrieve details for a game using a specific game ID.
        - Fetches all games for a year and then filters to find the game with the specified ID.
        - Asserts that the game details are not None and that the ID matches the specified ID.
        """
        # Arrange
        params = {'year': self.year}

        # Act
        games = self.games_api.get_games(**params)
        game_details = next(
            (game for game in games if getattr(game, 'id', "") == self.game_id), None)

        # Assert
        error_handling.assertAndCapture(self, self.assertIsNotNone, game_details, "Game details were not found.")
        error_handling.assertAndCapture(self, self.assertEqual, getattr(game_details, 'id'), self.game_id)

    def test_get_team_records(self):
        """
        test_ui whether the Games API can retrieve records for a specific team.
        - Uses 'team' parameter to fetch records.
        - Asserts that the response is not empty.
        - Verifies that every record in the response corresponds to the specified team.
        """
        # Arrange
        params = {'team': self.team}

        # Act

        response = self.games_api.get_team_records(**params)

        # Assert
        error_handling.assertAndCapture(self, self.assertTrue, response)
        error_handling.assertAndCapture(self, self.assertTrue,
                                        all(getattr(record, 'team') == self.team for record in response))


if __name__ == '__main__':
    unittest.main()
