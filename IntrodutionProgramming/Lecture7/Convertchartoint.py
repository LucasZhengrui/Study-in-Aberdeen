x = [1, '2', 3, '4', 5] # mixed with int and char

y = []

for item in x:
    temp = int(item) # convert all to int
    y.append(temp)
print(y)
