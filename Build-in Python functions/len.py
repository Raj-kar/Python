
print(len("Hello"))

print("Hello".__len__())	# by default all the datatypes calls __len__(), we may never call it manually.
							# this is the backend thing, that we should know

print(len([1,2,3,4])) # 4

print(len({'name':"Raj","dept":"BCA"})) # 4 

# also we can use tuple set etc ...! :)

# we can define our own function, and use len function on it.
# if you are not familier with OPP, please bear with me ..! It's just a little example !

class SpecialList:
 
    def __init__(self, data):
        self.__data = data
 
    def __len__(self):  # JUST LOOK AT THIS LINE
        return 50


l1 = SpecialList([1,40,30,100,30,1,2,3,4])
l2 = SpecialList([1,3,4,5]) 

print(len(l1)) #50
print(len(l2)) #50

