# While

num = 10
while num > 0:
    print(num)
    num = num - 1
print("finished.")

# guess a number whether it's same as a random number

import random
random_num = random.randrange(1,10)
guess = int(input("Please enter a number: "))
while random_num != guess:
    if guess < random_num:
        print("The number you guess is smaller than the random number, please try again.")
    else:
        print("The number you guess is greater than the random number, please try again.")

    guess = int(input("Please enter a number again: "))

print("Correct, congrats!")
