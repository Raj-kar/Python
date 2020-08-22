
day = int(input("Enter date :: "))
month = int(input("Enter month[1,2] :: "))
year = int(input("Enter year :: "))

month_code = None

if month in(1,10):
	month_code = 0
elif month in(2,3,11):
	month_code = 3
elif month in(4,7):
	month_code = 6
elif month == 5:
	month_code = 1
elif month == 6:
	month_code = 4
elif month == 8:
	month_code = 2
elif month in(9,12):
	month_code = 5
else:
	print("invalid month")	

remain_year = year - 1900
res = (day + month_code + remain_year + int(remain_year / 4)) % 7

date = None

if res == 0:
	date = "Sunday"
elif res == 1:
	date = "Monday"
elif res == 2:
	date = "Tuesday"
elif res == 3:
	date = "Wednusday"
elif res == 4:
	date = "Thursday"
elif res == 5:
	date = "Friday"
elif res == 6:
	date = "Saturday"
else:
	print("wrong input")

print(f"day = {date}")

