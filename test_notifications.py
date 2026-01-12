#!/usr/bin/env python3
"""
Test script to verify Telegram notifications work for both scenarios:
1. When appointment is found before threshold
2. When no appointment is found before threshold
"""
from datetime import datetime
from utils.notifier import notify_telegram_channel


def test_notification_success_scenario():
    """Test notification when appointment is found"""
    print("Testing SUCCESS notification scenario...")

    contact_name = "Test Patient"
    doctor_name = "Dr. Test"
    appointment_date = datetime(2025, 7, 25, 14, 0)
    threshold_date = datetime(2025, 7, 29, 23, 59, 59)
    city_name = "Tel Aviv"

    notify_telegram_channel(
        f"🎉 נמצא תור מוקדם!\n"
        f"👤 מטופל: {contact_name}\n"
        f"🧑‍⚕️ רופא: {doctor_name}\n"
        f"🗓️ תאריך זמין: {appointment_date.strftime('%d/%m/%Y %H:%M')}\n"
        f"📅 סף תאריך: {threshold_date.strftime('%d/%m/%Y')}\n"
    )

    print("✓ Success notification sent!")


def test_notification_no_appointment_scenario():
    """Test notification when no appointment is found"""
    print("\nTesting NO APPOINTMENT notification scenario...")

    contact_name = "Test Patient"
    doctor_name = "Dr. Test"
    threshold_date = datetime(2025, 7, 29, 23, 59, 59)
    city_name = "Tel Aviv"

    notify_telegram_channel(
        f"ℹ️ בדיקת תורים הושלמה\n"
        f"👤 מטופל: {contact_name}\n"
        f"🧑‍⚕️ רופא: {doctor_name}\n"
        f"🏙️ עיר: {city_name}\n"
        f"❌ לא נמצא תור לפני {threshold_date.strftime('%d/%m/%Y')}\n"
    )

    print("✓ No appointment notification sent!")


def main():
    print("=" * 60)
    print("Telegram Notification Mechanism Test")
    print("=" * 60)
    print("\nThis will send 2 test notifications to your Telegram channel:")
    print("1. Appointment found notification")
    print("2. No appointment found notification")
    print("\nPress Ctrl+C to cancel, or Enter to continue...")

    try:
        input()
    except KeyboardInterrupt:
        print("\n\nTest cancelled.")
        return

    try:
        test_notification_success_scenario()
        test_notification_no_appointment_scenario()

        print("\n" + "=" * 60)
        print("✓ All notifications sent successfully!")
        print("=" * 60)
        print("\nPlease check your Telegram channel to verify you received:")
        print("  1. Success message with appointment details")
        print("  2. Info message about no appointments found")

    except Exception as e:
        print(f"\n❌ Error sending notifications: {e}")
        raise


if __name__ == "__main__":
    main()
