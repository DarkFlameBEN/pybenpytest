"""Pytest plugin - generated with the help of ChatGPT"""
import pytest


# Define a custom exception for invalid tests
class InvalidTestError(Exception):
    pass


@pytest.hookimpl(tryfirst=True)
def pytest_runtest_setup(item):
    """Check if @pytest.mark.invalidif is applied and the condition is True."""
    invalid_mark = item.get_closest_marker("invalidif")
    if invalid_mark:
        condition = invalid_mark.args[0] if invalid_mark.args else False  # Extract condition
        reason = invalid_mark.kwargs.get("reason", "Marked as INVALID")  # Extract reason

        if condition:
            pytest.fail(f"INVALID: {reason}")


# Modify test reports to show "INVALID" instead of "FAILED"
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Customize the test report to include INVALID status."""
    outcome = yield
    report = outcome.get_result()

    if call.excinfo and call.excinfo.errisinstance(InvalidTestError):
        report.outcome = "invalid"
        report.longrepr = f"Invalid: {call.excinfo.value}"
    if report.failed and "INVALID:" in str(report.longrepr):
        report.outcome = "invalid"
        report.longrepr = f"Invalid: {str(report.longrepr)}"


# Define pytest.invalid() globally
def invalid(reason="Test marked as INVALID"):
    pytest.fail(f"INVALID: {reason}")


# Attach invalid() to pytest as pytest.invalid()
setattr(pytest, "invalid", invalid)


# Register @pytest.mark.invalidif(condition=True, reason="message")
def pytest_configure(config):
    """Register the invalidif marker for documentation."""
    config.addinivalue_line(
        "markers", "invalidif(condition, reason): Mark test as INVALID (failed) if condition is True"
    )


# Modify pytest output to distinguish INVALID from normal FAILED tests
@pytest.hookimpl(tryfirst=True)
def pytest_report_teststatus(report):
    """Modify test output so INVALID appears in pytest results."""
    if report.outcome == "invalid":
        return "invalid", "I", "INVALID"  # Custom output for INVALID
