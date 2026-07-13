from decimal import Decimal

from playwright.sync_api import Page, expect

from components.sidebar import Sidebar


class TransferPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.sidebar = Sidebar(page)
        self.transfer_heading = page.get_by_test_id("transfer-page-title")

    def expected_loaded(self) -> None:
        expect(self.transfer_heading).to_be_visible()

    def transfer_money(self, sender: str, recipient: str, amount: str) -> None:
        self.page.get_by_test_id("transfer-from-select").click()
        self.page.get_by_text(sender).click()

        self.page.get_by_test_id("transfer-to-select").click()
        self.page.get_by_test_id("transfer-to-option").get_by_text(recipient)
        self.page.get_by_test_id("transfer-to-option").click()

        self.page.get_by_test_id("transfer-amount-input").click()
        self.page.get_by_test_id("transfer-amount-input").fill(amount)

        self.page.get_by_test_id("review-transfer-btn").click()
        self.page.get_by_test_id("confirm-transfer-btn").click()
        self.page.get_by_test_id("back-to-dashboard-btn").click()
