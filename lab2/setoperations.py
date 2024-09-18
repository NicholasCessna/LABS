# Lab 2 Intermediate Python

def make_set(data):
    list_int = []
    for item in data:
        if item not in list_int:
            list_int.append(item)
            
    return list_int

# make_set tests
# print(make_set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5]))
# print(make_set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
# print(make_set([1, 2, 3, 4, 4, 5]))
# print(make_set([]))



def is_set(data):
    if data is None:
        return False
    
    list_int = []
    for item in data:
        if item not in list_int:
            list_int.append(item)
        else:
            return False
        
    return True

#is_set tests
# print(is_set([1, 2, 3, 4, 5]))
# print(is_set([5, 5]))
# print(is_set([]))
# print(is_set(None))



def union(setA, setB):
    if not is_set(setA) or not is_set(setB):
        return []
    
    union_set = []
    for item in setA:
        if item not in union_set:
            union_set.append(item)
    
    for item in setB:
        if item not in union_set:
            union_set.append(item)
    
    return union_set

# union tests
# print(union([1,2], [2,3]))
# print(union([], [2,3]))
# print(union([1,1,1], [2,3]))




def intersection(setA, setB):
    if not is_set(setA) or not is_set(setB):
        return []
    
    intersection_set = []
    for item in setA:
        if item in setB:
            intersection_set.append(item)
            
    return intersection_set

# intersection tests
# print(intersection([1,2], [2,3])) 
# print(intersection([], [2,3]))
# print(intersection([1,1,1], [2,]))
    
        