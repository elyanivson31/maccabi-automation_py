# utils/loop_runner.py
import time
from datetime import datetime, timedelta
from selenium import webdriver
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from tests.elon_shlomo import elon_shlomo



def run_loop_for_max_duration(max_minutes=120, interval_minutes=10):
    end_time = datetime.now() + timedelta(minutes=max_minutes)

    while datetime.now() < end_time:
        print("\n🔄 Running test...")
        driver = webdriver.Chrome()
        try:
            success = elon_shlomo(driver)
            if success:
                print("✅ Test passed. Stopping loop.")
                break
            else:
                print("❌ No appointment found. Retrying in 10 minutes...")
        except Exception as e:
            print(f"⚠️ Test raised an exception: {e}")
            print("⏱️ Will retry in 10 minutes...")
        finally:
            driver.quit()

        time.sleep(interval_minutes * 60)


if __name__ == "__main__":
    run_loop_for_max_duration()
