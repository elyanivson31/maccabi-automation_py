from flows.find_doctor_flow import FindDoctorFlow
from flows.login_flow import LoginFlow
from flows.main_flow import MainFlow
from flows.set_appointment_flow import SetAppointmentFlow
from flows.choose_appointment_type_flow import ChooseAppointmentTypeFlow
from flows.confirm_appointment_flow import ConfirmAppointmentFlow
class WebFlow:
    def __init__(self, driver):
        self.driver = driver
        self._login_flow = None
        self._main_flow = None
        self._set_appimtment_flow = None
        self._find_doctor_flow  = None
        self._choose_appointment_type_flow = None
        self._confirm_appointment_flow = None

    def login_flow(self):
        if not self._login_flow:
            self._login_flow = LoginFlow(self.driver)
        return self._login_flow

    def main_flow(self):
        if not self._main_flow:
            self._main_flow = MainFlow(self.driver)
        return self._main_flow

    def set_appointment_flow(self):
        if not self._set_appimtment_flow:
            self._set_appimtment_flow = SetAppointmentFlow(self.driver)
        return self._set_appimtment_flow
    
    def find_doctor_flow(self):
        if not self._find_doctor_flow:
            self._find_doctor_flow = FindDoctorFlow(self.driver)
        return self._find_doctor_flow

    def choose_appointment_type_flow(self):
        if not self._choose_appointment_type_flow:
            self._choose_appointment_type_flow = ChooseAppointmentTypeFlow(self.driver)
        return self._choose_appointment_type_flow


    def confirm_appointment_flow(self):
        if not self._confirm_appointment_flow:
            self._confirm_appointment_flow = ConfirmAppointmentFlow(self.driver)
        return self._confirm_appointment_flow
