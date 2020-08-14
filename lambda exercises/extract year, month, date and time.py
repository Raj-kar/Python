# Write a Python program to extract year, month, date and time using Lambda.

import datetime

now = datetime.datetime.now()


year = lambda y: y.year
month = lambda m: m.month
day = lambda d: d.day
time = lambda t: t.time()


print(year(now))
print(month(now))
print(day(now))
print(time(now))


