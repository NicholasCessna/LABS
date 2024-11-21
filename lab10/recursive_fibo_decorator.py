# Task 2 Fibonacci
import time
import functools


# High level function to create decorator
def store_value(func):
    cache = {}

    @functools.wraps(func)
    def wrapper(*args):
        if args in cache:
            return cache[args]
        else:
            result = func(*args)
            cache[args] = result
            return result

    return wrapper
  

# Fibo using decorator
@store_value
def recur_fib(n):
    if n <= 1:
        return n
    else:
        return(recur_fib(n-1) + recur_fib(n-2))


# Original Fibo
def original_recur_fib(n):
    if n <= 1:
        return n
    else:
        return(original_recur_fib(n-1) + original_recur_fib(n-2))
    
   
n = 35

start_time = time.time()
original_recur_fib(n)
original_time = time.time() - start_time

start_time = time.time()
recur_fib(n)
decorated_time = time.time() - start_time

print(f"Original Fibonacci Time: {original_time:.6f} seconds")
print(f"Decorated Fibonacci Time: {decorated_time:.6f} seconds")