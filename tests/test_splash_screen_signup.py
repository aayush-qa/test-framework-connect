"""
Test module for Splash Screen functionality
"""

import pytest
from pages.Splash import SplashScreen
from pages.SignIn import SignInPage


class TestSplashScreenUI:
    """Test cases for Splash Screen UI elements"""

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        """Setup test with Splash Screen page object"""
        self.splash_screen = SplashScreen(driver)

    # def test_allow_button_clicked(self):
    def test_splash_screen_is_loaded(self):
        """Verify Splash Screen is fully loaded with all main elements"""
        assert self.splash_screen.is_splash_screen_loaded()

    def test_app_title_and_subtitle(self):
        """Verify app title and subtitle are displayed"""
        assert self.splash_screen.get_app_title() == "Connect"
        assert self.splash_screen.get_app_subtitle() == "Persona"

    def test_app_tagline(self):
        """Verify app tagline is correct"""
        assert self.splash_screen.get_app_tagline() == "Connections Made Easy"


class TestSplashScreenSignIn:
    """Test cases for Sign In functionality"""

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        """Setup test with Splash Screen page object"""
        self.splash_screen = SplashScreen(driver)

    def test_sign_in_button_is_displayed(self):
        """Verify Sign In button is displayed"""
        assert self.splash_screen.is_sign_in_button_displayed()

    def test_click_sign_in_button(self):
        """Verify Sign In button click action navigates to Sign In page"""
        from pages.SignIn import SignInPage
        self.splash_screen.click_sign_in_button()
        # Verify we're on Sign In page by checking email field is present
        sign_in_page = SignInPage(self.splash_screen.driver)
        assert sign_in_page.is_sign_in_page_loaded()


class TestSplashScreenSignUp:
    """Test cases for Sign Up functionality"""

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        """Setup test with Splash Screen and Sign In page objects"""
        self.splash_screen = SplashScreen(driver)
        self.sign_in_page = SignInPage(driver)

    def ensure_splash_screen(self):
        """Ensure the app is on the Splash screen before interacting with splash elements"""
        # Handle any permission dialogs first
        self.splash_screen.handle_permission_dialog()
        
        if not self.splash_screen.is_splash_screen_loaded():
            if self.sign_in_page.is_sign_in_page_loaded():
                self.sign_in_page.click_back_button()
        assert self.splash_screen.is_splash_screen_loaded()

    def test_sign_up_button_is_displayed(self):
        """Verify Sign Up button is displayed"""
        self.ensure_splash_screen()
        assert self.splash_screen.is_sign_up_button_displayed()

    def test_sign_up_button_is_enabled(self):
        """Verify Sign Up button is enabled"""
        self.ensure_splash_screen()
        assert self.splash_screen.is_sign_up_button_enabled()

    def test_sign_up_button_text(self):
        """Verify Sign Up button has correct text"""
        self.ensure_splash_screen()
        button_text = self.splash_screen.get_sign_up_button_text()
        assert button_text.lower() == "sign up"

    def test_click_sign_up_button(self):
        """Verify clicking Sign Up button navigates away from Splash screen"""
        self.ensure_splash_screen()
        self.splash_screen.click_sign_up_button()
        # Verify Sign Up button is no longer clickable/accessible (we've navigated away)
        # or verify the page changed by checking the splash screen is no longer fully loaded
        assert not self.splash_screen.is_splash_screen_loaded()

    def test_click_create_account_for_business(self):
        """Verify clicking Create Account link navigates away from Splash screen"""
        self.ensure_splash_screen()
        assert self.splash_screen.is_create_account_link_displayed()
        self.splash_screen.click_create_account_for_business()
        # Verify we navigated away from the Splash screen
        assert not self.splash_screen.is_splash_screen_loaded()


class TestSocialLogin:
    """Test cases for Social Login buttons"""

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        """Setup test with Splash Screen page object"""
        self.splash_screen = SplashScreen(driver)

    def test_google_login_button_is_displayed(self):
        """Verify Continue with Google button is displayed"""
        assert self.splash_screen.is_google_button_displayed()

    def test_apple_login_button_is_displayed(self):
        """Verify Continue with Apple button is displayed"""
        assert self.splash_screen.is_apple_button_displayed()

    def test_click_google_login_button(self):
        """Verify clicking Continue with Google button navigates away from Splash"""
        self.splash_screen.click_continue_with_google()
        # Verify we navigated away from the Splash screen (Google login/webview triggered)
        assert not self.splash_screen.is_splash_screen_loaded()

    def test_click_apple_login_button(self):
        """Verify clicking Continue with Apple button navigates away from Splash"""
        self.splash_screen.click_continue_with_apple()
        # Verify we navigated away from the Splash screen (Apple login/webview triggered)
        assert not self.splash_screen.is_splash_screen_loaded()


class TestSplashScreenLinks:
    """Test cases for legal links on Splash Screen"""

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        """Setup test with Splash Screen page object"""
        self.splash_screen = SplashScreen(driver)

    def test_click_terms_and_conditions(self):
        """Verify Terms and Conditions link is clickable and navigates"""
        self.splash_screen.click_terms_and_conditions()
        # Verify we navigated away from the Splash screen (Terms page opened)
        assert not self.splash_screen.is_splash_screen_loaded()

    def test_click_privacy_policy(self):
        """Verify Privacy Policy link is clickable and navigates"""
        self.splash_screen.click_privacy_policy()
        # Verify we navigated away from the Splash screen (Privacy Policy page opened)
        assert not self.splash_screen.is_splash_screen_loaded()
