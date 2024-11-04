def signup(user_accounts, log_in, username, password):
    '''
    This function allows users to sign up.
    If both username and password meet the requirements:
    - Updates the username and the corresponding password in the user_accounts dictionary.
    - Updates the log_in dictionary, setting the value to False.
    - Returns True.

    If the username and password fail to meet any one of the following requirements, returns False.
    - The username already exists in the user_accounts.
    - The password must be at least 8 characters.
    - The password must contain at least one lowercase character.
    - The password must contain at least one uppercase character.
    - The password must contain at least one number.
    - The username & password cannot be the same.

    For example:
    - Calling signup(user_accounts, log_in, "Brandon", "123abcABCD") will return False
    - Calling signup(user_accounts, log_in, "BrandonK", "123ABCD") will return False
    - Calling signup(user_accounts, log_in, "BrandonK","abcdABCD") will return False
    - Calling signup(user_accounts, log_in, "BrandonK", "123aABCD") will return True. Then calling
    signup(user_accounts, log_in, "BrandonK", "123aABCD") again will return False.

    Hint: Think about defining and using a separate valid(password) function that checks the validity of a given password.
    This will also come in handy when writing the change_password() function.
    '''


    # your code here

    if username is not in user_accounts and valid(password) and username is not equals to password
        update username and password in user_accounts dictionary
        update username and login T / F in log_in dictionary
        return True

    else
        return False


def valid(password):
    # write the code for valid password
    # Debug/ Check if your valid funtin works as desired
    return True / False


def import_and_create_accounts(filename):
    # your code here
    initiate
    user_accounts
    dictionary
    initiate
    log_in
    dictionary
    user = open('user.txt', 'r')

    for line in user
        if '-' not in line
            continue

        username = get
        the
        username
        from the file
        password = get
        the
        password
        from the file

        if username empty
        continue
    if password empty
    continue


signup(user_accounts, log_in, username, password)

return user_accounts, log_in


def import_and_create_accounts(filename):
    # your code here
    initiate user_accounts dictionary
    initiate log_in dictionary
    user = open('user.txt', 'r')

    for line in user
        if '-' not in line
            continue

        username = get the username from the file
        password = get the password from the file

        if username empty
        continue
    if password empty
    continue
signup(user_accounts, log_in, username, password)

return user_accounts, log_in
