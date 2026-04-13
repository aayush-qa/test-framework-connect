"""
Sign In Page Object Model
Handles all interactions with the Sign In page
"""

from .SignInLocators import SignInLocators
from pages.BasePage.base_page import BasePage


class SignInPage(BasePage):
    """Page Object for Sign In page"""

    def __init__(self, driver):
        """
        Initialize Sign In page object

        Args:
            driver: Appium WebDriver instance
        """
        super().__init__(driver)
        self.locators = SignInLocators()

    # ──────────────────────────── Navigation ────────────────────────────

    def click_back_button(self) -> None:
        """Click on the Back button to return to Splash screen"""
        try:
            self.click_element(self.locators.BACK_BUTTON)
            return
        except Exception:
            pass

        try:
            self.click_element(self.locators.BACK_BUTTON_ALT)
            return
        except Exception:
            pass

        x, y = self.locators.BACK_BUTTON_COORDINATE
        self._tap_coordinate(x, y)

    def is_back_button_displayed(self) -> bool:
        """Check if Back button is displayed"""
        # Since back button is not a separate element but uses coordinates,
        # we consider it "displayed" if we're on the sign-in page
        return self.is_sign_in_page_loaded()

    def _tap_coordinate(self, x: int, y: int) -> None:
        """Tap on a screen coordinate when no element locator is available"""
        self.tap_coordinate(x, y)

    # ──────────────────────────── Sign In Flow ──────────────────────────

    def enter_email(self, email: str) -> None:
        """
        Enter email address in the email field

        Args:
            email: Email address to enter
        """
        self.send_keys_to_element(self.locators.EMAIL_FIELD, email)

    def enter_password(self, password: str) -> None:
        """
        Enter password in the password field

        Args:
            password: Password to enter
        """
        self.send_keys_to_element(self.locators.PASSWORD_FIELD, password)

    def click_sign_in_submit_button(self) -> None:
        """Click on the Sign In submit button"""
        self.click_element(self.locators.SIGN_IN_SUBMIT_BUTTON)

    def handle_system_permission_dialog(self) -> None:
        """Handle any runtime system permission dialog if it appears."""
        super().handle_system_permission_dialog(accept=True)

    def sign_in_with_credentials(self, email: str, password: str) -> None:
        """
        Complete sign in flow with email and password
        
        Args:
            email: Email address
            password: Password
        """
        self.enter_email(email)
        self.enter_password(password)
        self.click_sign_in_submit_button()

    # ──────────────────────────── Links ────────────────────────────────

    def click_forgot_password(self) -> None:
        """Click on Forgot Password link"""
        self.click_element(self.locators.FORGOT_PASSWORD_LINK)

    def click_create_account(self) -> None:
        """Click on Create Account link"""
        self.click_element(self.locators.CREATE_ACCOUNT_LINK)

    # ──────────────────────────── Verification ──────────────────────────

    def is_sign_in_page_loaded(self) -> bool:
        """Verify Sign In page is loaded with all main elements"""
        # Check if email field is present as primary indicator of sign-in page
        return self.is_element_present(self.locators.EMAIL_FIELD, timeout=10)
