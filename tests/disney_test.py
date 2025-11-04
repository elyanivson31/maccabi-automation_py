# tests/disney_test.py
from dlp_last_month import get_last_month_number
from utils.notifier import notify_telegram_channel
import calendar

def test_disney_notification():
    last_month = get_last_month_number()
    month_name = calendar.month_name[int(last_month)]
    notify_telegram_channel(f"The last available month for Disney Tickets is: {month_name}")
