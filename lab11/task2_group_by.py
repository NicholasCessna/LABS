# Task two group_by function

from functools import reduce

def group_by(f, imported_list: list):
    
    elements = map(lambda x: (f(x), x), imported_list)
    
    return reduce(lambda grouped_dict, pair: {**grouped_dict, pair[0]: grouped_dict.get(pair[0], []) + [pair[1]]}, elements,{})



# Tests
print(group_by(len, ["hi", "dog", "me", "bad", "good"]))
print(group_by(len, ["hello", "dog", "meals", "supercalafragalisticexpealadocious", "good"]))
# Use with lambda function grouping by first letter.
print(group_by(lambda x: x[0], ["apple", "banana", "apricot", "cherry", "blueberry"]))