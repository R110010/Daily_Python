# Implement thread-safe increment function.
import threading
counter = 0
lock = threading.Lock()
def thread_safe():
    global counter
    with lock:
        counter+=1
threads = []
for _ in range(10000):
    thread = threading.Thread(target=thread_safe)
    threads.append(thread)
    thread.start()
for thread in threads:
    thread.join()
print(" counter ",counter)