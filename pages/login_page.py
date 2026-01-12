import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def click_password_login_link(self):
        """
        Click the 'כניסה עם סיסמה' tab to show the password login form.
        """
        wait = WebDriverWait(self.driver, 30)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='#IdentifyWithPassword']")))
        self.driver.execute_script("document.querySelector(\"a[href='#IdentifyWithPassword']\").click();")
        wait.until(EC.visibility_of_element_located((By.ID, "IdentifyWithPassword")))



    def enter_username(self, username):
        self.driver.find_element(By.ID, "idNumber2").send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.ID, "password").send_keys(password)

    def click_login(self):
        wait = WebDriverWait(self.driver, 30)
        login_button = wait.until(EC.element_to_be_clickable((By.ID, "enterWithPasswordBtn")))
        # Scroll element into view to ensure it's not covered
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", login_button)
        time.sleep(0.5)  # Brief pause after scroll
        try:
            login_button.click()
        except Exception as e:
            # Fallback to JavaScript click if regular click fails
            print(f"Regular click failed, using JavaScript click: {e}")
            self.driver.execute_script("arguments[0].click();", login_button)

    def enter_id_number(self, id_number):
        self.driver.find_element(By.ID, "idNumber").send_keys(id_number)

    def click_next_to_choose_login_method(self):
        wait = WebDriverWait(self.driver, 30)
        button = wait.until(EC.element_to_be_clickable((By.ID, "chooseTypeBtn")))
        # Scroll element into view to ensure visibility (important for headless mode)
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", button)
        time.sleep(0.3)  # Brief pause after scroll
        try:
            button.click()
        except Exception as e:
            # Fallback to JavaScript click if regular click fails
            print(f"Regular click failed, using JavaScript click: {e}")
            self.driver.execute_script("arguments[0].click();", button)

    def click_login_with_password_type(self):
        wait = WebDriverWait(self.driver, 30)
        link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "כניסה עם סיסמה")))
        # Scroll element into view to ensure visibility (important for headless mode)
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", link)
        time.sleep(0.3)  # Brief pause after scroll
        try:
            link.click()
        except Exception as e:
            # Fallback to JavaScript click if regular click fails
            print(f"Regular click failed, using JavaScript click: {e}")
            self.driver.execute_script("arguments[0].click();", link)