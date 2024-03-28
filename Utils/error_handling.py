import pytest


@pytest.mark.skip(reason="This function handle the error")
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
            args[0].error_msg = str(e)
            raise

    return wrapper
