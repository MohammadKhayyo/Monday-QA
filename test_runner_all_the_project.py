from typing import Type
import unittest
from concurrent.futures import ThreadPoolExecutor
from Utils.configurations import ConfigurationManager
from Tests.ui.parallel.parallel_tasks_test import ParallelTasksTests
from Tests.ui.parallel.parallel_sprints_test import ParallelSprintsTests
from Tests.ui.parallel.parallel_epics_test import ParallelEpicsTests
from Tests.ui.parallel.parallel_login_test import ParallelLoginTests
from Tests.ui.parallel.parallel_home_test import ParallelHomeTests
from Tests.ui.parallel.parallel_bugs_queue_test import ParallelBugsQueueTests
from Tests.ui.parallel.parallel_retrospectives_page_test import ParallelRetrospectivesTests

from Tests.ui.non_parallel.serial_tasks_test import SerialTasksTests
from Tests.ui.non_parallel.serial_sprints_test import SerialSprintsTests
from Tests.ui.non_parallel.serial_epics_test import SerialEpicsTests
from Tests.ui.non_parallel.serial_login_test import SerialLoginTests
from Tests.ui.non_parallel.serial_home_test import SerialHomeTests
from Tests.ui.non_parallel.serial_bugs_queue_test import BugsQueuePage
from Tests.ui.non_parallel.serial_retrospectives_test import RetrospectivesPage

from Tests.api.games_api_test import TestGameAPI
from Tests.api.teams_api_test import TestTeamsApi
from Tests.api.venues_api_test import TestVenuesApi
from Tests.api.ranking_api_test import RankingsApi

# Grouping test cases
serial_test_groups_one = [SerialTasksTests, SerialSprintsTests, SerialEpicsTests, SerialLoginTests, SerialHomeTests,
                          BugsQueuePage, RetrospectivesPage]
parallel_test_groups_one = [ParallelTasksTests, ParallelSprintsTests, ParallelEpicsTests, ParallelLoginTests,
                            ParallelHomeTests, ParallelBugsQueueTests, ParallelRetrospectivesTests]
all_test_group_one = serial_test_groups_one + parallel_test_groups_one

all_test_group_two = [TestGameAPI, TestTeamsApi, TestVenuesApi, RankingsApi]

all_test_groups = all_test_group_one + all_test_group_two


def execute_test_with_browser(browser_name: str, test_group: Type[unittest.TestCase]):
    test_group.browser = browser_name
    test_suite = unittest.TestLoader().loadTestsFromTestCase(test_group)
    unittest.TextTestRunner().run(test_suite)


def run_tests_for_browser_serial(browser_list, test_groups):
    for test in test_groups:
        for browser in browser_list:
            execute_test_with_browser(browser, test)


def run_tests_for_browser_parallel(browser_list, test_groups):
    task_list = [(browser, test_case) for browser in browser_list for test_case in test_groups]

    with ThreadPoolExecutor(max_workers=min(len(all_test_groups), 8)) as executor:
        [executor.submit(execute_test_with_browser, browser, test) for browser, test in task_list]


if __name__ == "__main__":
    config_manager = ConfigurationManager()
    settings = config_manager.load_settings()
    is_parallel = settings['parallel']
    is_serial = not settings['parallel']
    browsers = settings["browser_types"]
    grid_url = settings["hub"]
    if is_parallel:
        run_tests_for_browser_parallel(browsers, parallel_test_groups_one)
        run_tests_for_browser_serial(browsers, all_test_group_two)
    elif is_serial:
        run_tests_for_browser_serial(browsers, all_test_groups)
