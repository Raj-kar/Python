# Write a Python program to get next day of a given date.

# Expected Output 1:
# Input a year: 2016
# Input a month [1-12]: 08
# Input a day [1-31]: 23
# The next date is [yyyy-mm-dd] 2016-8-24

# Expected Output 2:
# Input a year: 2000
# Input a month [1-12]: 12
# Input a day [1-31]: 31
# The next date is [yyyy-mm-dd] 2001-1-1

while True:
    try:
        year = int(input("Input a year: "))

        leapyear = True

        if year % 400 == 0:
            leapyear = True
        elif year % 100 == 0:
            leapyear = False
        elif year % 4 == 0:
            leapyear = True
        else:
            leapyear = False
    except ValueError:
        print("\n Number required, String given \n ")
    else:
        while True:
            try:
                month = int(input("Input a month [1-12]: "))

                days = 31

                if(month == 2):
                    if(leapyear):
                        days = 29
                    else:
                        days = 28
                elif(month in (1, 3, 5, 7, 8, 10, 12)):
                    days = 31
                else:
                    days = 30
            except ValueError:
                print("\n Number required, String given \n ")
            else:
                while True:
                    try:
                        day = int(input("Input a day [1-31]: "))

                        if(day < days):
                            day += 1
                        else:
                            if month == 12:
                                year += 1
                                month = 1
                                day = 1
                            elif day == days:
                                month += 1
                                day = 1

                        if(day <= days):
                            print(f"The next date is [yyyy-mm-dd] {year}-{month}-{day}")
                        else:
                            print("Invalid Input ...!")
                    except:
                        print("\n Number required, String given \n ")
                    else:
                        exit()                                              # for end the whole loop !

