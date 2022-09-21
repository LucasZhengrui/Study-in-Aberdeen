# Main Exercise: 

# Exercise 3: Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old. Note: for this exercise,the expectation is that you explicitly write out the year (and therefore be out of date the next year).
# Exercise 4: Print out that 5 copies of the message of the program in Exercise 3 on separate lines. 
# Exercise 5: Add on to the program in Exercise 3 by asking the user for another number and printing out thatmany copies of the previous message.

name = input("What is your name: ")
age = int(input("How old are you: "))
num = int(input("Enter a number: "))
year = 2022 - age + 100
msg = name + ", you will be 100 years old in the year " + str(year) +"\n"
print(msg*num)
