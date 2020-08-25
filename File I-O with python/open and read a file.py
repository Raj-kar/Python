f = open("story.txt")  # for open file

print(f.read())  # read content from file

f.seek(0)  # move courser to 0 place

f.seek(12)  # move courser to 10th place

print(f.readline())  # read single line at a time
# now courser at 2nd line
print(f.readlines())  # read all lines and return the lines as a list

print(f.readline())  # read single line at a time
# now courser at 2nd line
f.seek(0)
# move courser to position zero
print(f.readlines())  # read all lines and return the lines as a list

f.close()  # we have to manually close the file, after we reads !

# f.read()    # thrown a ValueError


# Run this file to show the outputs !
