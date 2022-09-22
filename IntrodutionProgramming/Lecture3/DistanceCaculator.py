import math
x1 = int(input("Please input the location 1's X"))
y1 = int(input("Please input the location 1's Y"))
x2 = int(input("Please input the location 2's X"))
y2 = int(input("Please input the location 2's Y"))
D = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
# D = ((x1 - x2)**2 + (y1 - y2)**2)**0.5
print("Distance between these two locations: ")
print(D)


# How to rename the library's name:
# import math as (any names you want)
