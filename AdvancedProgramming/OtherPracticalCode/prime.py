def primenum(num):
    for i in range(2,num):
        if num % i == 0:
            return False
        # else:
        i = i + 1
    return True
number = int(input("Please input a number "))
print(primenum(number))