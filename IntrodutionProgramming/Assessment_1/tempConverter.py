'''
Write a program called 'tempConverter.py' to convert temperatures to and from Celsius,
Fahrenheit. To accomplish this, you need to create the following two functions that accept a
temperature degree as the only argument:
celToFah(temperature)
FahToCel(temperature)
In addition, you need to create another function called mainProgram() that asks the user for a
temperature scale (1 for Celsius and 2 for Fahrenheit) and returns the converted temperature to
the user. (15 Marks)
For example, if the user selects Celsius as the input temperature scale, the output would be:
>>> The temperature xxx in Celsius is equivalent to xxx in Fahrenheit.
Similarly, if the user selects Fahrenheit as the input temperature scale, the output would be:
>>> The temperature xxx in Fahrenheit s equivalent to xxx in Celsius.


From Google:
How to convert: C = 5/9(F - 32)
'''

def celToFah(temperature):
    Ftemperature = (temperature/5)*9 + 32
    return Ftemperature

def fahToCel(temperature):
    Ctemperature = (5/9)*(temperature - 32)
    return Ctemperature

mode = int(input("Please input which mode of degree you want to select (1 is for celsius or 2 is for fahrenheit): "))
temp = int(input("Please input the temperature you want to convert: "))
if mode == 1:
    contemp = celToFah(temp)
    print("The temperature", temp, "in Celsius is equivalent to", contemp, "in Fahrenheit.")
elif mode == 2:
    contemp = fahToCel(temp)
    print("The temperature", temp, "in Fahrenheit is equivalent to", contemp, "in Celsius.")
else:
    print("Input error. Please check!")
