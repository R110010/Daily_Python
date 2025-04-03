 # Create a thread to print numbers from 1 to 10.
import threading
def print_numbers():
    for i in range (1,20):
        print(i,end=" ")
thread = threading.Thread(target=print_numbers)
thread.start()
thread.join()
print("\n main thread execution completed")