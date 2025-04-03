# Write a function that utilizes multi-processing to speed up computation.
import multiprocessing
import time
def square(n):
    return n * n
def parallel_square(numbers):
    with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
        results = pool.map(square, numbers)
    return results
if __name__ == "__main__":
    numbers = list(range(1, 1000000))
    start_time = time.time()
    results = parallel_square(numbers)
    end_time = time.time()
    print(f"First 10 results: {results[:10]}")
    print(f"Time taken with multiprocessing: {end_time - start_time:.4f} seconds")
