from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ChooseAppointmentTypePage:
    def __init__(self, driver):
        self.driver = driver

    def click_appointment_type(self, type_text):
        locator = (By.XPATH, f"//button[.//div[text()='{type_text}']]")
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(locator)).click()

    def click_continue(self):
            continue_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='המשך']"))
        )
            continue_btn.click()

    def select_under_18_if_present(self):
        try:
            under_18_btn = WebDriverWait(self.driver, 3).until(
                EC.element_to_be_clickable((By.XPATH, "//button[.//div[text()='מתחת לגיל 18']]"))
            )
            under_18_btn.click()
        except:
            # No under-18 prompt, so just proceed silently
            pass


    def click_continue_for_agree_to_bring_your_personal_health_card(self):
            continue_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[.//div[text()='להמשך']]"))
        )
            continue_btn.click()