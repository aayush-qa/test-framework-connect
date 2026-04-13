"""
Splash Screen Locators
Centralized locator definitions for Splash Screen elements

Locator Strategy:
- accessibility id: Used for elements with content-desc attribute (main strategy)
- id: Used for resource-id (full path like "com.package:id/element")
- -android uiautomator: Used for UIAutomator2 selector queries
- xpath: Used as fallback only when other strategies fail
"""


class SplashScreenLocators:
    """Locators for Splash Screen page"""

    # Main Buttons (using accessibility_id for content-desc)
    SIGN_IN_BUTTON = ("accessibility id", "Sign in")
    SIGN_UP_BUTTON = ("accessibility id", "Sign up")
    
    # Social Login Buttons
    CONTINUE_WITH_GOOGLE_BUTTON = ("accessibility id", "Continue with Google")
    CONTINUE_WITH_APPLE_BUTTON = ("accessibility id", "Continue with Apple")

    # System permission dialog (resource-id from Android system)
    ALLOW_PERMISSIONS_BUTTON = ("id", "com.android.permissioncontroller:id/permission_allow_button")
    
    # Text and Links (using accessibility_id for content-desc)
    CREATE_ACCOUNT_LINK = ("accessibility id", "Create an Account for Business or Brand")
    TERMS_AND_CONDITIONS_LINK = ("accessibility id", "Terms and conditions")
    PRIVACY_POLICY_LINK = ("accessibility id", "Privacy Policy")
    
    # App Logo/Title (text elements with content-desc)
    APP_LOGO = ("accessibility id", "Connect")
    APP_SUBTITLE = ("accessibility id", "Persona")
    APP_TAGLINE = ("accessibility id", "Connections Made Easy")
