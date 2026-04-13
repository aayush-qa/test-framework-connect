import os
from pathlib import Path

import yaml
from appium import webdriver

try:
    from appium.options.android import UiAutomator2Options
except ImportError:
    UiAutomator2Options = None

try:
    from appium.options.ios import XCUITestOptions
except ImportError:
    XCUITestOptions = None


ROOT_DIR = Path(__file__).resolve().parents[1]
CONFIG_FILE = ROOT_DIR / "config" / "config.yaml"


class DriverManager:
    def __init__(self, caps: dict):
        self.caps = self._normalize_caps(caps or {})
        self.driver = None
        self.host = "127.0.0.1"
        self.port = 4723
        self._load_config()

    def _normalize_caps(self, caps: dict) -> dict:
        normalized = caps.copy()

        if "platform" in normalized and "platformName" not in normalized:
            normalized["platformName"] = normalized.pop("platform")

        if "automation_name" in normalized and "automationName" not in normalized:
            normalized["automationName"] = normalized.pop("automation_name")

        if "device_name" in normalized and "deviceName" not in normalized:
            normalized["deviceName"] = normalized.pop("device_name")

        if "app_path" in normalized and not normalized.get("app") and not normalized.get("appium:app"):
            app_path = Path(normalized.pop("app_path"))
            if not app_path.is_absolute():
                app_path = (ROOT_DIR / app_path).resolve()
            normalized["appium:app"] = str(app_path)

        if "platformName" in normalized and isinstance(normalized["platformName"], str):
            platform_name = normalized["platformName"].strip()
            normalized["platformName"] = (
                "iOS" if platform_name.lower() == "ios"
                else "Android" if platform_name.lower() == "android"
                else platform_name
            )

        return normalized

    def _load_config(self):
        if CONFIG_FILE.exists():
            with open(CONFIG_FILE, encoding="utf-8") as f:
                config = yaml.safe_load(f)
            appium_cfg = config.get("appium", {}) if isinstance(config, dict) else {}
            self.host = appium_cfg.get("host", self.host)
            self.port = appium_cfg.get("port", self.port)

    def _build_options(self):
        platform = self.caps.get("platformName", "").lower()

        if platform == "android" and UiAutomator2Options is not None:
            options = UiAutomator2Options()
        elif platform == "ios" and XCUITestOptions is not None:
            options = XCUITestOptions()
        else:
            from appium.options.common import AppiumOptions
            options = AppiumOptions()

        options.load_capabilities(self.caps)
        return options

    def __enter__(self):
        appium_url = f"http://{self.host}:{self.port}"
        options = self._build_options()
        self.driver = webdriver.Remote(command_executor=appium_url, options=options)
        return self.driver

    def __exit__(self, exc_type, exc_value, traceback):
        if self.driver:
            try:
                self.driver.quit()
            except Exception:
                pass
