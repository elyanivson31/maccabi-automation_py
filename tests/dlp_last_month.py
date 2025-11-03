# dlp_last_month.py
import requests
from datetime import datetime

def get_last_month_number() -> int:
    """
    Calls the Disneyland Paris price calendar API
    and returns the last available month number (1–12).
    """
    headers = {
        "accept": "application/json",
        "content-type": "application/json; charset=UTF-8",
        "origin": "https://tickets.disneylandparis.com",
        "referer": "https://tickets.disneylandparis.com/",
        "user-agent": "Mozilla/5.0",
    }

    payload = {
        "market": "en-usd",
        "currency": "USD",
        "startDate": "2025-11-03",
        "endDate": "2026-03-31",
        "products": [
            {
                "productType": "2-day-2-parks",
                "adultProductCode": "TKITHS002A",
                "childProductCode": "TKITHS002C",
            }
        ],
        "eligibilityInformation": {
            "salesChannel": "DIRECT",
            "membershipType": "",
            "masterCategoryCodes": ["EVENT", "TICKET", "TKTEXPERI"],
        },
    }

    response = requests.post(
        "https://api.disneylandparis.com/prices-calendar/api/v2/prices/ticket-price-calendar",
        headers=headers,
        json=payload,
        timeout=30,
    )
    response.raise_for_status()

    data = response.json()
    calendar = data.get("calendar", [])
    if not calendar:
        raise ValueError("No calendar data returned.")

    dates = []
    for item in calendar:
        try:
            dates.append(datetime.strptime(item["date"], "%Y-%m-%d"))
        except Exception:
            pass

    if not dates:
        raise ValueError("No valid date entries found.")

    last_date = max(dates)
    return last_date.month
