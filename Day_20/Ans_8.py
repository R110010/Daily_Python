# Compare performance between multi-threading and multi-processing.
import threading
import multiprocessing
import time
def sum_square():
    return sum(x*x for x in range(1,100000000))
def run_thread():
    thread1 = threading.Thread(target=sum_square)
    thread2 = threading.Thread(target=sum_square)
    start =time.time()
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    exec_time = time.time()-start
    print(" time taken for threading ",exec_time)
def run_process():
    process1 = multiprocessing.Process(target=sum_square)
    process2 = multiprocessing.Process(target=sum_square)
    start = time.time()
    process1.start()
    process2.start()
    process1.join()
    process2.join()
    exec_time = time.time()-start
    print(" time taken for multiprocessing ",exec_time)

if __name__=="__main__":
    run_thread()
    run_process()