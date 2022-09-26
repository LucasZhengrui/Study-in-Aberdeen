# Finding the highest number in a lot of values. 

highest = 1
while highest != 0:
    num = int(input("Please enter a number: "))
    if highest < num:
        highest = num
    elif num == 0:
        break
print(highest)
