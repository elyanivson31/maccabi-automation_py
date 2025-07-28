from asyncio import timeout
from httpcore import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException


class ConfirmAppointmentPage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.timeout = timeout

    def get_appointment_date_text(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "availableForDateTitle"))
        )
        return element.text
    
    def get_time_slot_buttons(self):
        """Wait for and return all visible time slot buttons inside the container."""
        try:
            container = WebDriverWait(self.driver, self.timeout).until(
                EC.presence_of_element_located((By.ID, "btnsConatiner"))
            )

            # Wait until at least one button appears in the container
            WebDriverWait(self.driver, self.timeout).until(
                lambda d: container.find_elements(By.CSS_SELECTOR, "button[data-hook^='Button__RoundButtonPicker__']")
            )

            # Return visible buttons
            return [
                btn for btn in container.find_elements(By.CSS_SELECTOR, "button[data-hook^='Button__RoundButtonPicker__']")
                if btn.is_displayed()
            ]
        except TimeoutException:
            print("❌ No time slot buttons found.")
            return []

    def click_first_available_time_slot(self):
        """Click the first available time slot."""
        buttons = self.get_time_slot_buttons()

        if not buttons:
            raise Exception("❌ No time slots available.")

        all_times = [btn.text.strip() for btn in buttons if btn.text.strip()]
        print(f"🕒 Available time slots: {all_times}")

        first_button = buttons[0]

        try:
            WebDriverWait(self.driver, self.timeout).until(
                EC.element_to_be_clickable(first_button)
            )
            first_button.click()
            print(f"✅ Clicked on time slot: {first_button.text.strip()}")
        except ElementClickInterceptedException:
            print("⚠️ Element not clickable directly. Falling back to JS click.")
            self.driver.execute_script("arguments[0].click();", first_button)
    
    
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
