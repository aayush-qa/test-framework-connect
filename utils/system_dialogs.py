"""System dialog helpers for mobile runtime permission dialogs."""

from appium.webdriver.webdriver import WebDriver


class SystemDialogHandler:
    """Helper to handle Android runtime permission dialogs.
    
    Handles both system-level permission dialogs (Android) and app-level permission prompts.
    Uses multiple locator strategies in order of reliability:
    1. resource-id (most reliable for system dialogs)
    2. content-desc/accessibility id
    3. Text-based XPath (fallback)
    """

    # Android system permission dialog locators (in priority order)
    PERMISSION_ALLOW_BUTTON = [
        ("id", "com.android.permissioncontroller:id/permission_allow_button"),
        ("accessibility id", "Allow"),
        ("xpath", "//android.widget.Button[@text='Allow' or @text='ALLOW']"),
    ]
    
    PERMISSION_DENY_BUTTON = [
        ("id", "com.android.permissioncontroller:id/permission_deny_button"),
        ("accessibility id", "Don't allow"),
        ("xpath", "//android.widget.Button[@text=\"Don't allow\" or @text='Deny']"),
    ]

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def _find_element_by_locators(self, locators: list) -> object:
        """Try to find element using multiple locator strategies."""
        for locator in locators:
            try:
                return self.driver.find_element(*locator)
            except Exception:
                continue
        return None

    def is_permission_dialog_displayed(self) -> bool:
        """Return True when a system permission dialog is visible."""
        allow_btn = self._find_element_by_locators(self.PERMISSION_ALLOW_BUTTON)
        deny_btn = self._find_element_by_locators(self.PERMISSION_DENY_BUTTON)
        return bool(allow_btn or deny_btn)

    def click_allow(self) -> None:
        """Click the Allow button on a system permission dialog."""
        allow_button = self._find_element_by_locators(self.PERMISSION_ALLOW_BUTTON)
        if allow_button:
            allow_button.click()

    def click_deny(self) -> None:
        """Click the Deny button on a system permission dialog."""
        deny_button = self._find_element_by_locators(self.PERMISSION_DENY_BUTTON)
        if deny_button:
            deny_button.click()

    def handle_permission_dialog(self, accept: bool = True) -> None:
        """Handle a runtime permission dialog by accepting or denying it.
        
        Args:
            accept: True to click Allow, False to click Deny
        """
        if self.is_permission_dialog_displayed():
            if accept:
                self.click_allow()
            else:
                self.click_deny()
