import math

CON_FAC = 2

radius = input("Please enter the radius of the circle: ")
radius = int(radius)


perimeter = CON_FAC * math.pi * radius 
area = math.pi * radius**CON_FAC

print("The circle with a radius of ", radius, " has an area of ", round(area,CON_FAC), " and a perimeter of ", round(perimeter,CON_FAC))
