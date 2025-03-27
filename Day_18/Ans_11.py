# Implement a retry mechanism for an unreliable function.
import random
import time

def un_func():
    if random.random()<0.7:
        raise ValueError(" failure retrying")
    else:
        return "Success"
    
def retry_func(func,retries=3,delay=2):
    for attempt in range(1,retries+1):
        try:
            result = func()
            print("success ")
            return result
        except Exception as e:
            print(f"Attempt :{attempt} {e}")
            if attempt<retries:
                time.sleep(delay)
            else:
                print("Maximum tries exceeded.")
                

retry_func(un_func)