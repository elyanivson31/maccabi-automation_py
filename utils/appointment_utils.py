from datetime import datetime
from typing import Optional

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


def get_soonest_appointment_before_threshold(api_response: dict, threshold_date: datetime) -> Optional[datetime]:
    """
    Return the earliest appointment date before the threshold, if any.
    """
    for item in api_response.get("Items", []):
        date_str = item.get("CLOSEST_APPOINMENT_DATE")
        if not date_str:
            continue
        try:
            date = datetime.fromisoformat(date_str) 
            if date <= threshold_date:
                return date
        except ValueError:
            continue
    return None

def get_soonest_appointment_in_city(api_response: dict, threshold_date: datetime, target_city: str) -> Optional[datetime]:
    """
    Return the earliest appointment date before the threshold, only for the given city.
    """
    soonest_date = None

    for item in api_response.get("Items", []):
        city = item.get("CITY_NAME", "").strip()
        if city != target_city.strip():
            continue

        date_str = item.get("CLOSEST_APPOINMENT_DATE")
        if not date_str:
            continue

        try:
            date = datetime.fromisoformat(date_str)
            if date <= threshold_date:
                if soonest_date is None or date < soonest_date:
                    soonest_date = date
        except ValueError:
            continue

    return soonest_date

