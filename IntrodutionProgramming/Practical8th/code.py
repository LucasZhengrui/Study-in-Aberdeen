list = []
temp = 0

def number():
    num = int(input("Please enter the number of your elements"))
    return num   

def sort(num, sublist):
    for item in range(num, 0, -1):
        for item1 in range(0, item - 1):
            if sublist[item1] > sublist[item1 + 1]:
                temp = sublist[item1]
                sublist[item1] = sublist[item1 + 1]
                sublist[item1 + 1] = temp
        
    return sublist

def bin_search(num, sublist):
    low = 1
    high = num - 1
    pos = -1
    value = int(input("Please input a value that you want to check is it in the list: "))
    while low <= high and pos == -1:
        mid = (low + high) // 2
        if sublist[mid] > value:
            high = mid - 1
        elif sublist[mid] < value:
            low = mid + 1
        else:
            pos = mid

    return pos

length = number()
for item in range(length):
    num = int(input("Please enter a value: "))
    list.append(num)

print("The list you input is ", list)
sublist = sort(length, list)
print("The list after sorting is", sublist)
no = bin_search(length, sublist)
if no == -1:
    print("The number you want to search is no in the list.")
else:
    print("The number you want to search is in No.", no + 1)
