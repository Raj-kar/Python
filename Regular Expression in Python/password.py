import re


def password_strength():
    password = input("Enter your password for check strength:: ")
    pattern = re.compile(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$")

    match = pattern.search(password)
    if match:
        print("Password is strong ..!")
    else:
        print("Password is weak ! try again with an different password ..!")
        print(" ******* Instruction ********")
        print(
            "Minimum eight characters,\n \
             at least one uppercase letter,\n \
             one lowercase letter,\n \
             one number and one special character, \n \
             without spaces."
        )


password_strength()
