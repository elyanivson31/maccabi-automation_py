# loop_runner.py

import time
from datetime import datetime, timedelta
from selenium import webdriver
from tests.elon_shlomo import elon_shlomo
from tests.test_open_new_appointment import test_open_new_appointment

INTERVAL_MINUTES = 10
MAX_HOURS = 24

def main():
    start_time = datetime.now()
    end_time = start_time + timedelta(hours=MAX_HOURS)

    while datetime.now() < end_time:
        print(f"[{datetime.now().strftime('%H:%M:%S')}] Running test...")

        driver = webdriver.Chrome()
        try:
            elon_shlomo(driver)
            print("✅ Test passed. Exiting loop.")
            break  # exit loop if test passes
        except Exception as e:
            print(f"❌ Test failed: {e}")
        finally:
            driver.quit()

        print(f"⏳ Waiting {INTERVAL_MINUTES} minutes before retrying...\n")
        time.sleep(INTERVAL_MINUTES * 60)

    print("⏹️ Loop finished (either passed or hit time limit).")

if __name__ == "__main__":
    main()
