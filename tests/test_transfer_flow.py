from decimal import Decimal
import pytest
import pytest_html
from collections.abc import Callable

from playwright.sync_api import Page, expect

from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.accounts_page import AccountsPage
from pages.transfer_page import TransferPage
from pages.transactions_page import TransactionsPage


##TODO change the hardcoded accounts and amount to a test_data file 
@pytest.mark.parametrize(
    "source_account,destination_account,amount",
    [
        (
            "Everyday Checking",
            "High-Yield Savings",
            Decimal("1000.00"),
        ),
    ],
    # ids provides a clear name to the report data set
    ids=["checking-to-savings-1000"],
)

def test_successful_account_transfer(
    page: Page,
    app_url: str,
    bank_credentials: tuple[str, str],
    source_account: str,
    destination_account: str,
    amount: Decimal,
    report_step: Callable[[str], None],
) -> None:

    test_steps = []

    login_page = LoginPage(page)
    dashboard_page = DashboardPage(page)
    accounts_page = AccountsPage(page)
    transfer_page = TransferPage(page)
    transactions_page = TransactionsPage(page)

    username, password = bank_credentials

    login_page.open(app_url)
    login_page.login(
        username,
        password,
    )

    dashboard_page.expect_loaded()

    report_step(
        "Login completed successfully and the dashboard was displayed."
    )

    dashboard_page.sidebar.open_accounts()
    accounts_page.expect_loaded()

    source_balance_before = accounts_page.get_account_balance(
        source_account
    )

    destination_balance_before = accounts_page.get_account_balance(
        destination_account
    )

    report_step(
        f"Initial balances were read: "
        f"{source_account} = {source_balance_before}, "
        f"{destination_account} = {destination_balance_before}."
    )

    accounts_page.sidebar.open_transfer()
    transfer_page.expect_loaded()

    transfer_page.transfer_money(
        source_account,
        destination_account,
        str(amount),
    )

    report_step(
        f"Transferred {amount} from "
        f"{source_account} to {destination_account}."
    )

    transfer_page.sidebar.open_accounts()
    accounts_page.expect_loaded()

    source_balance_after = accounts_page.get_account_balance(
        source_account
    )

    destination_balance_after = accounts_page.get_account_balance(
        destination_account
    )

    assert source_balance_after == source_balance_before - amount
    assert destination_balance_after == destination_balance_before + amount

    report_step(
        f"Balances were updated correctly: "
        f"{source_account} = {source_balance_after}, "
        f"{destination_account} = {destination_balance_after}."
    )

    accounts_page.sidebar.open_transactions()
    transactions_page.expect_loaded()

    debit_row = transactions_page.get_transfer_row(
        source_account,
        f"Transfer to {destination_account}",
    )

    credit_row = transactions_page.get_transfer_row(
        destination_account,
        f"Transfer from {source_account}",
    )

    expect(debit_row).to_be_visible()
    expect(credit_row).to_be_visible()

    debit_amount = transactions_page.get_transaction_amount(
        debit_row
    )

    credit_amount = transactions_page.get_transaction_amount(
        credit_row
    )

    assert debit_amount == -amount
    assert credit_amount == amount

    report_step(
        f"Transaction history was verified: "
        f"debit = {debit_amount}, credit = {credit_amount}."
    )
