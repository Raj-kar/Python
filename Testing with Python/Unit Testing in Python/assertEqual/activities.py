def eat(name, is_healthy):
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