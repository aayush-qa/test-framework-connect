"""Base page object with shared helpers for all app pages."""

from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from utils.system_dialogs import SystemDialogHandler


class BasePage:
    """Common page functionality shared by all page objects.
    
    Provides:
    - Explicit waits for element presence, visibility, and clickability
    - System permission dialog handling
    - Element interaction helpers with built-in error handling
    """

    DEFAULT_TIMEOUT = 10  # seconds

    def __init__(self, driver: WebDriver, timeout: int = DEFAULT_TIMEOUT):
        self.driver = driver
        self.dialog_handler = SystemDialogHandler(driver)
        self.wait = WebDriverWait(driver, timeout)
        self.timeout = timeout

    def handle_system_permission_dialog(self, accept: bool = True) -> None:
        """Handle any runtime system permission dialog if it appears."""
        self.dialog_handler.handle_permission_dialog(accept=accept)

    def wait_for_element(self, locator, timeout: int = None) -> object:
        """Wait for element to be present in DOM (not necessarily visible).
        
        Args:
            locator: Tuple of (By.STRATEGY, "locator_value")
            timeout: Optional custom timeout in seconds
            
        Returns:
            WebElement when found
            
        Raises:
            TimeoutException: If element not found within timeout
        """
        wait = WebDriverWait(self.driver, timeout or self.timeout)
        return wait.until(EC.presence_of_element_located(locator))

    def wait_for_element_visible(self, locator, timeout: int = None) -> object:
        """Wait for element to be visible on screen.
        
        Args:
            locator: Tuple of (By.STRATEGY, "locator_value")
            timeout: Optional custom timeout in seconds
            
        Returns:
            WebElement when visible
            
        Raises:
            TimeoutException: If element not visible within timeout
        """
        wait = WebDriverWait(self.driver, timeout or self.timeout)
        return wait.until(EC.visibility_of_element_located(locator))

    def wait_for_element_clickable(self, locator, timeout: int = None) -> object:
        """Wait for element to be present and clickable.
        
        Args:
            locator: Tuple of (By.STRATEGY, "locator_value")
            timeout: Optional custom timeout in seconds
            
        Returns:
            WebElement when clickable
            
        Raises:
            TimeoutException: If element not clickable within timeout
        """
        wait = WebDriverWait(self.driver, timeout or self.timeout)
        return wait.until(EC.element_to_be_clickable(locator))

    def find_element(self, *locator, visible: bool = False):
        """Find a single element using a locator tuple with implicit wait.
        
        Args:
            *locator: Tuple of (By.STRATEGY, "locator_value")
            visible: If True, wait for element visibility; else just presence
            
        Returns:
            WebElement
        """
        if visible:
            return self.wait_for_element_visible(locator)
        return self.wait_for_element(locator)

    def find_elements(self, *locator):
        """Find multiple elements using a locator tuple.
        
        Args:
            *locator: Tuple of (By.STRATEGY, "locator_value")
            
        Returns:
            List of WebElements (may be empty if none found)
        """
        try:
            self.wait_for_element(locator)
            return self.driver.find_elements(*locator)
        except TimeoutException:
            return []

    def click_element(self, locator) -> None:
        """Click an element using a locator tuple with wait for clickability.
        
        Args:
            locator: Tuple of (By.STRATEGY, "locator_value")
        """
        element = self.wait_for_element_clickable(locator)
        element.click()

    def is_element_displayed(self, locator, timeout: int = 5) -> bool:
        """Return True when the element is displayed.
        
        Args:
            locator: Tuple of (By.STRATEGY, "locator_value")
            timeout: Custom timeout in seconds (default 5)
            
        Returns:
            True if element is visible, False otherwise
        """
        try:
            self.wait_for_element_visible(locator, timeout=timeout)
            return True
        except TimeoutException:
            return False

    def is_element_enabled(self, locator) -> bool:
        """Return True when the element is enabled.
        
        Args:
            locator: Tuple of (By.STRATEGY, "locator_value")
            
        Returns:
            True if element is enabled, False otherwise
        """
        try:
            element = self.wait_for_element(locator)
            return element.is_enabled()
        except TimeoutException:
            return False

    def is_element_present(self, locator, timeout: int = 5) -> bool:
        """Return True when element is present in DOM (may not be visible).
        
        Args:
            locator: Tuple of (By.STRATEGY, "locator_value")
            timeout: Custom timeout in seconds (default 5)
            
        Returns:
            True if element exists, False otherwise
        """
        try:
            self.wait_for_element(locator, timeout=timeout)
            return True
        except TimeoutException:
            return False

    def send_keys_to_element(self, locator, text: str) -> None:
        """Send keys to an element with wait for visibility.
        
        Args:
            locator: Tuple of (By.STRATEGY, "locator_value")
            text: Text to send
        """
        element = self.wait_for_element_visible(locator)
        element.clear()
        element.send_keys(text)

    def tap_coordinate(self, x: int, y: int) -> None:
        """Tap on a screen coordinate using Appium mobile gesture.
        
        Used for system-level UI elements (e.g., device back button) where
        locators are unavailable or unreliable.
        
        Args:
            x: X coordinate
            y: Y coordinate
        """
        self.driver.execute_script("mobile: tap", {"x": x, "y": y})
