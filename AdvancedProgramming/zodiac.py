year = int(input("Please input a year: "))

zodiac_dic = ['Dragon', 'Snake', 'Horse', 'Sheep', 'Monkey', 'Rooster', 'Dog', 'Pig', 'Rat', 'Ox', 'Tiger', 'Hare']
print(zodiac_dic[(year-2000)%12])
