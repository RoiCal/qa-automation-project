from playwright.sync_api import Page


class Sidebar:
    def __init__(self, page: Page) -> None:
        self.accounts_link = page.get_by_test_id("sidebar-link-accounts")
        self.transfer_link = page.get_by_test_id("sidebar-link-transfer")
        self.send_money_link = page.get_by_test_id("sidebar-link-send-money")
        self.bill_pay_link = page.get_by_test_id("sidebar-link-bill-pay")
        self.transactions_link = page.get_by_test_id("sidebar-link-transactions")
        self.apply_loan_link = page.get_by_test_id("sidebar-link-apply-loan")

    def open_accounts(self) -> None:
        self.accounts_link.click()
