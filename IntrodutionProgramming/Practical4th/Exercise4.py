# Find the median one in three values.

def sort(a,b,c):
    if (a > b and b > c) or (c > b and b > a):
        print("b is the median number.")
    elif (a > c and c > b) or (b > c and c > a):
        print("c is the median number.")
    else:
        print("a is the median number.")

a = int(input("Please input the first number."))
b = int(input("Please input the second number(different from the 1st one)."))
c = int(input("Please input the third number(different from the 1st, 2nd one)."))
sort(a,b,c)
