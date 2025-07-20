import time
from selenium.webdriver.common.by import By

class HomePage:
    """
    Page Object for the Maccabi homepage.
    Provides methods to interact with elements on the home page (e.g., login link).
    """
    URL = "https://www.maccabi4u.co.il/"

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        """Open the Maccabi homepage in the browser."""
        self.driver.get(HomePage.URL)

    # def navigate_to_login(self):
    #     """
    #     Click the 'Maccabi Online' login link on the homepage.
    #     This will navigate the browser to the Maccabi Online login page.
    #     """
    #     # Find the login link by partial href (contains 'online.maccabi4u') and click it
    #     login_link = self.driver.find_element(By.CSS_SELECTOR, "a[href*='online.maccabi4u']")
    #     login_link.click()
    
    def navigate_to_login(self):
        """
        Clicks the 'Maccabi Online' login link and switches to the new tab if opened.
        """
        original_tabs = self.driver.window_handles
        self.driver.find_element(By.CSS_SELECTOR, "a[href*='online.maccabi4u.co.il']").click()

        # Wait for new tab if it opens
        time.sleep(2)  # short pause to let new tab open

        new_tabs = self.driver.window_handles
        if len(new_tabs) > len(original_tabs):
            self.driver.switch_to.window(new_tabs[-1])  # switch to new tab