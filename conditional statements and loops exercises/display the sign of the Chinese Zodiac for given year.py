# Write a Python program to display the sign of the Chinese Zodiac for given year,
# in which you were born. Go to the editor

# Expected Output:
# Input your birth year: 1973
# Your Zodiac sign : Ox

year = int(input("Enter your birth year: "))

zodiac = None

if year % 12 == 4:
	zodiac ="Rat"
elif year % 12 == 5:
	zodiac = "Ox"
elif year % 12 == 6:
	zodiac = "Tiger"
elif year % 12 == 7:
	zodiac = "Rabbit"
elif year % 12 == 8:
	zodiac = "Dragon"
elif year % 12 == 9:
	zodiac = "Dragon"
elif year % 12 == 10:
	zodiac = "Horse"
elif year % 12 == 11:
	zodiac = "Goat"
elif year % 12 == 0:
	zodiac = "Monkey"
elif year % 12 == 1:
	zodiac = "Rooster"
elif year % 12 == 2:
	zodiac = "Dog"
elif year % 12 == 3:
	zodiac = "Pig"
else:
	zodiac = "Invalid Input ....! :)"

print(f"Your Zodiac sign : {zodiac}")

