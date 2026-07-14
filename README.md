# QA Automation Project With Playwright

This project contains an end-to-end automated test for the QA Playground Bank application.

The main test checks a money transfer between two bank accounts.

## What the test does

The test performs the following steps:

1. Logs in to the bank application.
2. Opens the accounts page.
3. Reads the balances of the source and destination accounts.
4. Transfers money between the accounts.
5. Verifies that the source account balance was reduced.
6. Verifies that the destination account balance was increased.
7. Opens the transactions page.
8. Verifies the debit and credit transaction records.

## Technologies

- Python
- Playwright
- pytest
- pytest-playwright
- pytest-html
- python-dotenv

## Project Structure

```text
qa-automation-project/
├── components/
│   └── sidebar.py
├── pages/
│   ├── accounts_page.py
│   ├── dashboard_page.py
│   ├── login_page.py
│   ├── transactions_page.py
│   └── transfer_page.py
├── tests/
│   ├── test_smoke.py
│   └── test_transfer_flow.py
├── utils/
│   └── money.py
├── conftest.py
├── pytest.ini
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## Requirements

Before running the project, make sure the following are installed:

- Python 3.12 or later
- Git

## Installation

Clone the repository:

```bash
git clone https://github.com/RoiCal/qa-automation-project.git
cd qa-automation-project
```

Create a virtual environment:

```bash
python3 -m venv .venv
```

Activate it on Linux:

```bash
source .venv/bin/activate
```

Activate it on Windows:

```powershell
.venv\Scripts\activate
```

Install the project packages:

```bash
pip install -r requirements.txt
```

Install Chromium for Playwright:

```bash
playwright install chromium
```

## Environment Configuration

Create a local `.env` file:

```bash
cp .env.example .env
```

Add the following values:

```env
BASE_URL=https://qaplayground.com/bank
BANK_USERNAME=<your-username>
BANK_PASSWORD=<your-password>
```
The login credentials are provided at the bottom of the QA Playground Bank login page.
The `.env` file is ignored by Git and is not uploaded to the repository.

## Running the Tests

Run all tests:

```bash
pytest
```

Run the transfer test:

```bash
pytest tests/test_transfer_flow.py
```

Run with a visible browser:

```bash
pytest tests/test_transfer_flow.py --headed
```

## HTML Report

Create an HTML report:

```bash
pytest tests/test_transfer_flow.py \
  --html=reports/report.html \
  --self-contained-html
```

Open the report on Linux:

```bash
xdg-open reports/report.html
```

Open the report on Windows:

```powershell
start reports\report.html
```

The report shows the test name, result and execution time.

## Failure Files

When a test fails, Playwright can save:

- A screenshot
- A trace file

These files are saved in:

```text
test-results/
```

Open a trace file with:

```bash
playwright show-trace path/to/trace.zip
```

## Repository

https://github.com/RoiCal/qa-automation-project