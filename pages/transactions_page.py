from decimal import Decimal

from playwright.sync_api import Locator, Page, expect

from components.sidebar import Sidebar
from utils.money import parse_money


class TransactionsPage:
    """Provides transaction-history interactions and assertions."""

    AMOUNT_CELL_INDEX = 4

    def __init__(self, page: Page) -> None:
        self.page = page
        self.sidebar = Sidebar(page)
        self.transactions_heading = page.get_by_test_id(
            "transactions-page-title"
        )

    def expect_loaded(self) -> None:
        """Verify that the transactions page is visible."""
        expect(self.transactions_heading).to_be_visible()

    def get_transfer_row(
        self,
        account_name: str,
        description: str,
    ) -> Locator:
        """Return the transaction row matching the account and description."""
        return (
            self.page.get_by_role("row")
            .filter(has_text=account_name)
            .filter(has_text=description)
            .first
        )

    def get_transaction_amount(
        self,
        transaction_row: Locator,
    ) -> Decimal:
        """Return the amount displayed in the requested transaction row."""

        cells = transaction_row.get_by_role("cell")

        amount_text = cells.nth(
            self.AMOUNT_CELL_INDEX
        ).inner_text()

        return parse_money(amount_text)
