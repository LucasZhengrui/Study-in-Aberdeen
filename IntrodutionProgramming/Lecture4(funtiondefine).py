def funtion1(x):
    print("Hello world!")
    return None

def add(a,b):
    """
    Here is a funtion to caculate 2 value.
    """
    c = a + b
    return c

def cube(x):
    """
    Raise the number to the third power.
    """
    z = pow(x,3)
    return z

def cubefree(x,y):
    """
    Raise the number to the third power.
    """
    z = pow(x,y)
    return z

def greet(name):
    """
    Print Hello <name> after you input your name
    """
    # x = str(input("Please input your name: "))
    print("Hello " + name + "!")

guesses = 0

def CheckGuess(aGuess):
    global guesses # Attention: The differences between global variable and local variable.
    guesses = guesses + 1
    # return guesses

aGuess = int(input("Please input"))
print(CheckGuess(aGuess))
print(guesses)

# Just a test
sum = add(2,4)
print(sum)

# Show some number's power
v = int(input("Please input a number: "))
w = int(input("Please input how many power you want to caculate"))
power = cube(v)
powerfree = cubefree(v,w)
print(power)
print(powerfree)

x = str(input("Please input your name: "))
print(greet(x))
