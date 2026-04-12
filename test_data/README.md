# test_data/

Centralised test data layer for the MyApp Appium automation framework.

Both Android and iOS platforms are configured.

## Structure

```
test_data/
├── auth/
│   ├── login.json       # Valid, invalid, locked login credentials
│   └── signup.json      # New user, duplicate, invalid email payloads
├── personas/
│   └── users.json       # User personas (standard, locked, error, admin)
├── products/
│   ├── products.json    # Product catalog and bundles
│   └── cart.json        # Cart configs per persona
├── platform/
│   ├── android.json     # Android caps and locator overrides
│   └── ios.json         # iOS caps and locator overrides
├── __init__.py
├── loader.py            # Single import point for all data
└── README.md
```

## Usage

```python
from test_data.loader import login_data, signup_data, users, get_user, products, platform_data

# Login test
data = login_data()["valid"]["standard_user"]

# Locked user
locked = login_data()["locked"]

# User persona
user = get_user("standard_user")

# Platform caps (reads PLATFORM env var, defaults to android)
caps = platform_data()           # uses env var
caps = platform_data("ios")      # explicit
```

## Adding new test data

1. Add a new key to the relevant JSON file.
2. No code changes needed — `loader.py` reads the file dynamically.
3. For a new feature, create a new subfolder and add a `loader.py` function.

## Environment variable

Set `PLATFORM=ios` or `PLATFORM=android` before running tests to control
which platform capabilities are loaded.

```bash
PLATFORM=ios pytest -m regression
PLATFORM=android pytest -m smoke
```
