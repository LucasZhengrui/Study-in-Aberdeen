# input the number of items that you want to buy, and print specific discounts.

itemsnum = int(input("Please enter the number of items you want to buy: "))
if itemsnum < 10:
    print("You will receive 0 discounts, sorry!")
elif itemsnum >= 10 and itemsnum <= 19:
    print("You will receive 20 percent discounts, congrats!")
elif itemsnum >= 20 and itemsnum < 30:
    print("You will receive 30 percent discounts, keep going!")
elif itemsnum >= 30:
    print("You will receive 50 percent discounts, appreciate!")
