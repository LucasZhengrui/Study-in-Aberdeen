# Spell out a number. For example

#   o) 99 --> ninety nine
#   o) 300 --> three hundred
#   o) 310 --> three hundred and ten
#   o) 1501 --> one thousand, five hundred and one
#   o) 12609 --> twelve thousand, six hundred and nine
#   o) 512607 --> five hundred and twelve thousand, six hundred and seven
#   o) 43112603 --> forty three million, one hundred and twelve thousand, six hundred and three

# [Source http://rosettacode.org]

def globalconvert(number):
    if number == 1:
        return "one"
    elif number == 2:
        return "two"
    elif number == 3:
        return "three"
    elif number == 4:
        return "four"
    elif number == 5:
        return "five"
    elif number == 6:
        return "six"
    elif number == 7:
        return "seven"
    elif number == 8:
        return "eight"
    elif number == 9:
        return "nine"
    elif number == 10:
        return "ten"
    elif number == 11:
        return "eleven"
    elif number == 12:
        return "twelve"
    elif number == 13:
        return "thirteen"
    elif number == 14:
        return "fourteen"
    elif number == 15:
        return "fifteen"
    elif number == 16:
        return "sixteen"
    elif number == 17:
        return "seventeen"
    elif number == 18:
        return "eighteen"
    elif number == 19:
        return "nineteen"

num = int(input("Please input a number "))
num1 = int(num/100)
num2 = num - num1*100
num3 = int(num2/10)
num4 = num2 - num3*10
print(globalconvert(num1), "hundred", globalconvert(num3), "ty", globalconvert(num4))
   
