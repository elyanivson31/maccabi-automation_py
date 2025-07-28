from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ConfirmAppointmentPage:
    def __init__(self, driver):
        self.driver = driver

    def get_appointment_date_text(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "availableForDateTitle"))
        )
        return element.text
