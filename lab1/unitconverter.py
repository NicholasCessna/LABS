import math

CM_IN = 0.393701
IN_CM = 2.54
YD_M = 0.9144
M_YD = 1.09361
OZ_G = 28.349523125
G_OZ = 0.035274
LB_KG = 0.45359237
KG_LB = 2.20462

measurment = input("Please enter a Distance or Weight you would like to convert followed by its units separated by a space (Acceptable Units:in, cm, yd, m, oz, g, kg, lb): ")

num_mes = measurment.split(" ")[0]
unit_mes = measurment.split(" ")[1]

if unit_mes == "cm":
    num_mes2 = float(num_mes) * CM_IN
    unit_mes2 = "in"
    print(num_mes, unit_mes, " = ", round(num_mes2, 2), unit_mes2)
    
elif unit_mes == "in":
    num_mes2 = float(num_mes) * IN_CM
    unit_mes2 = "cm"
    print(num_mes, unit_mes, " = ", round(num_mes2, 2), unit_mes2)
    
elif unit_mes == "yd":
    num_mes2 = float(num_mes) * YD_M
    unit_mes2 = "m"
    print(num_mes, unit_mes, " = ", round(num_mes2, 2), unit_mes2)
    
elif unit_mes == "m":
    num_mes2 = float(num_mes) * M_YD
    unit_mes2 = "yd"
    print(num_mes, unit_mes, " = ", round(num_mes2, 2), unit_mes2)
    
elif unit_mes == "oz":
    num_mes2 = float(num_mes) * OZ_G
    unit_mes2 = "g"
    print(num_mes, unit_mes, " = ", round(num_mes2, 2), unit_mes2)
    
elif unit_mes == "g":
    num_mes2 = float(num_mes) * G_OZ
    unit_mes2 = "oz"
    print(num_mes, unit_mes, " = " , round(num_mes2, 2), unit_mes2)
    
elif unit_mes == "lb":
    num_mes2 = float(num_mes) * LB_KG
    unit_mes2 = "kg"
    print(num_mes, unit_mes, " = ", round(num_mes2, 2), unit_mes2)
    
elif unit_mes == "kg":
    num_mes2 = float(num_mes) * KG_LB
    unit_mes2 = "lb"
    print(num_mes, unit_mes, " = ", round(num_mes2, 2), unit_mes2)