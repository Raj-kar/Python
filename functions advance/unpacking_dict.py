# 1st example


def greetings(first, second):
    print(first + " greets " + second)


# greetings("Raj", "Rahul")

names = {"first": "Raj", "second": "Rahul"}
greetings(**names)  # unpack the dict


# 2nd example

def calculate(num1, num2, num3):
    print(num1+num2*num3)

calculate(1, 2, 3)  # noraml pass values

nums = dict(num1=1,num2=2,num3=3)

calculate(**nums)	# unpacking and pass te values 


# we can also pass **kwargs or other variables , example :-

def calculate_2(num1, num2, num3,**kwargs):
    print(num1+num2*num3)
    print(".... print kwargs")
    print(kwargs)

# calculate(1, 2, 3)  # noraml pass values

nums = dict(num1=1,num2=2,num3=3,name="Raj",id=1,marks=85)

calculate_2(**nums)	