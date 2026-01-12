import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException


class MainPage:
    def __init__(self, driver):
        self.driver = driver

    def click_new_appointment_button(self):
            """
            Clicks the 'זימון תור חדש' (New Appointment) button on the main/home page.
            Includes scroll into view and JavaScript click fallback for headless mode reliability.
            """
            wait = WebDriverWait(self.driver, 30)
            new_appointment_btn = wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//button[.//h2[text()='זימון תור חדש']]")
            ))
            # Scroll element into view to ensure it's visible (important for headless mode)
            self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", new_appointment_btn)
            time.sleep(0.5)  # Brief pause after scroll
            try:
                new_appointment_btn.click()
            except Exception as e:
                # Fallback to JavaScript click if regular click fails (common in headless mode)
                print(f"Regular click failed, using JavaScript click: {e}")
                self.driver.execute_script("arguments[0].click();", new_appointment_btn)

    def switch_to_patient(self, patient_name):
        wait = WebDriverWait(self.driver, 20)

        # Retry once in case the first element gets stale
        for attempt in range(2):
            try:
                # Always fetch the element fresh before clicking
                dropdown_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[aria-haspopup='true']")))
                dropdown_button.click()
                break
            except StaleElementReferenceException:
                if attempt == 1:
                    raise

        # Wait until patient list appears
        wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".src-components-ImpersonationButton-ImpersonationButton__name___jwDEs")))

        # Find matching patient and click
        patient_buttons = self.driver.find_elements(By.CSS_SELECTOR, ".src-components-ImpersonationButton-ImpersonationButton__name___jwDEs")
        for button in patient_buttons:
            try:
                if button.text.strip() == patient_name:
                    button.click()
                    return
            except StaleElementReferenceException:
                pass  # Can retry here if needed

        raise Exception(f"Patient '{patient_name}' not found in dropdown.")