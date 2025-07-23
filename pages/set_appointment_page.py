# pages/set_appointment_page.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SetAppointmentPage:
    def __init__(self, driver):
        self.driver = driver

    def click_continue_to_search_for_doctor(self):
        buttons = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, "//button[@data-hook='Button' and contains(text(), 'המשך')]"))
        )
        buttons[1].click()  # Click the first one only

    def click_service_by_name(self, service_name):
        service_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((
                By.XPATH,
                f"//button[@data-hook='Button' and .//div[text()='{service_name}']]"
            ))
        )
        service_button.click()