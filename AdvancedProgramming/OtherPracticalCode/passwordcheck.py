def password(psd):
    upper = False
    lower = False
    num = False
    for p in psd:
        if p <= "Z" and p >= "A":
            upper = True
        elif p <= "z" and p >= "a":
            lower = True
        elif p <= "9" and p >= "0":
            num = True
    if len(psd) >= 8 and upper and lower and num:
        return True
    return False

def main():
    a = 0
    while(1):
        pd = input("Please input your password to check: ")
        if password(pd):
            print("Great password!")
            break
        else:
            print("Please try to think about another one.")
            continue

main()