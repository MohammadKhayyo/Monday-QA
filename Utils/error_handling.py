import traceback


def report_status(self):
    for test, exc_info in self._outcome.errors:
        if exc_info:
            # This will format the exception information into a string
            error_type, error_instance, error_traceback = exc_info
            formatted_traceback = ''.join(traceback.format_exception(error_type, error_instance, error_traceback))
            description = f"Test {self._testMethodName} failed: {str(error_instance)}\n{formatted_traceback}"
            error_message = f"{self._test_errors}" if self._test_errors else description
            issue_key = self.jira.create_issue(self.summary, error_message,
                                               self.project_key)
            print(f"Created JIRA issue: {issue_key}")


def assertAndCapture(self, assertion_callable, *args, **kwargs):
    try:
        assertion_callable(*args, **kwargs)
    except Exception as e:  # Catch any kind of exception
        self._test_errors = (e.__class__.__name__, str(e), e.__traceback__)
        raise
