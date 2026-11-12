import time
from datetime import datetime

while True:
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("log.txt", "a") as f:
        f.write(f"[{now}] Service updated and running!\n")
    time.sleep(5)
