import uuid
from flows.web_flow import WebFlow
from flows.web_flow import WebFlow
from flows.main_flow import MainFlow
from infra.data_loader import DataLoader
from api.maccabi_api import call_maccabi_search_api

def test_open_new_appointment(driver):
    contact = DataLoader().get_contact_by_name("yaniv")

    # Create and reuse WebFlow instance
    web_flow = WebFlow(driver)

    web_flow.login_flow().login_to_portal(contact)
    
    if "selectedPatient" in contact:
        web_flow.main_flow().switch_patient(contact["selectedPatient"])

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
    a = response.text
    assert response.status_code == 200
    print(response.json())