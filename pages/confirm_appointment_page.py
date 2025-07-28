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

    def get_time_slot_buttons(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#btnsConatiner button[data-hook^='Button__RoundButtonPicker__']"))
        )

    def click_time_slot(self, preference="latest"):
        buttons = self.get_time_slot_buttons()

        if not buttons:
            raise Exception("No time slots available")

        if preference == "earliest":
            buttons[0].click()
        elif preference == "latest":
            buttons[-1].click()
        else:
            raise ValueError("Invalid preference. Use 'earliest' or 'latest'.")
        

    def click_confirm_appointment_button(self):
        confirm_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='זימון התור']"))
        )
        confirm_btn.click()


    def click_confirm_button(self):
        confirm_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[.//div[text()='אישור']]"))
        )
        confirm_button.click()

    def click_continue_button(self):
        continue_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='המשך']"))
        )
        continue_button.click()

    def is_success_message_displayed(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//h1[text()='תורך נקבע בהצלחה']"))
            )
            return True
        except:
            return False
