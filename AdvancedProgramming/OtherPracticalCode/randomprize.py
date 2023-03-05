from random import randrange

min_number = 1
max_number = 49
num_number = 6

ticket_number = []

for i in range(num_number):
    rand = randrange(min_number, max_number)
    while rand in ticket_number:
        rand = randrange(min_number, max_number)
    ticket_number.append(rand)

ticket_number.sort()
print("Your numbers are: ", end = "")
for n in ticket_number:
    print(n, end = "")
print()