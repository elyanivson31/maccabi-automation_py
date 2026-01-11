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
        self.driver.find_element(By.ID, "enterWithPasswordBtn").click()

    def enter_id_number(self, id_number):
        self.driver.find_element(By.ID, "idNumber").send_keys(id_number)

    def click_next_to_choose_login_method(self):
        self.driver.find_element(By.ID, "chooseTypeBtn").click()

    def click_login_with_password_type(self):
        self.driver.find_element(By.LINK_TEXT, "כניסה עם סיסמה").click()