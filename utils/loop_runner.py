# # from selenium import webdriver
# # import sys
# # import os

# # sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# # from tests.elon_shlomo import elon_shlomo



# # def main():
# #     print("🔄 Running test once...")
# #     driver = webdriver.Chrome()
# #     try:
# #         success = elon_shlomo(driver)
# #         if success:
# #             print("✅ Test passed.")
# #         else:
# #             print("❌ No appointment found.")
# #     except Exception as e:
# #         print(f"⚠️ Test raised an exception: {e}")
# #     finally:
# #         driver.quit()

# # if __name__ == "__main__":
# #     main()











# utils/loop_runner.py
import time
from datetime import datetime, timedelta
from selenium import webdriver
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from tests.test_elon_shlomo import elon_shlomo


def timestamp():
    return datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")


def run_loop_for_max_duration(max_minutes=900, interval_minutes=10):
    end_time = datetime.now() + timedelta(minutes=max_minutes)

    while datetime.now() < end_time:
        print(f"\n{timestamp()} 🔄 Running test...")
        driver = webdriver.Chrome()
        try:
            success = elon_shlomo(driver)
            if success:
                print(f"{timestamp()} ✅ Test passed. Stopping loop.")
                break
            else:
                print(f"{timestamp()} ❌ No appointment found. Retrying in {interval_minutes} minutes...")
        except Exception as e:
            print(f"{timestamp()} ⚠️ Test raised an exception: {e}")
            print(f"{timestamp()} ⏱️ Will retry in {interval_minutes} minutes...")
        finally:
            driver.quit()

        time.sleep(interval_minutes * 60)


if __name__ == "__main__":
    run_loop_for_max_duration()
