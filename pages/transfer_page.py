from playwright.sync_api import Page, expect

from components.sidebar import Sidebar


class TransferPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.sidebar = Sidebar(page)
        
        self.transfer_heading_locator = page.get_by_test_id(
            "transfer-page-title"
        )

        self.source_select_locator = page.get_by_test_id(
            "transfer-from-select"
        )
        self.source_account_option_locator = lambda account_name: (
            page.get_by_test_id("transfer-from-option").filter(
                has_text=account_name
            )
        )

        self.destination_select_locator = page.get_by_test_id(
            "transfer-to-select"
        )
        self.destination_account_option_locator = lambda account_name: (
            page.get_by_test_id("transfer-to-option").filter(
                has_text=account_name
            )
        )

        self.amount_input_locator = page.get_by_test_id(
            "transfer-amount-input"
        )

        self.review_button_locator = page.get_by_role(
            "button", name = "Review Transfer"
        )
        self.confirm_button_locator = page.get_by_test_id(
            "confirm-transfer-btn"
        )
        self.return_dashboard_button_locator = page.get_by_test_id(
            "back-to-dashboard-btn"
        )   

    def expect_loaded(self) -> None:
        expect(self.transfer_heading_locator).to_be_visible()

    def transfer_money(self, sender: str, recipient: str, amount: str) -> None:

        self.source_select_locator.click() 
        self.source_account_option_locator(sender).click()

        self.destination_select_locator.click()
        self.destination_account_option_locator(recipient).click()

        self.amount_input_locator.fill(amount)

        self.review_button_locator.click()
        
        self.confirm_button_locator.click()

        self.return_dashboard_button_locator.click()
       

      
