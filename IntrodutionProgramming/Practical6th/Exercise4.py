temp = []
number = 1
while number == 1:
    str = input("Please input your message, white space is for break: ")
    for item in range(len(str)):
        if str[item] == "X":
            num = ord(str[item]) - 23
            mess = chr(num)
            temp.append(mess)
            #message = ''.join(temp)
        elif str[item] == "Y":
            num = ord(str[item]) - 23
            mess = chr(num)
            temp.append(mess)
            #message = ''.join(temp)
        elif str[item] == "Z":
            num = ord(str[item]) - 23
            mess = chr(num)
            temp.append(mess)
            #message = ''.join(temp)
        elif str[item] == " ":
            number = 0
            break
        else:
            num = ord(str[item]) + 3
            mess = chr(num)
            temp.append(mess)
        message = ''.join(temp)

print(message)


# input:
# ABCD
# XYZ" "
# output:
# DEFGABC
# Can be updated
