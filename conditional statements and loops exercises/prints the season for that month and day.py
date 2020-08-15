# Write a Python program that reads two integers representing a month and day,
# and prints the season for that month and day.

month = input("Input the month:: ").lower()
day = int(input("Input the day:: "))

alert = "Wrong Input ... :)"
season = None

def days31(month): return True if(day > 0 and day <=
                                  31) else print(alert)


def days30(month): return True if(day > 0 and day <=
                                  30) else print(alert)


if(month in ("december", "january")):
    if(days31(month)):
        season = "Winter"

elif(month == "february"):
    if(day > 0 and day <= 29):
        season = "Spring"
    else:
        print("alert")

elif(month == "march"):
    if(days31(month)):
        season = "Spring"

elif(month in ("april", "june")):
    if(days30(month)):
        season = "Summer"

elif(month == "may"):
    if(days31(month)):
        season = "Summer"

elif(month in ("july", "august")):
    if(days31(month)):
        season = "Monsoon"

elif(month == "september"):
    if(day >= 0 and day <= 15):
        season = "Monsoon"
    elif(day > 15 and day <= 30):
        season = "Autumn"
    else:
        print("alert")

elif(month == "october"):
    if(days31(month)):
        season = "Autumn"

elif(month == "november"):
    if(days30(month)):
        season = "Autumn"

else:
    print(alert)
    exit()							# program end here if exit() called

print("Season is",season)



# for input validation the program is looking big, but in realm It's so simple ..
# you can also add NULL input validation , or only the month the correct then only
# you show the date input box ...!! you can add  many validation as you needed :) .