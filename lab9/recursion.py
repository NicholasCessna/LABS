# Recursion Lab


def product_of_digits(x: int):
    
    x = abs(x)
    
    if x < 10:
        return x
    
    result = (x % 10) * product_of_digits(x//10) # 
    
    return result 

# Tests
print(product_of_digits(449)) # output should be 144
print(product_of_digits(12345678)) # output should be 40320



def array_to_string(a : list[int], index = 0):
    
    result = ""
    
    if index == len(a) - 1:
        return str(a[index])
    
    result = str(a[index]) + "," + array_to_string(a, index + 1)
    
    return result
    
    
    
# Tests   
print(array_to_string([122,212,113,334])) #List of ## printed as a string
print(array_to_string([1,2,3,4,5]))




# Tests
def log(base, value, count=0):
    
    if not (isinstance(base, int) and isinstance(value, int)):
        raise ValueError("Both input values must be integers")
    
    if base <= 1:
        raise ValueError("The entered base must be greater than 1")
        
    if value <= 0:
        raise ValueError("The entered value must be greater than 0")
    
    if value < base:
        return count
    
    # double slash for integer division and rounding
    result= log(base, value//base, count + 1)
    
    return result
    

# Tests    
print(log(2, 43)) # Ouput 5
print(log(10, 550)) # Ouput 2
