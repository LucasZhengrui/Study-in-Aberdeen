def doubles(num):
    num = num*2
    return num

num = int(input("Please input a number: "))
for i in range(1,4): # Or range(3)
    num = doubles(num)
    print(num)
