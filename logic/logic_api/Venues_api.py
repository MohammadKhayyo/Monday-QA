import cfbd
from typing import List, Any
from infra.infra_api.api_wrapper import APIWrapper


class VenuesApi():
    """
    VenuesApi provides an interface to fetch venue-related data from the college football data API,
    utilizing a wrapped API client.
    """

    def __init__(self):
        self.API_wrapper = APIWrapper()
        self.api = cfbd.VenuesApi(self.API_wrapper.client)

    def get_venues(self, **kwargs) -> List[Any]:
        """
        Retrieves a list of venues. Can be filtered using provided parameters.

        :param kwargs: Filters such as id, city, state, or country.
        :return: A list of venues matching the given filters.
        """
        return self.API_wrapper.fetch_data(self.api.get_venues, **kwargs)
