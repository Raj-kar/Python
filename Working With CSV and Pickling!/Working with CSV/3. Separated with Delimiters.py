# how to read the files that separated with ";" or "$" or "|" any other symbols [delimiters]
# using here fighters2.csv as example

from csv import reader

with open("fighters2.csv") as file:
    csv_data = reader(file, delimiter="|")
    for data in csv_data:
        print(data)

# Output

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
