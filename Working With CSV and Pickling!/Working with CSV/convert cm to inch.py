from csv import DictReader, DictWriter


def cm_to_inch(cm):
    return round(int(cm) * 0.393701, 2)


with open("fighters.csv") as file:
    csv_reader = DictReader(file)
    headers = ["Name", "Country", "Height"]
    with open("newDict.csv", "w") as f:
        csv_writer = DictWriter(f, fieldnames=headers)
        csv_writer.writeheader()
        for data in csv_reader:
            csv_writer.writerow({
                "Name": data['Name'],
                "Country": data['Country'],
                "Height": cm_to_inch(data['Height (in cm)'])
            })

# Another easy method [but it can't changes the header names]

with open("fighters.csv") as file:
    csv_reader = DictReader(file)
    headers = ["Name", "Country", "Height (in cm)"]
    with open("newDict_simple.csv", "w") as f:
        csv_writer = DictWriter(f, fieldnames=headers)
        csv_writer.writeheader()
        for data in csv_reader:
            data['Height (in cm)'] = str((cm_to_inch(list(data.values())[2])))
            csv_writer.writerow(data)
