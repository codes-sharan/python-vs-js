import time

def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time:.4f} seconds to execute.")
        return result
    return wrapper

@timer_decorator
def my_function():
    time.sleep(1)

my_function()


@timer_decorator
def example_function(n):
    total = 0
    for i in range(n):
        total += i
    return total

# Call the decorated function
result = example_function(1000000)
print(f"Result: {result}")