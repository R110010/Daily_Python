# Implement a thread that runs in the background.
import threading
import time
def bg_task():
    while True:
        print(" background task is running")
        time.sleep(1)
thread = threading.Thread(target=bg_task,daemon=True)
thread.start()
for i in range(1,4):
    print(" main program running ",i)
    time.sleep(2)
print(" main thread execution completed")