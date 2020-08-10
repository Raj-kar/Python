# If speed is less than 70, it should print “Ok”.
# Otherwise, for every 5km above the speed limit (70),
# it should give the driver one demerit point and print the total number of demerit points.
# For example, if the speed is 80, it should print: “Points: 2”.
# If the driver gets more than 12 points, the function should print: “License suspended”


def demerit_point(speed):
    init_point = 5
    driver_point = speed//init_point
    print(f"Points {driver_point}")
    if(driver_point > 12):
        print("License suspended")


def speed_checker(speed):
    if speed <= 74:
        print("Ok")
    else:
        demerit_point(speed - 70)


speed_checker(80)
print()
speed_checker(200)
print()
speed_checker(67)
