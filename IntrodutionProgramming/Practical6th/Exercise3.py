# How to display using two decimal places:
# float = 2.154327
# format_float = "{:.2f}".format(float)
# print(format_float)

def cost(age):
    if age <= 2:
        cost = 0.00
    elif age >= 3 and age <= 12:
        cost = 14.00
    elif age >= 65:
        cost = 18.00
    else:
        cost = 23.00
    return cost

total = 0
while 1:
    age = input("Please input the age of visitor(type " " is for stoping4): ")
    if age != " ":
        yearsold = int(age)
        costing = cost(yearsold)
        costing_float = "{:.2f}".format(costing)
        print("The age is", age, "so the cost of him or her is", costing_float)
    else:
        break
    total = total + costing

total_float = "{:.2f}".format(total)
print(total_float)
