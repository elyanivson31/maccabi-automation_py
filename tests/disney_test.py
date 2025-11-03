# main.py
from dlp_last_month import get_last_month_number
from utils.notifier import notify_telegram_channel

last_month = get_last_month_number()
print(f"The last available month number is: {last_month}")

notify_telegram_channel(f"The last available month for Disney Tickets is: {last_month}")