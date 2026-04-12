"""
conftest.py — root pytest fixtures
"""
import os
import pytest
from test_data.loader import platform_data
from utils.driver_manager import DriverManager


@pytest.fixture(scope="function")
def driver():
    platform = os.getenv("PLATFORM", "android")
    caps = platform_data(platform)
    with DriverManager(caps) as d:
        yield d
