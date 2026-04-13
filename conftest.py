"""
conftest.py — root pytest fixtures
"""
import json
from pathlib import Path
import pytest
from utils.driver_manager import DriverManager


def _load_capabilities(config_file: str = "config/capabilities.json") -> dict:
    """Load Appium capabilities from JSON config file."""
    config_path = Path(__file__).parent / config_file
    if not config_path.exists():
        raise FileNotFoundError(f"Capabilities file not found: {config_path}")
    with open(config_path, "r", encoding="utf-8") as f:
        return json.load(f)


@pytest.fixture(scope="function")
def driver():
    caps = _load_capabilities()
    with DriverManager(caps) as d:
        yield d
