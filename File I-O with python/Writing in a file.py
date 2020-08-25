# w - stands for write on file
# If no fill is there, it will automatically create one
# w overwrite all the previous things !

with open("story2.txt", "w") as file:
    file.write("this is a new line \n")
    file.write("we can wrote multiple line Here ! \n")
    file.write("file will be closed automatically also !\n")
    file.write("great right ! \npower of Python ")

with open('story.txt', "w") as f:
    f.write("this file is now open \n")
    f.write("whatever we write now, it'll replaced the\n")
    f.write("original file \n")

with open('lol.txt', "w") as f:
    f.write("\n")
    f.write("haha" * 1000)

# a - stands for append  on file
# If no fill is there, it will automatically create one
# a add all the new things after previous things !
# It's add all the thing always after the previous staffs !


with open('story.txt', "a") as f:
    f.write("\n")
    f.write("this file is now open \n")
    f.write("whatever we write now, it'll append on the\n")
    f.write("original file \n")
    f.write("no previous data will be lost ! :)")
