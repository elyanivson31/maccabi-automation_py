from pages.main_page import MainPage

class MainFlow:
    def __init__(self, driver):
        self.driver = driver
        self.main_page = MainPage(driver)

    def start_new_appointment(self):
        self.main_page.click_new_appointment_button()

    
    def switch_patient(self, patient_name: str):
        self.main_page.switch_patient(patient_name)