import random
num1 = random.randint(0,999)
num2 = random.randint(0,999)
print(num1 + num2)
guess = int(input("Please enter a number that you guess is it the adding result of these two number, your value is: "))
if guess == num1 + num2:
    print("Congrats! You're right!")
else:
    print("Please try again!")
