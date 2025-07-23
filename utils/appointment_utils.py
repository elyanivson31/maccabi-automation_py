from datetime import datetime

def is_appointment_sooner_than_threshold(api_response: dict, threshold_date: datetime) -> bool:
    """
    Check if any appointment in the response is sooner than the threshold date.
    """
    for item in api_response.get("Items", []):
        closest_date_str = item.get("CLOSEST_APPOINMENT_DATE")
        if not closest_date_str:
            continue
        try:
            closest_date = datetime.fromisoformat(closest_date_str)
            if closest_date < threshold_date:
                return True
        except ValueError:
            pass  # skip malformed date strings
    return False
