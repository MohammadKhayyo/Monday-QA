import cfbd
from typing import List, Any
from infra.infra_api.api_wrapper import APIWrapper


class GamesApi():
    def __init__(self):
        self.API_wrapper = APIWrapper()
        self.api = cfbd.GamesApi(self.API_wrapper.client)

    def get_games(self, **kwargs) -> List[Any]:
        """
        Fetches a list of games based on given filter parameters.

        :param kwargs: Filters such as year, week, season_type, team, conference, etc.
        :return: A list of games matching the criteria.
        """
        return self.API_wrapper.fetch_data(self.api.get_games, **kwargs)

    def get_team_records(self, **kwargs) -> List[Any]:
        """
        Retrieves team records based on given filter parameters.

        :param kwargs: Filters such as year, team, conference, etc.
        :return: A list of team records matching the criteria.
        """
        return self.API_wrapper.fetch_data(self.api.get_team_records, **kwargs)

    def get_player_game_stats(self, **kwargs) -> List[Any]:
        """
        Gets statistics for players in games based on given filter parameters.

        :param kwargs: Filters such as year, week, team, player, game, etc.
        :return: A list of player game stats matching the criteria.
        """
        return self.API_wrapper.fetch_data(self.api.get_player_game_stats, **kwargs)

    def get_game_weather(self, **kwargs) -> List[Any]:
        """
        Fetches weather information for games based on given filter parameters.

        :param kwargs: Filters such as year, week, team, game, etc.
        :return: A list of game weather reports matching the criteria.
        """
        return self.API_wrapper.fetch_data(self.api.get_game_weather, **kwargs)

    def get_game_media(self, **kwargs) -> List[Any]:
        """
        Retrieves media information for games based on given filter parameters.

        :param kwargs: Filters such as year, week, team, game, etc.
        :return: A list of game media information matching the criteria.
        """
        return self.API_wrapper.fetch_data(self.api.get_game_media, **kwargs)

    def get_scoreboard(self, **kwargs) -> List[Any]:
        """
        Obtains scoreboard information for games based on given filter parameters.

        :param kwargs: Filters such as year, week, team, game, etc.
        :return: A list of scoreboard information matching the criteria.
        """
        return self.API_wrapper.fetch_data(self.api.get_scoreboard, **kwargs)
