# 5/2/10 (DD/MM/YY) is a magic date, which mean that 5*2 == 10, that's why it's a magic date. PS. Please input a 2-digit year number, like 2010 is 10.
# Write a function to check if it's a magic date.

def CheckMagicDate(day,month,year):
    if day*month == year:
        print("True, it's a magic date.")
    else:
        print("Badluck, it's not a magic date, sorry!")

day = int(input("Please input day of the date: "))
month = int(input("Please input month of the date: "))
year = int(input("Please input year(2-digit) of the date: "))
print("The date you input is ",day,"/",month,"/",year)
CheckMagicDate(day,month,year)
