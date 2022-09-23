def mystereNumber(x):
    x = x*x
    # print("The value of x is now ",x)  # useless
    return x

# x = 2
x = int(input("Please input a value that you want to put into x: "))
print("Value of x is",x)
# print(mystereNumber(x))
print("The value of x after calling mystereNumber is ",mystereNumber(x))


'''
The original version is:

def mystereNumber(x):
    x = x*x
    print("The value of x is now ",x)  # useless

x = 2
print("Value of x is",x)
mystereNumber(x)
print("The value of x after calling mystereNumber is ",x)

'''
