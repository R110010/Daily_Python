# Use multiprocessing to run two functions simultaneously.
import multiprocessing
import time
def numbers():
    for i in range(1,6):
        print(" function number ",i)
        time.sleep(1)
def letters():
    for letter in ["a","b","c","d","e"]:
        print(" function letters ",letter)
        time.sleep(1)
if __name__=="__main__":
    process1 = multiprocessing.Process(target=numbers)
    process2 = multiprocessing.Process(target=letters)

    process1.start()
    process2.start()

    process1.join()
    process2.join()
    print(" both process executed")