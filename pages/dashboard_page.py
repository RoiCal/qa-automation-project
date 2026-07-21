from playwright.sync_api import Page, expect

from components.sidebar import Sidebar


class DashboardPage:
    """Represents the authenticated dashboard displayed after login."""

    def __init__(self, page: Page) -> None:
        self.page = page
        self.sidebar = Sidebar(page)
        
        self.dashboard_heading = page.get_by_test_id(
            "dashboard-welcome-message"
        )

    def expect_loaded(self) -> None:
        """Verify that the dashboard's unique welcome element is visible."""
        expect(self.dashboard_heading).to_be_visible()
