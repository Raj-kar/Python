from csv import writer, reader

print("1. Create an account")
print("2. Login to an account")

choice = 0
while True:
    choice = int(input("Enter your choice :: "))
    if choice not in (1, 2):
        print("Enter between 1 and 2")
    else:
        break

if choice == 1:
    print("-------------------")
    user_first_name = input("Enter you first name :: ")
    user_last_name = input("Enter you last name :: ")
    user_email = input("Enter you email :: ")
    user_password = input("Enter your password :: ")

    user_data = [user_first_name, user_last_name, user_email, user_password]

    with open("user_data.csv") as f:
        csv_data = reader(f)
        print(csv_data)

        with open("user_data.csv", "a") as file:
            csv_writer = writer(file)
            headers = ["fName", "lName", "email", "password"]
            csv_writer.writerow(headers)
            csv_writer.writerow(user_data)