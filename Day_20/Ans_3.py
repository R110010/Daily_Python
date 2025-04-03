# Use join() to wait for a thread to finish.
import threading
def print_numbers():
    for i in range (1,8):
        print(i)
thread = threading.Thread(target=print_numbers)
thread.start()
thread.join()
print("\n main thread execution completed")