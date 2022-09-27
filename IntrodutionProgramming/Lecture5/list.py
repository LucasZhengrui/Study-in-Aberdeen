# lst = [1, 2, 3, 4, 5] # int
# lst_str = ["a", "hello","python"] # str

# lst = [1, "str", [1, 2, 3]] # sub-list is also allowed

sublist = [2 ,4 ,3, 4]
# lst_ = [1, "str", sublist] # This ways is allowed as well

# print(lst_)
# print(lst_[0]) # 0 means the first one, so 1 is the second one
# print(lst_[0:2]) # lst[start: stop: step]

# lst_int = [i for i in range(0, 10)]
# print(lst_int[0: 10: 2])
# print(lst_int[0: 10: 3])
# print(lst_int[:4])
# print(lst_int[2:])

# Add more value
# sublist.extend([2,7])
# sublist.append([10])
# sublist.append(10) # Check the difference between this one and the last one
# sublist.insert(2,100) # insert a values after the second values

# Delete value
# sublist.pop(1) # remove the second number, since 0, 1, 2
# sublist.remove(4) # remove a number that its value is 4, which is the first "4" in the list, but not the other "4"

# print(sublist)

# lst__ = []
# for i in range(5):
#     num = int(input("Please input a number: "))
#     lst__.append(num)
# print(lst__)

lst_string = "Python"
print(lst_string[2:5])
# sublist.append(lst_string)
# sublist.extend(lst_string) # Check the difference between this line and the last line
print(sublist)

sublist[1] = 200 # Change the second number 4 to 200
print(sublist)

food = ["rice", "beans"]
food.append("brocoli")
food.extend(["seafood"])
print(food)
# food[:2]
# food[:2][1]
# food[:2][1][:3]
# food[-1] # Show the last one only, which is same with food[3]

strs = "eggs,fruit,orange,juice"
print(len(strs))
breakfast = strs.split(",")
print(breakfast)
print(len(breakfast))

lengths = [len(items) for items in breakfast] # show the length of each items
print(lengths)

breakfastlist = [item[0] for item in breakfast] # Make the first character of each item to create a new list
breakfastlist_ = [item[-1] for item in breakfast] # Make the last character of each item to create a new list
print(breakfastlist)
print(breakfastlist_)

breakfast_ = breakfast[:] # The solution how to copy a existing list
print(breakfast_)
