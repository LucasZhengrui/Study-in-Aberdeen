#

year = int(input("Please input the year you want to check: "))
month = input("Please input the month you want to check: ")
if (year%4 == 0 and year%100 != 0) or year%400 == 0:
    if month == "feb":
        print("There are 29 days.")
    elif month == "jan" or month == "mar" or month == "may" or month == "jul" or month == "aug" or month == "oct" or month == "dec":
        print("There are 31 days.")
    elif month == "apr" or month == "jun" or month == "sep" or month == "nov":
        print("There are 30 days only.")
    else:
        print("Check your month, is it correct?")
else:
    if month == "feb":
        print("There are 28 days only.")
    elif month == "jan" or month == "mar" or month == "may" or month == "jul" or month == "aug" or month == "oct" or month == "dec":
        print("There are 31 days.")
    elif month == "apr" or month == "jun" or month == "sep" or month == "nov":
        print("There are 30 days only.")
    else:
        print("Check your month, is it correct?")
