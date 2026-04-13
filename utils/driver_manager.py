import os
from pathlib import Path

import yaml
from appium import webdriver

try:
    from appium.options.android import UiAutomator2Options
except ImportError:
    UiAutomator2Options = None


ROOT_DIR = Path(__file__).resolve().parents[1]
CONFIG_FILE = ROOT_DIR / "config" / "config.yaml"


class DriverManager:
    def __init__(self, caps: dict):
        self.caps = caps
        self.driver = None
        self.host = "127.0.0.1"
        self.port = 4723
        self._load_config()

    def _load_config(self):
        if CONFIG_FILE.exists():
            with open(CONFIG_FILE, encoding="utf-8") as f:
                config = yaml.safe_load(f)
            appium_cfg = config.get("appium", {}) if isinstance(config, dict) else {}
            self.host = appium_cfg.get("host", self.host)
            self.port = appium_cfg.get("port", self.port)

    def _build_options(self):
        if UiAutomator2Options is not None and self.caps.get("platformName", "").lower() == "android":
            options = UiAutomator2Options()
            options.load_capabilities(self.caps)
            return options

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
