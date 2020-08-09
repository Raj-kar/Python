from random import randint

# def coin_flip():
# 	ran = randint(1,2)
# 	if ran == 1:
# 		return "Head"
# 	else:
# 		return "Tail"

# short version
def coin_flip():
	if randint(1,2) == 1:
		return "Head"
	else:
		return "Tail"

print(coin_flip())