secret_password = ""
while secret_password != "secret":
    secret_password =input("Please enter the password:")
    if secret_password == "secret":
        print("Welcome!")
    else:
            print("Sorry, the password you entered is incorrect. Please try again.")
