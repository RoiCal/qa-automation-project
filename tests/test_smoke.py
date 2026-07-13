from playwright.sync_api import Page, expect

def test_bank_site_opens(page: Page, app_url: str) -> None:
	page.goto(app_url)

	expect(page).to_have_title(
		"QA Playground - Master Automation Testing"
	)