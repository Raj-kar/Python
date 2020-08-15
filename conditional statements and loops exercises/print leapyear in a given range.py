def leapYear(year):
    leapyear = True

    if year % 400 == 0:
        leapyear = True
    elif year % 100 == 0:
        leapyear = False
    elif year % 4 == 0:
        leapyear = True
    else:
        leapyear = False

    if(leapyear):
        print(year, end=" ")


for i in range(2000, 3001):
    leapYear(i)
