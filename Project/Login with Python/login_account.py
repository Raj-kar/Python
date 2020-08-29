from csv import reader

def user_login():
    user_email = input("Enter your email: ").lower()
    user_password = input("Enter password: ")

    with open("test_data.csv") as file:
        user_data = reader(file)
        for data in user_data:
            if data[2] == user_email:
                if data[3] == user_password:
                    print("LOGIN SUCCESSFULLY !")
                    exit()
                else:
                    print("Wrong Password")
                    exit()
        else:
            print("No Account found !")