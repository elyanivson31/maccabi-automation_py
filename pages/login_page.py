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
        self.driver.find_element(By.ID, "identifyWithPasswordCitizenId").send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.ID, "password").send_keys(password)

    def click_login(self):
        self.driver.find_element(By.CSS_SELECTOR, "button.submit.validatePassword").click()
