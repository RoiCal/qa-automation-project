from decimal import Decimal

from playwright.sync_api import Locator, Page, expect

from components.sidebar import Sidebar
from utils.money import parse_money


class TransactionsPage:
    """Provides transaction-history interactions and assertions."""

    AMOUNT_CELL_INDEX = 4 # constant variable

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
        )

    def get_transaction_amount(
        self,
        transaction_row: Locator,
    ) -> Decimal:
        """Return the amount displayed in the a wanted transaction row."""
        cells = transaction_row.get_by_role("cell")

        amount_text = cells.nth(
            self.AMOUNT_CELL_INDEX
        ).inner_text()

        return parse_money(amount_text)

    # def expect_transfer_visible(
    #     self,
    #     sender: str,
    #     recipient: str,
    #     amount: Decimal,
    # ) -> None:
    #     """Verify the debit and credit records for a completed transfer."""
    #     debit_row = self.get_transfer_row(
    #         sender,
    #         f"Transfer to {recipient}",
    #     )

    #     credit_row = self.get_transfer_row(
    #         recipient,
    #         f"Transfer from {sender}",
    #     )

    #     expect(debit_row).to_be_visible()
    #     expect(credit_row).to_be_visible()

    #     debit_amount = self.get_transaction_amount(debit_row)
    #     credit_amount = self.get_transaction_amount(credit_row)

    #     assert debit_amount == -amount
    #     assert credit_amount == amount