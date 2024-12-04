# Task three fitler function using reduce()

from functools import reduce

def filter_using_reduce(function, iterable):
    return reduce(lambda items, value: items + [value] if function(value) else items, iterable,[],)




# Tests
numbers = [1, 2, 3, 4, 5, 6]

my_function_result = ("Filter using Reduce", list(filter_using_reduce(lambda x: x % 2 == 0, numbers)))  
print(my_function_result)

filter_function_result = ("filter function result:", list(filter(lambda x: x % 2 == 0, numbers)))
print(filter_function_result)