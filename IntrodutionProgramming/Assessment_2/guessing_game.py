'''
Write a program called “guessing_game” without arguments that generates a random number
between 1 and 100, inclusive. Ask the user to guess the number in a loop until they get it right,
advising whether the number is too big or too small. You should also keep track of the number
of guesses the user has made. The function should output the following:
>>>That's not right, g is too small/big (if wrong, where g is the guess)
>>>That's right! You took n guess(es) (if correct, where n is the number of guesses).
For this task, you can import and use 'random.randint'. (10 Marks)
'''

import random
def random_num():
    num = random.randint(1,100)
    return num

item = 0
num = random_num()
# print(num) # Just for testing the program
while True:
    guessing_num = int(input("Please guessing and inputing a number(n): "))
    if guessing_num == num:
        item += 1
        print("That's right! You took", item, "guess(es)")
        break
    elif guessing_num < num:
        item += 1
        print("That's not right!", guessing_num, "is too small")
    else:
        item += 1
        print("That's not right!", guessing_num, "is too big")
