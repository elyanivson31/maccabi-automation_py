# utils/loop_runner.py
from datetime import datetime, timedelta
from pathlib import Path
import subprocess
import time
import os
import sys

ROOT = Path(__file__).resolve().parents[1]
os.chdir(ROOT)

def ts() -> str:
    return datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")

def run_loop() -> int:
    interval = int(os.getenv("LOOP_INTERVAL", str(3 * 60 * 60)))      # seconds (default: 6h)
    duration = int(os.getenv("LOOP_DURATION", str(7 * 24 * 60 * 60))) # seconds (default: 7d)
    end_time = datetime.now() + timedelta(seconds=duration)

    print(f"{ts()} start: run tests/disney_test.py every {interval}s for {duration}s "
          f"(until {end_time:%Y-%m-%d %H:%M:%S})")

    while datetime.now() < end_time:
        print(f"{ts()} running pytest…")
        result = subprocess.run(
            [sys.executable, "-m", "pytest", "-q", "tests/disney_test.py"],
            cwd=str(ROOT),
        )
        code = result.returncode
        print(f"{ts()} {'✅ passed' if code == 0 else f'❌ failed (exit {code})'}")

        # stop if the next sleep would exceed the window
        if datetime.now() + timedelta(seconds=interval) > end_time:
            print(f"{ts()} time window reached. exiting.")
            break

        print(f"{ts()} sleeping {interval}s…")
        time.sleep(interval)

    return 0

if __name__ == "__main__":
    raise SystemExit(run_loop())
