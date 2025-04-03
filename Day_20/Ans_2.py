# Create multiple threads for different tasks.
import threading
def number_1(n):
    for i in range(1,n+1):
        print(f"{threading.current_thread().name} : {i}")
thread1 = threading.Thread(target=number_1, args=(3,),name="T1")
thread2 = threading.Thread(target=number_1, args=(5,),name="T2")
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print(" main thread execution completed")
