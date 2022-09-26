# Input 5 numbers and caculate their total value

total = 0
for i in range(5):
    num = int(input("Please enter a number: "))
    total = total + num
print(total)

# Print the multiple of 5 until 100

for i in range(5,101):
    if i % 5 == 0:
        print(i)
