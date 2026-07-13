from decimal import Decimal

from playwright.sync_api import Page, expect

from components.sidebar import Sidebar


class AccountsPage:
    """Provides account-table interactions and balance extraction."""

    BALANCE_CELL_INDEX = 2

    def __init__(self, page: Page) -> None:
        self.page = page
        self.sidebar = Sidebar(page)
        self.accounts_heading = page.get_by_test_id("accounts-page-title")

    def expect_loaded(self) -> None:
        """Verify that the accounts page is displayed."""
        expect(self.accounts_heading).to_be_visible()

    def get_account_balance(self, account_name: str) -> Decimal:
        """Return the displayed balance for the requested account as Decimal."""
        account_row = self.page.get_by_role("row").filter(has_text=account_name)
        cells = account_row.get_by_role("cell")
        balance_text = cells.nth(self.BALANCE_CELL_INDEX).inner_text()

        fixed_balance = balance_text.replace("$", "").replace(",", "")

        return Decimal(fixed_balance)
