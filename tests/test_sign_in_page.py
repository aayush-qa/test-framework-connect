"""
Test module for Sign In Page functionality
"""

import pytest
from pages.SignIn import SignInPage
from pages.Splash import SplashScreen


class TestSignInPageNavigation:
    """Test cases for Sign In page navigation"""

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        """Setup test with page objects"""
        self.splash_screen = SplashScreen(driver)
        self.sign_in_page = SignInPage(driver)
        self.splash_screen.handle_permission_dialog()

    def test_back_button_on_sign_in_page(self):
        """Verify Back button is displayed on Sign In page"""
        # Navigate to Sign In page
        self.splash_screen.click_sign_in_button()
        self.sign_in_page.handle_system_permission_dialog()
        
        # Verify Sign In page is loaded
        assert self.sign_in_page.is_sign_in_page_loaded()
        
        # Verify Back button is displayed
        assert self.sign_in_page.is_back_button_displayed()

    def test_back_button_navigation_to_splash(self):
        """Verify Back button navigates back to Splash screen"""
        # Navigate to Sign In page
        self.splash_screen.click_sign_in_button()
        self.sign_in_page.handle_system_permission_dialog()
        
        # Click Back button to return to Splash screen
        self.sign_in_page.click_back_button()
        
        # Verify we're back at Splash screen by checking Sign Up button
        assert self.splash_screen.is_sign_up_button_displayed()

    def test_complete_registration_flow_from_splash(self):
        """
        Test complete flow: Splash -> Sign In -> Back to Splash -> Sign Up
        This ensures the back button allows registration flow to continue
        """
        # Step 1: Verify Splash screen is loaded
        assert self.splash_screen.is_splash_screen_loaded()
        
        # Step 2: Click Sign In button to navigate to Sign In page
        self.splash_screen.click_sign_in_button()
        self.sign_in_page.handle_system_permission_dialog()
        
        # Step 3: Verify Sign In page loaded
        assert self.sign_in_page.is_sign_in_page_loaded()
        
        # Step 4: Click Back button to return to Splash screen
        self.sign_in_page.click_back_button()
        
        # Step 5: Verify back at Splash screen
        assert self.splash_screen.is_splash_screen_loaded()
        
        # Step 6: Click Sign Up button to continue registration flow
        self.splash_screen.click_sign_up_button()
        # Step 7: Verify Sign Up page loaded (Splash screen no longer visible)
        assert not self.splash_screen.is_splash_screen_loaded()
