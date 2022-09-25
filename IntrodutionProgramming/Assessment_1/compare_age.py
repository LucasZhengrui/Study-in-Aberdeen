'''
Write a function called “compare_ages” without arguments that asks for the user's age and
responds by saying whether the user is the same age as you, younger or older (and by how
much). (10 Marks)
For example, if you are 18 years old the program should display on the screen the following:
• "You are one year younger than me." (if input is 17)
• "You are the same age as me." (if input is 18)
• "You are 2 years older than me." (if input is 20)
'''

def compare_ages():
    # distance = 0
    ages = int(input("Please input your own age(my ages is 22 years old(2000)): "))
    if ages < 22:
        # distance == 22 - ages
        print("You are", 22 - ages, "year(s) younger than me.")
    elif ages == 22:
        print("You are the same age as me.")
    else:
        # distance == ages - 22
        print("You are", ages - 22, "year(s) older than me.")

compare_ages()
