user_input = input("Enter the secret password for Close the Loop:: ").lower()

while user_input != "master":
	print("Wrong password ..!")
	user_input = input("Enter the secret password :: ").lower()
print("Welcome master")