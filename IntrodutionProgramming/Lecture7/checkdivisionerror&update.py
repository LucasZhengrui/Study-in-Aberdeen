def div(x,y):
    if y == 0:
        return None
    else:
        return x/y

def div2(x,y):
    try:
        return x/y
    except:
        print("there is error")
        return None

result1 = div(3, 0)
print(result1)
result = div2(3, 0)
print(result)
