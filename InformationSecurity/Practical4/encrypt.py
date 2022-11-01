def encrypt(text, s):
    # result = []
    result_str=''
    # transverse the plaintext
    for i in range(len(text)):
        char = text[i]
        # Encrypt uppercase characters in plaintext
      
        if char.upper: # isupper() is Verifying whether the characters are all of upper letters
            result_str += chr((ord(char) - 97 + s) % 26 + 97) # ord() is transfer characters to their ASCII code number, the reverse is chr()
        # Encrypt lowercase characters in plaintext
        else:
            result_str +=  chr((ord(char) - 65 + s) % 26 + 65)
    return result_str

#check the above function
text = input("Please input your CEASER CIPHER DEMO: ")
s = int(input("Please input the shift pattern number: "))

print("PlainText", text)
print("Shift pattern: ", s)
print("Cipher: ", encrypt(text, s))
