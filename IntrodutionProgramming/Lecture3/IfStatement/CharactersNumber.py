# input some words, and recognize with 5

words = input("Please input some words: ")
length = len(words)
if length > 5:
    print("The number of characters are greater than 5.")
elif length < 5:
    print("The number of characters are smaller than 5.")
else:
    print("The number of characters are 5.")
