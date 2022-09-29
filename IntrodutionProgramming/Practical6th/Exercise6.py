def speed(time, distance):
    try:
        return distance/time
    except:
        print("There is an error!")
        return None

timehour = int(input("Please input how long did you use(should be hour): "))
timeminute = int(input("Please input how long did you use(should be minute): "))
distance = int(input("Please input the distance that you have went through: "))
time = timehour + timeminute/60
if time != 0:
    speed = speed(time, distance)
    print("Time in hours is", time, "and the distance in mile is", distance)
    print("The speed in mph is", speed, "mph")
else:
    speed(time, distance)
