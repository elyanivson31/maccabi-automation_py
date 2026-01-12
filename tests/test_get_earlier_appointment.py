import uuid
from selenium.webdriver.chrome.webdriver import WebDriver
from flows.web_flow import WebFlow
from infra.data_loader import DataLoader
from api.maccabi_api import call_maccabi_search_api
from datetime import datetime
from utils.appointment_utils import get_soonest_appointment_in_city
from utils.notifier import notify_telegram_channel


def test_get_earlier_appointment(driver: WebDriver) -> bool:
    try:
        driver.maximize_window()  # 👈 Maximize after initialization
        data_loader = DataLoader()
        contact = data_loader.get_contact_by_name("yaniv_marina")
        selected_patient = contact["selectedPatient"]

        threshold_str = data_loader.get_contact_setting("yaniv_marina", "appointmentThresholdDate")
        threshold_date = datetime.fromisoformat(threshold_str)

        service_name = data_loader.get_contact_setting("yaniv_marina", "appointmentServiceName")
        city_name = data_loader.get_contact_setting("yaniv_marina", "appointmentDoctorCity")
        appointment_type = data_loader.get_contact_setting("yaniv_marina", "appointmentType")

        web_flow = WebFlow(driver)
        web_flow.login_flow().login_to_portal(contact)
        # web_flow.main_flow().switch_to_patient(selected_patient)
        web_flow.main_flow().start_new_appointment()

        if "doctorName" not in contact:
            raise ValueError("Missing 'doctorName' in contact settings.")

        payload = {
            "DocName": contact["doctorName"],
            "ChapterId": "001",
            "InitiatorCode": "001",
            "isKosher": 0,
            "IsMobileApplication": 0,
            "PageNumber": 1,
            "RequestId": str(uuid.uuid4())
        }

        response = call_maccabi_search_api(driver, payload)
        response_json = response.json()
        assert response.status_code == 200

        soonest_date = get_soonest_appointment_in_city(response_json, threshold_date, city_name)

        if soonest_date:
            notify_telegram_channel(
                f"🎉 נמצא תור מוקדם!\n"
                f"👤 מטופל: {contact['selectedPatient']}\n"
                f"🧑‍⚕️ רופא: {contact['doctorName']}\n"
                f"🗓️ תאריך זמין: {soonest_date.strftime('%d/%m/%Y %H:%M')}\n"
                f"📅 סף תאריך: {threshold_date.strftime('%d/%m/%Y')}\n"
            )
            return True
        else:
            notify_telegram_channel(
                f"ℹ️ בדיקת תורים הושלמה\n"
                f"👤 מטופל: {contact['selectedPatient']}\n"
                f"🧑‍⚕️ רופא: {contact['doctorName']}\n"
                f"🏙️ עיר: {city_name}\n"
                f"❌ לא נמצא תור לפני {threshold_date.strftime('%d/%m/%Y')}\n"
            )
            return False

    except Exception as e:
        print(f"❗ Exception in test_get_earlier_appointment: {e}")
        raise
