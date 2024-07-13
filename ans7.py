import time
import logging

logging.basicConfig(level=logging.INFO)

def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        logging.info(f"Execution time of {func.__name__}: {execution_time:.2f} seconds")
        return result
    return wrapper

@timer_decorator
def expensive_task():
    result = 0
    for i in range(10000000):
        result += i
    return result

expensive_task()  