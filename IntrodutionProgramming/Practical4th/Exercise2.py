# Test whether it is correct about the Fermat's Last Theorem(a**n + b**n == c**n cannot be found) #useful-link: https://en.wikipedia.org/wiki/Fermat%27s_Last_Theorem

def CheckFermat(a,b,c,n):
    if a**n + b**n == c**n:
        print(a,"**",n," + ",b,"**",n," == ",c,"**",n)
        print("Holy smokes, Fermat was wrong!")
    else:
        print(a,"**",n," + ",b,"**",n," != ",c,"**",n)
        print("No, that doesn't work.")

n = int(input("Please input a value of n that greater than 2: "))
a = int(input("Now, please input a value of a: "))
b = int(input("Now, it's turn for b: "))
c = int(input("Finally, it's turn for c: "))
CheckFermat(a,b,c,n)
