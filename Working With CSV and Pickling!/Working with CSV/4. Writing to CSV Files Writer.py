from csv import writer

with open("test.csv", "w") as file:
    csv_writer = writer(file)
    csv_writer.writerow(["Name", "Age"])
    csv_writer.writerow(["Blue", 3])
    csv_writer.writerow(["kitty", 1])
    csv_writer.writerow(["moy", 2])
    csv_writer.writerow(["rick", 4])
