tmp = int(input("Please input the temperature of water: "))
if tmp >= 212:
    print("It's in gas state.")
elif tmp > 32 and tmp < 212:  # 32 < tmp < 212 is incorrect, Operator cannot recognize two.
    print("It's in liquid state.")
else:
    print("It's in ice state.")
