string_ = "Introduction of Python Programming" # string
new_string = string_.split(" ") # change string to list
new_list = []
print(new_string)
for i in new_string:
    new_list.append('$' + i[1:])
x = ' '.join(new_list) # change list back to string

print(x)

# Result is "$ntroduction $f $ython $rogramming"
