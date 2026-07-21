from playwright.sync_api import Page


class LoginPage:
    """Encapsulates interactions with the bank application's login screen."""

    def __init__(self, page: Page) -> None:
        self.page = page
        self.username_input = page.get_by_test_id(
            "login-username-input"
        )

        self.password_input = page.get_by_test_id(
            "login-password-input"
        )
        
        self.login_button = page.get_by_test_id(
            "login-submit-btn"
        )

    def open(self, app_url: str) -> None:
        """Open the login page using the configured application base URL."""
        self.page.goto(f"{app_url}/login")

    def login(self, username: str, password: str) -> None:
        """Submit valid or invalid credentials through the login form."""
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()
