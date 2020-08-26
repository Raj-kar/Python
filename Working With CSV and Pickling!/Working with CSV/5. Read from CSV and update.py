from csv import reader, writer

with open("fighters.csv") as file:
    csv_reader = reader(file)
    fighters = [[s.upper() for s in row] for row in csv_reader]

with open("newFile.csv", "w") as file:
    csv_writer = writer(file)
    for fighter in fighters:
        csv_writer.writerow(fighter)

# Another way

from csv import reader, writer

with open("fighters.csv") as file:
    csv_data = reader(file)
    res = [data for data in csv_data]

with open("newFile.csv", "w") as file2:
    csv_writer = writer(file2)
    for data in res:
        csv_writer.writerow(d.upper() for d in data)

# Second method

with open("fighters.csv") as file:
    csv_reader = reader(file)
    # fighters = [[s.upper() for s in row] for row in csv_reader]
    with open("newFile.csv", "w") as file:
        csv_writer = writer(file)
        for fighter in csv_reader:
            csv_writer.writerow([s.upper() for s in fighter])

# Another way
from csv import reader, writer

with open("fighters.csv") as file:
    csv_data = reader(file)
    res = [data for data in csv_data]

with open("newFile.csv", "w") as file2:
    csv_writer = writer(file2)
    for data in res:
        csv_writer.writerow(d.upper() for d in data)
