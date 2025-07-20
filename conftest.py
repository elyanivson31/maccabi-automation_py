import pytest
from infra.driver_factory import create_chrome_driver

@pytest.fixture(scope="function")
def driver():
    """
    Pytest fixture to initialize and teardown a Chrome WebDriver for each test.
    Returns a Selenium WebDriver instance for Chrome.
    """
    # Setup: create the Chrome WebDriver using our driver factory
    driver = create_chrome_driver()
    # Implicit wait (e.g., 10 seconds) for elements to appear before interactions
    driver.implicitly_wait(10)
    yield driver
    # Teardown: quit the browser after test completes
    driver.quit()