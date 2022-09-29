def div(x,y):
    if y == 0:
        return None
    else:
        return x/y

def div2(x,y):
    try:
        return x/y
    except:
        print("there is error")
        return None

result1 = div(3, 0)
print(result1)
result = div2(3, 0)
print(result)

# Best solution:
# def func():
#     while True:
#         try:
#             x = int(input("Please enter x: "))
#             y = int(input("Please enter y: "))
#             return x/y # If x and y are both correct, return can be ran, and break as well. Otherwise, it will skip to the except statement.
#             break
#         except:
#             print("The last input is not a number or y is 0.")
# 
# func()
#
# # It's an example to show how to make sure the input values are correct(try and except)
