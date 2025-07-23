# pages/find_doctor_page.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class FindDoctorPage:
    def __init__(self, driver):
        self.driver = driver

    def enter_doctor_name(self, name):
        input_box = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "DocName"))
        )
        input_box.clear()
        input_box.send_keys(name)

    def click_search(self):
        search_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "SearchButton"))
        )
        search_btn.click()
