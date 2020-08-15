# Write a Python program to convert month name to a number of days.

month = ["january", "february", "march", "april", "may", "june",
         "july", "august", "september", "october", "november", "december"]

input_month = input("Input the name of Month: ").lower()

if input_month in month:
    if input_month == "february":
        print("No. of days: 28/29 days ")
    else:
        x = month.index(input_month)
        if x < 7:
            if x % 2 == 0:
                print("No. of days: 31 days ")
            else:
                print("No. of days: 30 days ")
        else:
            if x % 2 != 0:
                print("No. of days: 31 days ")
            else:
                print("No. of days: 30 days ")
else:
    print("Incorrect Month ...!")


# another easy method

month_name = input("Input the name of Month: ")

if month_name == "February":
    print("No. of days: 28/29 days")
elif month_name in ("April", "June", "September", "November"):
    print("No. of days: 30 days")
elif month_name in ("January", "March", "May", "July", "August", "October", "December"):
    print("No. of days: 31 day")
else:
    print("Wrong month name")
