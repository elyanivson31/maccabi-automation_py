from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from tests.elon_shlomo import elon_shlomo

def run_test():
    options = Options()
    options.add_argument("--headless")  # For CI
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)

    try:
        elon_shlomo(driver)  # ✅ manually pass driver
        return True
    except Exception as e:
        print(f"❌ Test failed: {e}")
        return False
    finally:
        driver.quit()
