import re


def enter_email():
    user_email = input("Enter your email address :: ")
    pattern = re.compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")

    match = pattern.search(user_email)
    if match:
        print("valid Email ..!")
    else:
        print("invalid Email ..!")


enter_email()
