# Use Thread class with arguments.
import threading
import time
def print_num(name,count):
    for i in range(1,count+1):
        print(f"{name} count ={i}")
        time.sleep(0.5)
thread1 = threading.Thread(target=print_num,args=("thread_1",5))
thread2 = threading.Thread(target=print_num,args=("thread_2",4))
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print("Execution completed")