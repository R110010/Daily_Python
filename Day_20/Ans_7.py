# Implement process communication using Queue().
import multiprocessing
def worker1(queue):
    queue.put(" Hello send from process1 and retrieved by process2")
def worker2(queue):
    message = queue.get()
    print(message)

if __name__=="__main__":
    queue = multiprocessing.Queue()
    process1 = multiprocessing.Process(target=worker1,args=(queue,))
    process2 = multiprocessing.Process(target=worker2,args=(queue,))
    process1.start()
    process1.join()
    process2.start()
    process2.join()


print(" both process executed")