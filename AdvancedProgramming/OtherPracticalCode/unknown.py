def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

print(factorial(2))

# def linersearch(n, s):
#     for i in range(len(s - 1)):
#         if n[i] == s:
#             print("The index is ", i)
#             return i
#     return -1

# print(linersearch([1, 2, 3, 4, 5], 5))

# location = -1
# def search(array, n):
#     x = 0
#     while x < len(array):
#         if array[x] == n:
#             globals()['location'] = x
#             return True
#         x = x + 1

#     return False

# array = [3, 4, 5, 7, 8, 9, 1, 2]

# n = 9

# if search(array, n):
#     print("Hurray!")
# else:
#     print("Ooops")


def binsearch(array, n):
    low = 0
    upp = len(array) - 1

    while low <= upp:
        mid_index = (low + upp) // 2

        if array[mid_index] == n:
            globals()['locations'] = mid_index
            return True
        else:
            if array[mid_index] < n:
                low = mid_index + 1
            else:
                upp = mid_index - 1
    
    return False

array = [1, 2, 3, 4, 5, 7, 9]

y = 8

if binsearch(array, y):
    print("hurray!")
else:
    print("opps")