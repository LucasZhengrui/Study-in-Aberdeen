width = float(input("Please insert the width of the room: "))
length = float(input("Please insert the length of the room: "))
unit = str(input("Please input the unit of your length and width(feet || meter): "))

area = width*length

if(unit == "feet"):
    print("The area of the room: ", area)
    print("feet**2")
elif(unit == "meter"):
    print("The area of the room: ", area)
    print("meter**2")