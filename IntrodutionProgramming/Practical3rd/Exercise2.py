# Enter a letter, then recognize is it a vowel(sometimes) or not

letter = input("Please input letter in English: ")
if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
    print("Your letter is a vowel.")
elif letter == "y":
    print("Your letter is a vowel sometimes or not sometimes.")
else:
    print("Your letter is a consonant.")
