# utils/loop_runner.py
import time
from datetime import datetime, timedelta
from selenium import webdriver
from tests.elon_shlomo import elon_shlomo

if __name__ == "__main__":
    try:
        elon_shlomo()
    except Exception as e:
        print(f"No appointment or error: {e}")
