import math

CON_FAC = 2

a = input("Please enter the first number corosponding to the length of a triangle: ")
b = input("Please enter the second number corosponding to the length of a triangle: ")

a = int(a)
b = int(b)

c = math.sqrt(a**CON_FAC + b**CON_FAC)

print("The hypottenuse of the triangle is ", round(c,CON_FAC))


