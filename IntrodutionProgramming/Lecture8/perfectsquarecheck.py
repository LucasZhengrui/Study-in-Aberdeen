# The title is https://i.imgur.com/2cyPWOQ.png

def bin_search(num):
    low = 0
    high = num
    while True:
        mid = (low + high) // 2 # In order to make sure that mid is int
        if mid**2 == num:
            return mid
        elif mid**2 > num:
            high = mid
        else: # mid**2 < num
            low = mid
        if high - low <= 1:
            if high == low:
                return low
            else:
                h1 = abs(high**2 - num) # absolute value
                l1 = abs(low**2 - num)
                if h1 < l1:
                    return high
                else:
                    return low

print(bin_search(70))
