# flows/find_doctor_flow.py

from pages.find_doctor_page import FindDoctorPage

class FindDoctorFlow:
    def __init__(self, driver):
        self.driver = driver
        self.page = FindDoctorPage(driver)

    def search_for_doctor(self, name):
        self.page.enter_doctor_name(name)
        self.page.click_search()
