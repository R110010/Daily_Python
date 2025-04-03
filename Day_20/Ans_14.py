# Use multiprocessing.Manager() to share state across processes.
import multiprocessing
def worker(shared_list, value):
    shared_list.append(value)
if __name__ == "__main__":
    manager = multiprocessing.Manager()
    shared_list = manager.list()
    processes = []
    for i in range(5):
        p = multiprocessing.Process(target=worker, args=(shared_list, i))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()
    print("Final shared list:", list(shared_list))
