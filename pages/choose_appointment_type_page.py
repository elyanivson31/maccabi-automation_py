from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ChooseAppointmentTypePage:
    def __init__(self, driver):
        self.driver = driver

    def click_appointment_type(self, type_text):
        locator = (By.XPATH, f"//button[.//div[text()='{type_text}']]")
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(locator)).click()
