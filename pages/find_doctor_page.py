# pages/find_doctor_page.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class FindDoctorPage:
    def __init__(self, driver):
        self.driver = driver

    def enter_doctor_name(self, name):
        input_box = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "DocName"))
        )
        input_box.clear()
        input_box.send_keys(name)


    def enter_city(self, city_name):
        city_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@aria-label='בחירת ישוב']"))
        )
        city_input.clear()
        city_input.send_keys(city_name)
        city_input.send_keys(Keys.ENTER)

    def click_search(self):
        search_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "SearchButton"))
        )
        search_btn.click()

    def click_set_appointment(self):
        set_appointment_link = WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[text()='זימון תור']"))
        )
        set_appointment_link.click()
