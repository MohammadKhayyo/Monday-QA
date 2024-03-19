import unittest
from logic.logic_api.Venues_api import VenuesApi
import cfbd
from infra.infra_jira.jira_wrapper import JiraWrapper
from Utils import error_handling


class TestVenuesApi(unittest.TestCase):

    def setUp(self):
        self.venues_api = VenuesApi()
        self.mock_venue = cfbd.Venue(id=3997, city="New Haven", name="Yale Bowl")
        self.jira = JiraWrapper()
        self.test_name = self.id().split('.')[-1]
        self.summary = f"{self.test_name}"
        self.project_key = "KP"  # Adjust to your JIRA project key
        self._test_error = None  # Initialize error tracking

    def test_get_venue_information(self):
        # Arrange
        # params = {'id': 3997, 'city': "New Haven", 'name': "Yale Bowl"}

        # Act
        response = self.venues_api.get_venues()

        # Assert
        error_handling.assertAndCapture(self, self.assertTrue, response)
        venue_details = next(
            (venue for venue in response if getattr(venue, 'id', "") == self.mock_venue.id), None)
        error_handling.assertAndCapture(self, self.assertEqual, getattr(venue_details, 'id', ""), self.mock_venue.id)
        error_handling.assertAndCapture(self, self.assertEqual, getattr(venue_details, 'city', ""),
                                        self.mock_venue.city)
        error_handling.assertAndCapture(self, self.assertEqual, getattr(venue_details, 'name', ""),
                                        self.mock_venue.name)

    def tearDown(self):
        error_handling.report_status(self)
        super().tearDown()


if __name__ == '__main__':
    unittest.main()
