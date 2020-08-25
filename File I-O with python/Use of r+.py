# r+ - stands for reads and write  on file
# If no fill is there, it thrown an Error <---
# r+ can add the files whenever developer wants !
# r+ can control the courser !


with open('story3.txt', "r+") as file:
    file.write("This is the first line, of the file.  \n")
    file.write("This is the second line of the file !")
    file.seek(0)
    file.write("replace the previous \n")  # start replace char from place 0
    print(file.read())  # in r+ you can also read
    file.write("\n NEW STUFF \n")
