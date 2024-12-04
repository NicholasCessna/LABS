# Task One Zipmap

def zipmap(key_list: list, value_list: list, override=False):
    
    values = value_list[:len(key_list)] + [None] * (len(key_list) - len(value_list))
    
    key_value_pairs = map(lambda grouped_dict: grouped_dict, zip(key_list, values))
    
    if override:
        return dict(key_value_pairs)
    else:
        if len(key_list) != len(set(key_list)):
            return None
        return dict(key_value_pairs)



# Tests
print(zipmap(['a', 'b', 'c'], [1, 2, 3]))  
print(zipmap([1, 2, 3, 2], [4, 5, 6, 7], True))  
print(zipmap([1, 3, 5, 7], [2, 4, 6]))  