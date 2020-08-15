# Write a Python program to display astrological sign for given date of birth.

# Expected Output:
# Input birthday: 15
# Input month of birth (e.g. march, july etc): may
# Your Astrological sign is : Taurus

date = int(input("Enter birthday date :: "))
month = input("Enter birthday month :: ").lower()

astrological = None


def verify_date(lb, ub): return True if date >= lb and date <= ub else False


if(month in("march", "april")):
    if(month == "march"):
        if(verify_date(21, 31)):
            astrological = "Aries"
    else:
        if(verify_date(1, 19)):
            astrological = "Aries"

if(month in ("april", "may")):
    if(month == "april"):
        if(verify_date(20, 30)):
            astrological = "Tarus"
    else:
        if(verify_date(1, 20)):
            astrological = "Tarus"

if(month in ("may", "june")):
    if(month == "may"):
        if(verify_date(21, 31)):
            astrological = "Gemini"
    else:
        if(verify_date(1, 21)):
            astrological = "Gemini"
            

            # ...continue !
            	#refarance :: http://www.astromax.org/con-page/con-12.htm


print(f"Your Astrological sign is : {astrological}")
