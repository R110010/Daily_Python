# Implement a worker thread pool for processing tasks.
from concurrent.futures import ThreadPoolExecutor
import time
def sq_num(n):
    time.sleep(0.5)
    return n*n
with ThreadPoolExecutor(max_workers=2) as executer:
    square =list(executer.map(sq_num,[1,2,3,4,5]))
print(" squared number list = ",square)