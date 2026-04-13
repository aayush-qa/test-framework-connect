import pytest

@pytest.mark.smoke
def test_open_app(driver):
    assert driver.session_id is not None
    assert driver.current_package is not None
