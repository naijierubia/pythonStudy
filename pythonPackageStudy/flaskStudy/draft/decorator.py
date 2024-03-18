import time

def time_it(message):
    def decorator(func):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            print(f"{message}: Function {func.__name__} executed in {end_time - start_time:.5f} seconds")
            return result
        return wrapper
    return decorator

@time_it("Adding numbers")
def add(a, b):
    return a + b

@time_it("Multiplying numbers")
def multiply(a, b):
    return a * b

result1 = add(1, 2)
result2 = multiply(3, 4)
