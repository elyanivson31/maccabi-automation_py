from pages.choose_appointment_type_page import ChooseAppointmentTypePage

class ChooseAppointmentTypeFlow:
    def __init__(self, driver):
        self.page = ChooseAppointmentTypePage(driver)

    def select_appointment_type(self, type_text):
        self.page.click_appointment_type(type_text)
