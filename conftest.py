import os
from collections.abc import Callable
from html import escape

import pytest
import pytest_html
from dotenv import load_dotenv
from pytest import FixtureRequest

# Loads variables from the local .env file.
load_dotenv()


@pytest.fixture(scope="session")
def app_url() -> str:
    """Return the application URL from the environment."""
    url = os.getenv("BASE_URL")

    if not url:
        raise ValueError("BASE_URL is not defined in the .env file")

    return url


@pytest.fixture(scope="session")
def bank_credentials() -> tuple[str, str]:
    """Return the bank login credentials from the environment."""
    username = os.getenv("BANK_USERNAME")
    password = os.getenv("BANK_PASSWORD")

    if not username or not password:
        raise ValueError(
            "BANK_USERNAME and BANK_PASSWORD must be defined in the .env file"
        )

    return username, password


@pytest.fixture
def report_step(request: FixtureRequest) -> Callable[[str], None]:
    """Provide a function for adding test steps to the HTML report."""
    steps: list[str] = []

    # Saves the steps on the current pytest test item.
    request.node.report_steps = steps

    def add_step(description: str) -> None:
        """Add one numbered step to the current test report."""
        step_number = len(steps) + 1
        steps.append(f"Step {step_number}: {description}")

    return add_step


def build_steps_html(steps: list[str]) -> str:
    """Build a readable HTML section for the collected test steps."""
    step_items = "".join(
        f"<li>{escape(step)}</li>"
        for step in steps
    )

    return (
        "<div>"
        "<h3>Test Steps and Results</h3>"
        f"<ol>{step_items}</ol>"
        "</div>"
    )


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(
    item: pytest.Item,
    call: pytest.CallInfo,
):
    """Attach collected test steps to the pytest-html report."""
    outcome = yield
    report = outcome.get_result()

    # Adds steps only to the main test execution result.
    if report.when != "call":
        return

    steps = getattr(item, "report_steps", [])

    if not steps:
        return

    extras = getattr(report, "extras", [])

    extras.append(
        pytest_html.extras.html(
            build_steps_html(steps)
        )
    )

    report.extras = extras