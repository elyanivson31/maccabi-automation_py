from pages.confirm_appointment_page import ConfirmAppointmentPage
from datetime import datetime

class ConfirmAppointmentFlow:
    def __init__(self, driver):
        self.driver = driver
        self.page = ConfirmAppointmentPage(driver)

    def is_displayed_date_equal_to_threshold(self, threshold_date: datetime) -> bool:
        text = self.page.get_appointment_date_text()
        # Extract date in format DD/MM/YY using regex
        import re
        match = re.search(r"\d{2}/\d{2}/\d{2}", text)
        if not match:
            return False

        displayed_str = match.group()  # e.g., "29/07/25"
        try:
            displayed_date = datetime.strptime(displayed_str, "%d/%m/%y")
            return displayed_date.date() == threshold_date.date()
        except ValueError:
            return False

    def get_displayed_appointment_date(self) -> datetime:
        text = self.page.get_appointment_date_text()
        import re
        match = re.search(r"\d{2}/\d{2}/\d{2}", text)
        if not match:
            raise ValueError("Could not find a valid date format in the appointment header.")

        displayed_str = match.group()  # e.g., "29/07/25"
        try:
            return datetime.strptime(displayed_str, "%d/%m/%y")
        except ValueError:
            raise ValueError(f"Invalid date format found in text: {displayed_str}")
