from password_checker import check_strength


def take_user_name(state):
    while True:
        user_name = input(f"Enter your {state} name :: ")
        try:
            type(int(user_name)) == int
        except Exception as e:
            # print(e)
            if len(user_name) < 3:
                print(f"minimum 3 alphabetic {state} name required !")
            else:
                user_name = "".join(user_name.split(" "))
                return user_name
        else:
            print("only numeric digit not allowed on name !")



def take_user_fName():
    return take_user_name("first")


def take_user_lName():
    return take_user_name("last")


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


# for check validation !

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
