# Caculate the greatest common divisor between two values through the Euclides algorithm.

def gcd(x,y):
    r = x%y
    if r != 0:
        x = y
        y = r
    else:
        print("Please check it again")
    return y

x = int(input("Please input the greater value (x): "))
y = int(input("Please input the smaller one (y): "))
gcd(x,y)
