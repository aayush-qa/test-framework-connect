"""
Splash Screen Page Object Model
Handles all interactions with the Splash Screen
"""

from pages.Splash.SplashScreenLocators import SplashScreenLocators
from pages.BasePage.base_page import BasePage


class SplashScreen(BasePage):
    """Page Object for Splash Screen"""

    def __init__(self, driver):
        """
        Initialize Splash Screen page object

        Args:
            driver: Appium WebDriver instance
        """
        super().__init__(driver)
        self.locators = SplashScreenLocators()

    # ──────────────────────────── Sign In ─────────────────────────────
    
    def click_allow_button(self) -> None:
        """Click on the Allow button in permission pop-up"""
        self.click_element(self.locators.ALLOW_PERMISSIONS_BUTTON)
        
    def is_allow_button_displayed(self) -> bool:
        """Check if Allow button is displayed in permission dialog"""
        return self.is_element_displayed(self.locators.ALLOW_PERMISSIONS_BUTTON, timeout=5)
        
    def handle_permission_dialog(self) -> None:
        """Handle a runtime system permission dialog if it appears."""
        self.handle_system_permission_dialog(accept=True)

    def click_sign_in_button(self) -> None:
        """Click on the Sign In button"""
        self.click_element(self.locators.SIGN_IN_BUTTON)

    def is_sign_in_button_displayed(self) -> bool:
        """Check if Sign In button is displayed"""
        return self.is_element_displayed(self.locators.SIGN_IN_BUTTON)

    # ──────────────────────────── Sign Up ─────────────────────────────

    def click_sign_up_button(self) -> None:
        """Click on the Sign Up button"""
        self.click_element(self.locators.SIGN_UP_BUTTON)

    def is_sign_up_button_displayed(self) -> bool:
        """Check if Sign Up button is displayed"""
        return self.is_element_displayed(self.locators.SIGN_UP_BUTTON)

    def is_sign_up_button_enabled(self) -> bool:
        """Check if Sign Up button is enabled"""
        return self.is_element_enabled(self.locators.SIGN_UP_BUTTON)

    def get_sign_up_button_text(self) -> str:
        """Get the text of Sign Up button"""
        element = self.wait_for_element_visible(self.locators.SIGN_UP_BUTTON)
        return element.text

    # ──────────────────────────── Social Login ────────────────────────

    def click_continue_with_google(self) -> None:
        """Click on Continue with Google button"""
        self.click_element(self.locators.CONTINUE_WITH_GOOGLE_BUTTON)

    def is_google_button_displayed(self) -> bool:
        """Check if Continue with Google button is displayed"""
        return self.is_element_displayed(self.locators.CONTINUE_WITH_GOOGLE_BUTTON)

    def click_continue_with_apple(self) -> None:
        """Click on Continue with Apple button"""
        self.click_element(self.locators.CONTINUE_WITH_APPLE_BUTTON)

    def is_apple_button_displayed(self) -> bool:
        """Check if Continue with Apple button is displayed"""
        return self.is_element_displayed(self.locators.CONTINUE_WITH_APPLE_BUTTON)

    # ──────────────────────────── Links ────────────────────────────────

    def click_create_account_for_business(self) -> None:
        """Click on Create an Account link for Business or Brand"""
        self.click_element(self.locators.CREATE_ACCOUNT_LINK)

    def is_create_account_link_displayed(self) -> bool:
        """Check if Create Account link is displayed"""
        return self.is_element_displayed(self.locators.CREATE_ACCOUNT_LINK)

    def click_terms_and_conditions(self) -> None:
        """Click on Terms and Conditions link"""
        self.click_element(self.locators.TERMS_AND_CONDITIONS_LINK)

    def click_privacy_policy(self) -> None:
        """Click on Privacy Policy link"""
        self.click_element(self.locators.PRIVACY_POLICY_LINK)

    # ──────────────────────────── App Info ──────────────────────────────

    def get_app_title(self) -> str:
        """Get the app title (Connect)"""
        element = self.wait_for_element_visible(self.locators.APP_LOGO)
        return element.text

    def get_app_subtitle(self) -> str:
        """Get the app subtitle (Persona)"""
        element = self.wait_for_element_visible(self.locators.APP_SUBTITLE)
        return element.text

    def get_app_tagline(self) -> str:
        """Get the app tagline (Connections Made Easy)"""
        element = self.wait_for_element_visible(self.locators.APP_TAGLINE)
        return element.text

    # ──────────────────────────── Verification ──────────────────────────

    def is_splash_screen_loaded(self) -> bool:
        """Verify all main elements are displayed on splash screen"""
        return (
            self.is_sign_in_button_displayed()
            and self.is_sign_up_button_displayed()
            and self.is_google_button_displayed()
            and self.is_apple_button_displayed()
        )
