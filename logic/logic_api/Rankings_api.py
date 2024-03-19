import cfbd
from typing import List, Any
from infra.infra_api.api_wrapper import APIWrapper


class RankingsApi():
    def __init__(self):
        """
        Initializes the TeamsApi with a wrapped API client.
        """
        self.API_wrapper = APIWrapper()
        self.api = cfbd.RankingsApi(self.API_wrapper.client)

    def get_rankings(self, **kwargs) -> List[Any]:
        """
        Fetches rankings for a given year and optional week and season type.

        :param year: The year to fetch rankings for.
        :param week: The optional week number within the season to fetch rankings for.
        :param season_type: The season type, "regular" or "postseason".
        :return: A list of rankings data.
        """
        # Filtering out None values
        kwargs = {k: v for k, v in kwargs.items() if v is not None}
        return self.API_wrapper.fetch_data(self.api.get_rankings, **kwargs)

    def is_rank_ascending(self, response):
        """
        Checks if ranks within a specified poll are in ascending order.

        :param response: The parsed JSON response.
        :param poll_name: The name of the poll to check.
        :return: True if ranks are in ascending order, False otherwise.
        """
        for entry in response:
            for poll in getattr(entry, 'polls', []):
                previous_rank = 0
                for rank in getattr(poll, 'ranks', []):
                    current_rank = getattr(rank, 'rank')
                    if current_rank < previous_rank:
                        return False
                    previous_rank = current_rank
                return True
        return False
