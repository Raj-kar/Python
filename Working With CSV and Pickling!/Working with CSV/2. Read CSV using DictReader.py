from csv import DictReader

with open("fighters.csv") as file:
    csv_data = DictReader(file)
    for data in csv_data:
        print(data)

print()
# we can access the data by using keys

with open("fighters.csv") as file:
    csv_data = DictReader(file)
    for data in csv_data:
        print(f"{data['Name']}'s height {data['Height (in cm)']}")

# Outputs !

# {'Name': 'Ryu', 'Country': 'Japan', 'Height (in cm)': '175'}
# {'Name': 'Ken', 'Country': 'USA', 'Height (in cm)': '175'}
# {'Name': 'Chun-Li', 'Country': 'China', 'Height (in cm)': '165'}
# {'Name': 'Guile', 'Country': 'USA', 'Height (in cm)': '182'}
# {'Name': 'E. Honda', 'Country': 'Japan', 'Height (in cm)': '185'}
# {'Name': 'Dhalsim', 'Country': 'India', 'Height (in cm)': '176'}
# {'Name': 'Blanka', 'Country': 'Brazil', 'Height (in cm)': '192'}
# {'Name': 'Zangief', 'Country': 'Russia', 'Height (in cm)': '214'}
# {'Name': 'Raj', 'Country': 'India', 'Height (in cm)': '196'}
#
# Ryu's height 175
# Ken's height 175
# Chun-Li's height 165
# Guile's height 182
# E. Honda's height 185
# Dhalsim's height 176
# Blanka's height 192
# Zangief's height 214
# Raj's height 196
