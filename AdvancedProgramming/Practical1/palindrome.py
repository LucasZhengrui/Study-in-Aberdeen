word = str(input("Please input a word: "))
print(len(word))


def pali(text):
    return (text == text[::-1])  # To check a word is it like "aba, level"
print(pali(word))
