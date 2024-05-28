import pytest


@pytest.mark.skip(reason="This test handel the error")
def test_decorator(test_func):
    def wrapper(*args, **kwargs):
        try:
            test_func(*args, **kwargs)
        except AssertionError as e:
            print(f"Assertion Error in {test_func.__name__}: {e}")
            args[0].test_failed = True
            args[0].error_msg = str(e)
            raise
        except Exception as e:
            print(f"Unexpected Error in {test_func.__name__}: {e}")
            args[0].test_failed = True
            raise

    return wrapper


# Hook to modify the Pytest test report
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, f"rep_{rep.when}", rep)


# Fixture automatically applied to each test for handling outcomes
@pytest.fixture(autouse=True)
def handle_test_outcomes(request):
    yield
    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
        # Logic for failed tests
        test_name = request.node.nodeid
        print(f"Test failed: {test_name}")
        # Here, you can integrate custom logic such as creating a JIRA issue

        # Example: Log the failure or call a function to handle the failure
        # This could be logging to a file, sending an email, or any other action
        # log_test_failure(test_name, request.node.rep_call.longreprtext)
