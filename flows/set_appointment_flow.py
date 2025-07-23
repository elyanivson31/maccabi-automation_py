# flows/set_appointment_flow.py

from pages.set_appointment_page import SetAppointmentPage

class SetAppointmentFlow:
    def __init__(self, driver):
        self.driver = driver
        self.page = SetAppointmentPage(driver)

    def continue_to_doctor_search(self):
        self.page.click_continue_to_search_for_doctor()

    def choose_service(self, service_name):
        self.page.click_service_by_name(service_name)