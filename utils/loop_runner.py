# utils/loop_runner.py
from datetime import datetime, timedelta
from pathlib import Path
import time
import os
import pytest

ROOT = Path(__file__).resolve().parents[1]
os.chdir(ROOT)

def ts() -> str:
    return datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")

def run_loop() -> int:
    interval = 6 * 60 * 60  # 6 hours
    end_time = datetime.now() + timedelta(hours=24)
    print(f"{ts()} start: run tests/disney_test.py every 6h for 24h (until {end_time:%Y-%m-%d %H:%M:%S})")

    while datetime.now() < end_time:
        print(f"{ts()} running pytest…")
        code = pytest.main(["-q", "tests/disney_test.py"])
        if code == 0:
            print(f"{ts()} success. exiting.")
            return 0

        if datetime.now() + timedelta(seconds=interval) > end_time:
            print(f"{ts()} 24h window reached. exiting.")
            break

        print(f"{ts()} sleeping 6h…")
        time.sleep(interval)

    return 1

if __name__ == "__main__":
    raise SystemExit(run_loop())
