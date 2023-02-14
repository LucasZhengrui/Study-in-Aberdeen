def leadyear(year):
    if((year%4 == 0 and year%100 != 0) or year%400 == 0):
        print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year.")

year_ = int(input("Please input the year: "))
leadyear(year_)