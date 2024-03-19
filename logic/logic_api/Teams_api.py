import cfbd
from typing import List, Any
from infra.infra_api.api_wrapper import APIWrapper


class TeamsApi():
    def __init__(self):
        """
        Initializes the TeamsApi with a wrapped API client.
        """
        self.API_wrapper = APIWrapper()
        self.api = cfbd.TeamsApi(self.API_wrapper.client)

    def get_roster(self, **kwargs) -> List[Any]:
        """
        Fetches the roster for a given team.

        :param kwargs: Filters such as team, year, etc.
        :return: A list of team members on the roster.
        """
        return self.API_wrapper.fetch_data(self.api.get_roster, **kwargs)
