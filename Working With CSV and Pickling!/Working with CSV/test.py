from csv import reader,writer

with open("fighters.csv") as file:
	csv_data = reader(file)
	with open("newFile.csv", "w") as file2:
		csv_writer = writer(file2)
		for data in csv_data:
			csv_writer.writerow([d.upper() for d in data])


	

	