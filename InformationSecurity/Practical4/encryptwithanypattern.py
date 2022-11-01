def encrypt(text):
    # result = []
    
    # transverse the plaintext
    for item in range(1,26):
        result_str=''
        for i in range(len(text)):
            char = text[i]
            # Encrypt uppercase characters in plaintext
        
            if char.upper: # isupper() is Verifying whether the characters are all of upper letters
                result_str += chr((ord(char)- 97 - item) % 26 + 97) # ord() is transfer characters to their ASCII code number, the reverse is chr()
            # Encrypt lowercase characters in plaintext
            else:
                result_str +=  chr((ord(char) - 65 - item) % 26 + 65)
        print(result_str)

#check the above function
text = input("Please input your Cipher: ")
# s = int(input("Please input the shift pattern number: "))

print("Cipher: ", text)
print("PlainText", encrypt(text))
#print("Shift pattern: ", s)
