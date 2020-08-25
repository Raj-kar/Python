with open("story.txt") as file:
    print(file.read())
    file.seek(0)
    data = file.read()

print(data)  # print the data

# Don't need to call file.close statement ! It's already closed !
# So with statement is so popular !
