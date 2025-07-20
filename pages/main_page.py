import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MainPage:
    def __init__(self, driver):
        self.driver = driver

    def click_new_appointment_button(self):
            """
            Clicks the 'זימון תור חדש' (New Appointment) button on the main/home page.
            """
            wait = WebDriverWait(self.driver, 30)
            new_appointment_btn = wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//button[.//h2[text()='זימון תור חדש']]")
            ))
            new_appointment_btn.click()

    def switch_patient(self, patient_name: str):
        # Click current patient name dropdown
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-hook='DropDown']"))).click()

        # Wait and click the specific patient name
        self.wait.until(EC.element_to_be_clickable((By.XPATH, f"//span[text()='{patient_name}']"))).click()