# Recognize which area of room are bigger, or same

length1 = int(input("Please input the length of the 1st room: "))
width1 = int(input("Please input the width of the 1st room: "))
length2 = int(input("Please input the length of the 2nd room: "))
width2 = int(input("Please input the width of the 2nd room: "))
if length1*width1 < length2*width2:
    print("The 2nd one is bigger.")
elif length1*width1 > length2*width2:
    print("The 1st one is bigger.")
else:
    print("They are same.")
