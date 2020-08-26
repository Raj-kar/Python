from csv import DictWriter

with open("DictFile.csv", "w") as file:
    headers = ["name", "age"]
    csv_dict = DictWriter(file, fieldnames=headers)
    csv_dict.writeheader()
    csv_dict.writerow({
        "name": "Raj",
        "age": 19,
    })
    csv_dict.writerow({
        "name": "Raima",
        "age": 21
    })
