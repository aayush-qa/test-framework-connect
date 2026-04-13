import json
from pathlib import Path

import pytest
import yaml
from appium import webdriver
from appium.options.android import UiAutomator2Options


ROOT_DIR = Path(__file__).resolve().parents[1]
CONFIG_FILE = ROOT_DIR / "config" / "config.yaml"
CAPS_FILE = ROOT_DIR / "config" / "capabilities.json"


def load_config():
    with open(CONFIG_FILE, encoding="utf-8") as f:
        return yaml.safe_load(f)


def load_caps():
    with open(CAPS_FILE, encoding="utf-8") as f:
        caps = json.load(f)

    app_path = Path(caps.get("appium:app", ""))
    if not app_path.is_absolute():
        caps["appium:app"] = str((ROOT_DIR / app_path).resolve())

    return caps


@pytest.mark.smoke
def test_open_app():
    config = load_config()
    caps = load_caps()
    options = UiAutomator2Options()
    options.load_capabilities(caps)
    appium_url = f"http://{config['appium']['host']}:{config['appium']['port']}"

    driver = webdriver.Remote(command_executor=appium_url, options=options)
    try:
        assert driver.session_id is not None
        assert driver.current_package is not None
    finally:
        driver.quit()
