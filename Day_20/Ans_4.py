# Implement thread synchronization using a lock.
import threading
counter = 0
lock = threading.Lock()
def increment():
    global counter
    for _ in range(1000000):
        with lock:
            counter+=1
thread1 = threading.Thread(target=increment)
thread2 = threading.Thread(target=increment)
thread3 = threading.Thread(target=increment)
thread4 = threading.Thread(target=increment)

thread1.start()
thread2.start()
thread3.start()
thread4.start()

thread1.join()
thread2.join()
thread3.join()
thread4.join()

print(f" value of counter {counter}")