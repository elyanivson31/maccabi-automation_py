from pages.choose_appointment_type_page import ChooseAppointmentTypePage

class ChooseAppointmentTypeFlow:
    def __init__(self, driver):
        self.page = ChooseAppointmentTypePage(driver)

    def select_appointment_type(self, type_text):
        self.page.click_appointment_type(type_text)

    def select_appointment_type_and_continue(self, type_name):
        self.page.click_appointment_type(type_name)
        self.page.click_continue()

    def select_under_18_if_present(self):
        self.page.select_under_18_if_present()
        self.page.click_continue()

    
    def agree_to_come_with_personal_health_card(self):
        self.page.click_continue_for_agree_to_bring_your_personal_health_card()