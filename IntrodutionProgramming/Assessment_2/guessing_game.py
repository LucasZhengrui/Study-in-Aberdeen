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
def guessing_game():
    num = random.randint(1,100) # Gernerate a number between 1 and 100
    return num # Return the random number

item = 0
num = guessing_game() # The number is returned by the function
# print(num) # Just for testing the program
while True:
    guessing_num = int(input("Please guessing and inputing a number(n): ")) # Ask user to input the number, and it will stop after user input the correct number
    if guessing_num == num:
        item += 1 # Count how many times user use to guess
        print("That's right! It's", num, ". You took", item, "guess(es)")
        break
    elif guessing_num < num:
        item += 1 # Count how many times user use to guess
        print("That's not right!", guessing_num, "is too small")
    else: # Which mean that if guessing_num > num
        item += 1 # Count how many times user use to guess
        print("That's not right!", guessing_num, "is too big")
