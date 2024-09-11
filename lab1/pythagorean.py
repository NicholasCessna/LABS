import math

EXPONENT = 2

a = input("Please enter the first number corosponding to the length of a triangle: ")
b = input("Please enter the second number corosponding to the length of a triangle: ")

a = int(a)
b = int(b)

c = math.sqrt(a**EXPONENT + b**EXPONENT)

print("The hypottenuse of the triangle is ", round(c, 2))


