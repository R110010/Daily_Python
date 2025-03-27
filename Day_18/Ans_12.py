# Use logging to track function execution time.
import logging
import time

logging.basicConfig(filename="execution_time.log",filemode="a",level=logging.INFO)
def track_time():
    start_time = time.time()
    time.sleep(2)
    end_time = time.time()
    execution_time = end_time - start_time
    print("time to execute this function :",execution_time,"seconds with a delay of 2 seconds")
    logging.info(execution_time)

track_time()