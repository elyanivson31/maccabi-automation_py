from flows.login_flow import LoginFlow
from flows.main_flow import MainFlow


class WebFlow:
    def __init__(self, driver):
        self.driver = driver
        self._login_flow = None
        self._main_flow = None

    def login_flow(self):
        if not self._login_flow:
            self._login_flow = LoginFlow(self.driver)
        return self._login_flow

    def main_flow(self):
        if not self._main_flow:
            self._main_flow = MainFlow(self.driver)
        return self._main_flow
