"""
Sign In Page Locators
Centralized locator definitions for Sign In page elements

Locator Strategy:
- accessibility id: Used for elements with content-desc attribute
- id: Used for resource-id (full path like "com.package:id/element")
- -android uiautomator: Used for UIAutomator2 selector queries (specific and reliable)
- xpath: Used as fallback only when other strategies fail
- Coordinates: Used for system-level UI elements (e.g., back button) when no locator available
"""


class SignInLocators:
    """Locators for Sign In page"""

    # Back Button on Sign In page (use UiAutomator or coordinates as fallback)
    BACK_BUTTON = ("xpath", "//android.widget.ImageButton[@content-desc='Navigate up']")
    BACK_BUTTON_ALT = ("-android uiautomator", 'new UiSelector().className("android.widget.ImageButton").instance(0)')

    # Coordinates for the back button tap when no separate element exists
    BACK_BUTTON_COORDINATE = (60, 208)
    
    # Sign In Elements (actual locators from Appium Inspector)
    EMAIL_FIELD = ("-android uiautomator", 'new UiSelector().className("android.widget.EditText").instance(0)')
    PASSWORD_FIELD = ("-android uiautomator", 'new UiSelector().className("android.widget.EditText").instance(1)')
    SIGN_IN_SUBMIT_BUTTON = ("accessibility id", "Sign in")
    
    # Links and Text (use accessibility_id instead of id for content-desc based elements)
    FORGOT_PASSWORD_LINK = ("accessibility id", "Trouble Signing in?")
    CREATE_ACCOUNT_LINK = ("accessibility id", "Create account")

