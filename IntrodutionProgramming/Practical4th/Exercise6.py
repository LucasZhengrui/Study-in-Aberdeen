# Check if 3 lengths can make a triangle or not

def is_triangle(a,b,c):
    if a >= b + c or b >= a + c or c >= b + a:
        print("You cannot make a triangle by these 3 lengths.")
    else:
        print("You can make a triangle by these 3 lengths.")

a = int(input("Please input the first length: "))
b = int(input("Please input the second length: "))
c = int(input("Please input the third length: "))
print("Your three lengths is",a,b,c)
is_triangle(a,b,c)
