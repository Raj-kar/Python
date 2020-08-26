from password_checker import check_strength


def take_user_fName():
    while True:
        user_fName = input("Enter your first name :: ")
        try:
            type(int(user_fName)) == int
        except Exception as e:
            # print(e)
            if len(user_fName) < 3:
                print("minimum 3 alphabetic first name required !")
            else:
                user_fName = "".join(user_fName.split(" "))
                return user_fName
        else:
            print("only numeric digit not allowed on name !")


def take_user_lName():
    while True:
        user_lName = input("Enter your last name :: ")
        try:
            type(int(user_lName)) == int
        except Exception as e:
            # print(e)
            if len(user_lName) < 3:
                print("minimum 3 alphabetic last name required !")
            else:
                user_lName = "".join(user_lName.split(" "))
                return user_lName
        else:
            print("only numeric digit not allowed on name !")


def take_user_email():
    while True:
        user_email = input("Enter your email address :: ").lower()
        try:
            type(int(user_email)) == int
        except Exception as e:
            # print(e)
            if len(user_email) <= 10:
                print("Enter a valid email !")
            elif not any([True if x == "@" else False for x in user_email]):
                print("Not a valid email ! must containing @ !")
            elif not any([True if x == "." else False for x in user_email]):
                print("Not a valid email ! must containing '.' !")
            else:
                user_email = "".join(user_email.split(" "))
                return user_email
        else:
            print("only numeric digit not allowed on email !")


def take_user_password():
    while True:
        user_password = input("Enter a secure password :: ")
        try:
            type(int(user_password)) == int
        except Exception as e:
            strength = check_strength(user_password)
            if strength:
                return user_password
            else:
                print("enter a strong password ! ")
        else:
            print("only numeric digit not allowed on password !")


# fName = take_user_fName()
# lName = take_user_lName()
# email = take_user_email()
# password = take_user_password()

# print("New User Created !")
# print(
#     f"Name = {fName} {lName}\n"
#     f"Email = {email}\n"
#     f"Password = {password}\n"
# )
