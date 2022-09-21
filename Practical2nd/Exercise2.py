# freely type words repeatedly

words = input("Please input some words that you want to describe: ")
num = int(input("Please input the number that you want to repeat your words: "))
msg = "Here are your words: " + "'" + words + "'" + "\n"
print(num*msg)
