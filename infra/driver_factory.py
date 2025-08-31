from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def create_chrome_driver():
    """
    Create and return a Chrome WebDriver instance.
    Uses webdriver_manager to automatically handle the ChromeDriver installation.
    """
    # Initialize Chrome options
    options = Options()
    # (Optional) Run Chrome in headless mode for tests without UI:
    # options.add_argument("--headless")
    # Start Chrome maximized to ensure elements are visible

    options.add_argument("--headless=new")  # Use `new` for recent Chromium versions
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")

    # Optional: suppress logging
    options.add_argument("--log-level=3")
    options.add_argument('--remote-debugging-port=9222')  # avoids Runtime.evaluate error

    # your test logic here

    # Additional Chrome options (if needed) can be added, for example:
    # options.add_argument("--disable-gpu")
    # options.add_argument("--no-sandbox")
    
    # Use ChromeDriverManager to automatically download & use the matching ChromeDriver
    service = Service(ChromeDriverManager().install())
    # Create the Chrome WebDriver instance with the specified service and options
    driver = webdriver.Chrome(service=service, options=options)
    return driver
