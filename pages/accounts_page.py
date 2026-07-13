from playwright.sync_api import Page, expect
from decimal import Decimal
from components.sidebar import Sidebar


class AccountsPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.sidebar = Sidebar(page)
        self.accounts_heading = page.get_by_test_id("accounts-page-title")

    def expect_loaded(self) -> None:
        expect(self.accounts_heading).to_be_visible()

    def get_account_balance(self, account_name: str) -> Decimal:
        checking_row = self.page.get_by_role("row").filter(has_text=account_name)
        cells = checking_row.get_by_role("cell")
        balance_cell = 2
        print(balance_cell, "-->", cells.nth(balance_cell).inner_text())
        pass
