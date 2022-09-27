string_ = "Introduction of Python Programming"
new_string = string_.split(" ")
new_list = []
print(new_string)
for i in new_string:
    new_list.append('$' + i[1:])
x = ' '.join(new_list)

print(x)
