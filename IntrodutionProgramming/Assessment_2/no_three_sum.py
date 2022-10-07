'''
Write a program called “no_three_sum”, which take three integer values a, b, and c as
arguments and returns their sum. However, if any of the values is a multiple of three e.g. 3, 6, 9,
12, … then that value counts as 0, except the multiples of three between 20 and 29. Write a
separate helper function "def fix_three(n): "that takes in an integer value and returns that value
fixed for the rule. Then make use of this helper function through “no_three_sum” (15 Marks).
For example,
no_three_sum(1, 2, 3) → 3
no_three_sum(2, 13, 1) → 16
no_three_sum(2, 1, 21) → 24 
'''

def no_three_sum(a, b, c):
    num1 = fix_three(a) # Quote the fix_three function to fix the value of a, b, and c
    num2 = fix_three(b)
    num3 = fix_three(c)
    sum = num1 + num2 + num3 # Caculate the final sum value, and then return it
    return sum

def fix_three(n):
    if (n >= 20 and n <= 29): # if n(number) is between 20 and 29, it will not be changed or fixed here, so return directly
        return n
    else:
        if n % 3 == 0: # if n(number) is a multiple of 3, besides the number between 20 and 29, it will becomes zero
            n = 0
        return n

try:
    a = int(input("Please input the first number: "))
    b = int(input("Please input the second number: "))
    c = int(input("Please input the third number: ")) # input a, b, and c separately
    print("The numbers you have input are", a, b, c) # print the original number firstly, so that can see the difference
    sum = no_three_sum(a, b, c)
    print("Due to the internal rules, the sum of your numbers is", sum)
except:
    print("Input error!")
