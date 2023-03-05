word = str(input("Please input a word: "))
print(len(word))


def pali(text):
    return (text == text[::-1])
print(pali(word))
