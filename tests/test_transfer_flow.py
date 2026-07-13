from playwright.sync_api import Page, expect

from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.accounts_page import AccountsPage
from pages.transfer_page import TransferPage

# Login
# → Dashboard
# → Accounts
# → קריאת יתרת חשבון מקור
# → קריאת יתרת חשבון יעד
# → Transfer
# → קריאת היתרות שוב
# → השוואה


def test_successful_account_transfer(
    page: Page,
    app_url: str,
) -> None:

    login_page = LoginPage(page)
    dashboard_page = DashboardPage(page)
    accounts_page = AccountsPage(page)
    transfare_page = TransferPage(page)

    login_page.open(app_url)
    login_page.login(
        "standard_user",
        "bank_sauce",
    )

    dashboard_page.expect_loaded()

    dashboard_page.sidebar.open_accounts()
    accounts_page.expect_loaded()

    # hardcoded
    account_name = "Everyday Checking"
    recipient_name = "High-Yield Savings"
    #
    account_balance = accounts_page.get_account_balance(account_name)

    accounts_page.sidebar.open_transfer()
    transfare_page.expected_loaded()

    ########### [ TEMP CODE ]
    print("Account balance is:", account_balance)
    transfare_page.transfer_money(account_name, recipient_name, 1000)
    # name="Everyday Checking"

    # cells = checking_row.get_by_role("cell")
    # print("num of cells:", cells.count())
    # balance_cell = 2
    # print(balance_cell, "-->", cells.nth(balance_cell).inner_text())

    # # print("Matching rows:", checking_row.count())
    # print("Checking row text:")
    # print(checking_row.inner_text())


###########
