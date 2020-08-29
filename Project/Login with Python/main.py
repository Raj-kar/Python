from csv import reader, writer

from input_validation import take_user_fName, take_user_lName, take_user_email, take_user_password
from login_account import user_login


def create_user(is_header):
    if is_header and is_header != 2:
        search_user()
    elif is_header == 2 or is_header == 0:
        with open("test_data.csv", "a", newline='') as file:
            csv_writer = writer(file)
            headers = ["fName", "lName", "email", "password"]
            if not is_header:
                csv_writer.writerow(headers)
            csv_writer.writerow(current_user)
            print("New account Created !")


def password_strength(password):
    if len(password) < 8:
        return False


def search_user():
    with open("test_data.csv") as file:
        users = list(reader(file))
        for saved_user in users:
            if saved_user != ['fName', 'lName', 'email', 'password']:
                if saved_user[2] == current_user[2]:
                    print("email account already exits !")
                    return

        create_user(2)


# display menu
print("----- Menu ------")
print("1. Create a new account  ")
print("2. Login to an account  ")
user_choice = input("Enter your choice(1,2) : ")

if user_choice == '1':
    user_fName = take_user_fName()
    user_lName = take_user_lName()
    user_email = take_user_email()
    user_password = take_user_password()
    current_user = [user_fName, user_lName, user_email, user_password]
elif user_choice == '2':
    user_login()
else:
    print("Wrong choice !")
    exit()


# check already have data or not
def flag():
    return 1 if csv_reader else 0


with open("test_data.csv") as file:
    csv_reader = list(reader(file))
    flag = flag()
    create_user(flag)
