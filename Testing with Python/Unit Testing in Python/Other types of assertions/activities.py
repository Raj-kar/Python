def eat(name, is_healthy):
	if not isinstance(is_healthy, bool):
		raise ValueError("must need bool type !")
	end = "because YOLO"
	if is_healthy:
		end = "because life a temple"
	return f"I eat {name}, {end}"


def nap(time):
	end = "make me more lazy"
	if time == 1:
		end = "make me free"
	return f"sleep for {time} hour, {end}"

def walk(km):
	end = "Ok that's too low"
	if km >= 5:
		end = "Ok that's too much"
	return f"I just walk {km} km, {end}"

def is_funny(person):
	if person == "Rahul":
		return False
	return True

from random import choice
def laugh():
	return choice(("haha","lol","tehehe"))

def even_numbers(num):
	if num not in (2,4,6,8,10):
		return False
	return True

