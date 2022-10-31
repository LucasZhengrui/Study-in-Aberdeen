message = input("Please input some words that you want to input: ")
translated = '' #ciphertext is stored in this variable
i = len(message) - 1

while i >= 0:
   translated = translated + message[i]
   i = i - 1
print("The ciphertext is : ", translated)
