from csv import reader

# Manually read
with open("fighters.csv") as csv:
    data = csv.read()

data = data.split("\n")

for i in data:
    print((i.split(",")))

print()
# Using reader from csv

with open("fighters.csv") as file:
    csv_data = reader(file)
    for data in csv_data:
        print(data)

print()
# for skip the heading
with open("fighters.csv") as file:
    csv_data = reader(file)
    next(csv_data)
    for data in csv_data:
        print(data)

print()
# for get the file as a
with open("fighters.csv") as file:
    csv_data = reader(file)
    print(list(csv_data))

print()
# for access different property
with open("fighters.csv") as file:
    csv_data = reader(file)
    next(csv_data)
    for data in csv_data:
        print(f"{data[0]} from {data[1]}")

# outputs
# ['Name', 'Country', 'Height (in cm)']
# ['Ryu', 'Japan', '175']
# ['Ken', 'USA', '175']
# ['Chun-Li', 'China', '165']
# ['Guile', 'USA', '182']
# ['E. Honda', 'Japan', '185']
# ['Dhalsim', 'India', '176']
# ['Blanka', 'Brazil', '192']
# ['Zangief', 'Russia', '214']
# ['Raj', 'India', '196']
#
# ['Name', 'Country', 'Height (in cm)']
# ['Ryu', 'Japan', '175']
# ['Ken', 'USA', '175']
# ['Chun-Li', 'China', '165']
# ['Guile', 'USA', '182']
# ['E. Honda', 'Japan', '185']
# ['Dhalsim', 'India', '176']
# ['Blanka', 'Brazil', '192']
# ['Zangief', 'Russia', '214']
# ['Raj', 'India', '196']
#
# ['Ryu', 'Japan', '175']
# ['Ken', 'USA', '175']
# ['Chun-Li', 'China', '165']
# ['Guile', 'USA', '182']
# ['E. Honda', 'Japan', '185']
# ['Dhalsim', 'India', '176']
# ['Blanka', 'Brazil', '192']
# ['Zangief', 'Russia', '214']
# ['Raj', 'India', '196']
#
# [['Name', 'Country', 'Height (in cm)'], ['Ryu', 'Japan', '175'], ['Ken', 'USA', '175'], ['Chun-Li', 'China',
# '165'], ['Guile', 'USA', '182'], ['E. Honda', 'Japan', '185'], ['Dhalsim', 'India', '176'], ['Blanka', 'Brazil',
# '192'], ['Zangief', 'Russia', '214'], ['Raj', 'India', '196']]
#
# Ryu from Japan
# Ken from USA
# Chun-Li from China
# Guile from USA
# E. Honda from Japan
# Dhalsim from India
# Blanka from Brazil
# Zangief from Russia
# Raj from India