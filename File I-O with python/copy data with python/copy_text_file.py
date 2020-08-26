from csv import reader, writer

with open("copy_from_here.txt") as file:
    data = file.read()
    with open("paste_here.txt", "w") as f:
        # copy all the data from "copy_from_here.txt" and capitalized and paste to "paste_here.txt"
        f.write(data.upper())
