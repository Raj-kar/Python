# Write a Python program to find those numbers which are divisible by 7 and multiple of 5,
# between 1500 and 2700 (both included).

divisible = lambda num : print(num, end=" ") if num % 7 == 0 and num % 5 == 0 else False

for i in range(1500,2701):
	divisible(i)


# 1505 1540 1575 1610 1645 1680 1715 1750 1785 1820 1855 1890 1925 1960 1995 2030 2065
# 2100 2135 2170 2205 2240 2275 2310 2345 2380 2415 2450 2485 2520 2555 2590 2625 2660 2695


# There are also many other possible way, for doing this. you can also use list comprihansion.