"""
test_data/loader.py
-------------------
Single entry point for all test data across the framework.
Usage:
    from test_data.loader import login_data, signup_data, users, products

Note:
    Platform-specific Appium capabilities are now loaded from config/capabilities.json
    and managed by utils/driver_manager.py. Use that for all capability configuration.
"""

import json
import os

_BASE = os.path.dirname(__file__)


def _load(feature: str, filename: str) -> dict:
    """Read a JSON file from test_data/<feature>/<filename>."""
    filepath = os.path.join(_BASE, feature, filename)
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Test data file not found: {filepath}")
    with open(filepath, encoding="utf-8") as f:
        return json.load(f)


# ── Auth ────────────────────────────────────────────────────────────────────

def login_data() -> dict:
    """Return all login test data (valid, invalid, locked)."""
    return _load("auth", "login.json")


def signup_data() -> dict:
    """Return all signup test data (new user, duplicate, invalid)."""
    return _load("auth", "signup.json")


# ── Personas ────────────────────────────────────────────────────────────────

def users() -> dict:
    """Return all user personas (standard, locked, error, admin)."""
    return _load("personas", "users.json")


def get_user(persona: str) -> dict:
    """Return a single user persona by key. e.g. get_user('standard_user')"""
    all_users = users()
    if persona not in all_users:
        raise KeyError(f"Unknown persona '{persona}'. Available: {list(all_users.keys())}")
    return all_users[persona]


# ── Products ────────────────────────────────────────────────────────────────

def products() -> dict:
    """Return full product catalog and bundles."""
    return _load("products", "products.json")


def get_bundle(bundle_name: str) -> list:
    """Return product IDs for a named bundle."""
    data = products()
    if bundle_name not in data.get("bundles", {}):
        raise KeyError(f"Unknown bundle '{bundle_name}'.")
    return data["bundles"][bundle_name]


def cart_data() -> dict:
    """Return cart configurations per persona bundle."""
    return _load("products", "cart.json")


# ── Platform ────────────────────────────────────────────────────────────────
# NOTE: Platform-specific capabilities are now loaded from config/capabilities.json
# This function is deprecated. Use DriverManager with config/capabilities.json instead.
