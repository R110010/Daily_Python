# Create a thread that prints current time every second.
import threading
import time
from datetime import datetime
def time_now():
    while True:
        try:
            date = datetime.now().strftime("%H:%M:%S")
            print(date)
            time.sleep(1)
        except KeyboardInterrupt:
            print(" program stopped ")
thread = threading.Thread(target=time_now)
thread.start()
thread.join()
print("program executed")