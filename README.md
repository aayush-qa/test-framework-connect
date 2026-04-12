# MyApp — Appium Automation Framework

Python · Appium · PyTest · POM · Allure · Self-Healing

## Quick start

```bash
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
PLATFORM=android pytest -m smoke --alluredir=reports/allure-results
allure serve reports/allure-results
```

## Structure

- **`ai_locators/`** - Self-healing locator fallback engine
  - `__init__.py`

- **`api/`** - API client layer for authentication and user flows
  - `__init__.py`

- **`app/`** - Application binaries
  - `android/` - Android APK files
  - `ios/` - iOS IPA files

- **`config/`** - Configuration files
  - `capabilities.json` - Base Appium capabilities
  - `config.yaml` - Framework settings (timeouts, logging, etc.)

- **`mobile_api_ai_framework/`** - Core framework package
  - `__init__.py`

- **`pages/`** - Page Object Model classes
  - `__init__.py`

- **`reports/`** - Test artifacts and results
  - `allure-results/` - Allure report data
  - `logs/` - Framework logs
  - `screenshots/` - Test failure screenshots

- **`test_data/`** - Test data organized by domain
  - `__init__.py`
  - `loader.py` - Data loading utilities
  - `README.md` - Data documentation
  - `auth/` - Authentication test data
    - `login.json`
    - `signup.json`
  - `personas/` - User personas
    - `users.json`
  - `platform/` - Platform-specific configurations
    - `android.json`
    - `ios.json`
  - `products/` - Product and cart test data
    - `cart.json`
    - `products.json`

- **`tests/`** - PyTest test suites
  - `__init__.py`

- **`utils/`** - Utility modules
  - `__init__.py`

- **`visual/`** - OpenCV visual regression testing
  - `__init__.py`
