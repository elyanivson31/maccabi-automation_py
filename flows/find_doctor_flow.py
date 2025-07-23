# flows/find_doctor_flow.py

from pages.find_doctor_page import FindDoctorPage

class FindDoctorFlow:
    def __init__(self, driver):
        self.driver = driver
        self.page = FindDoctorPage(driver)

    def search_for_doctor(self, doctor_name, city_name=None):
        self.page.enter_doctor_name(doctor_name)
        if city_name:
            self.page.enter_city(city_name)
        self.page.click_search()

    def select_set_appointment(self):
        self.page.click_set_appointment()
