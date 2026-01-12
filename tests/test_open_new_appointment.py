import uuid

from selenium.webdriver.chrome.webdriver import WebDriver
from flows.confirm_appointment_flow import ConfirmAppointmentFlow
from flows.set_appointment_flow import SetAppointmentFlow
from flows.web_flow import WebFlow
from flows.main_flow import MainFlow
from infra.data_loader import DataLoader
from api.maccabi_api import call_maccabi_search_api
from datetime import datetime
from utils.appointment_utils import get_soonest_appointment_before_threshold, is_appointment_sooner_than_threshold
from utils.notifier import notify_telegram_channel


def test_open_new_appointment(driver: WebDriver):
    data_loader = DataLoader()
    contact = data_loader.get_contact_by_name("yaniv_marina")
    selected_patient = contact["selectedPatient"]

    threshold_str = data_loader.get_contact_setting("yaniv_marina", "appointmentThresholdDate")
    threshold_date = datetime.fromisoformat(threshold_str)



    service_name = data_loader.get_contact_setting("yaniv_marina", "appointmentServiceName")

    city_name = data_loader.get_contact_setting("yaniv_marina", "appointmentDoctorCity")
    appointment_type = data_loader.get_contact_setting("yaniv_marina", "appointmentType")

    # Create and reuse WebFlow instance
    web_flow = WebFlow(driver)

    web_flow.login_flow().login_to_portal(contact)
    
    web_flow.main_flow().switch_to_patient(selected_patient)

    web_flow.main_flow().start_new_appointment()

    if "doctorName" not in contact:
        raise ValueError("Missing 'doctorName' in contact settings.")
    
    # Assume you're logged in
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
    print(response.json())


    # assert is_appointment_sooner_than_threshold(response_json, threshold_date)

    soonest_date = get_soonest_appointment_before_threshold(response_json, threshold_date)

    if soonest_date:
        notify_telegram_channel(
            f"🎉 נמצא תור מוקדם!\n"
            f"👤 מטופל: {contact['selectedPatient']}\n"
            f"🧑‍⚕️ רופא: {contact['doctorName']}\n"
            f"🗓️ תאריך זמין: {soonest_date.strftime('%d/%m/%Y %H:%M')}\n"
            f"📅 סף תאריך: {threshold_date.strftime('%d/%m/%Y')}\n"
        )
    else:
        notify_telegram_channel(
            f"ℹ️ בדיקת תורים הושלמה\n"
            f"👤 מטופל: {contact['selectedPatient']}\n"
            f"🧑‍⚕️ רופא: {contact['doctorName']}\n"
            f"❌ לא נמצא תור לפני {threshold_date.strftime('%d/%m/%Y')}\n"
            f"⚠️ ממשיך בתהליך בכל זאת...\n"
        )


    web_flow.set_appointment_flow().continue_to_doctor_search()
    web_flow.set_appointment_flow().choose_service(service_name)
    web_flow.find_doctor_flow().search_for_doctor(contact["doctorName"], city_name)
    

    web_flow.find_doctor_flow().select_set_appointment()
    
    web_flow.choose_appointment_type_flow().select_appointment_type_and_continue(
    appointment_type)

    web_flow.choose_appointment_type_flow().select_under_18_if_present()
    web_flow.choose_appointment_type_flow().agree_to_come_with_personal_health_card()


    actual_date = web_flow.confirm_appointment_flow().get_displayed_appointment_date()

    assert actual_date.date() <= threshold_date.date(), (
    f"❌ Appointment date mismatch!\n"
    f"🟡 Expected (threshold): {threshold_date.strftime('%d/%m/%Y')}\n"
    f"🔵 Displayed on page:   {actual_date.strftime('%d/%m/%Y')}"
)
    
    web_flow.confirm_appointment_flow().choose_time_slot()

    web_flow.confirm_appointment_flow().confirm_appointment()

    web_flow.confirm_appointment_flow().confirm_and_continue()
    success = web_flow.confirm_appointment_flow().verify_appointment_success()

    if success:
          notify_telegram_channel(
    f"🎉 התור נקבע בהצלחה!!\n"
    f"👤 מטופל: {contact['selectedPatient']}\n"
    f"🧑‍⚕️ רופא: {contact['doctorName']}\n"
)
    else:
        raise AssertionError("❌ קביעת התור לא הצליחה או שההודעה של סיום התהליך השתנתה")