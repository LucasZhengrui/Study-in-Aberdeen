import time

def is_prime(num): # prime is the number that it can only be division by itself and 1
    if num == 0 or num == 1:
        return False
    elif num < 0:
        print("Error")
        return None
    else:
        for item in range(2, num):
            if num % item == 0:
                return False
        return True

'''
if __name__ == "__main__":
    t0 = time.time() # Caculate the time using to run the code
    try:
        num = int(input("Please input a number: "))
        print(is_prime(num))
    except:
        print("Input an invalid number.")
    t1 = time.time()
    print("Using time: ", t1 - t0)
'''

list = []
num = int(input("Please input a number: "))
for item in range(2, num + 1):
    if is_prime(item):
        list.append(item)
print(list)
# same with 'list[item for item in range(2, num) if is_prime(item)]'
