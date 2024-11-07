def change_password(user_accounts, log_in, username, old_password, new_password):
    '''
    This function allows users to change their password.

    If all of the following requirements are met, changes the password and returns True. Otherwise, returns False.
    - The username exists in the user_accounts.
    - The user is logged in (the username is associated with the value True in the log_in dictionary)
    - The old_password is the user's current password.
    - The new_password should be different from the old one.
    - The new_password fulfills the requirement in signup.

    For example:
    - Calling change_password(user_accounts, log_in, "BrandonK", "123abcABC" ,"123abcABCD") will return False
    - Calling change_password(user_accounts, log_in, "Brandon", "123abcABCD", "123abcABCDE") will return False
    - Calling change_password(user_accounts, log_in, "Brandon", "brandon123ABC", "brandon123ABC") will return False
    - Calling change_password(user_accounts, log_in, "Brandon", "brandon123ABC", "123abcABCD") will return True

    Hint: Think about defining and using a separate valid(password) function that checks the validity of a given password.
    This will also come in handy when writing the signup() function.
    '''

    # Check if the username exists in user_accounts
    if username not in user_accounts:
        return False

    # Check if the user is logged in
    if not log_in.get(username, False):
        return False

    # Check if the old_password matches the current password
    if user_accounts[username] != old_password:
        return False

    # Check if the new_password is different from the old one
    if old_password == new_password:
        return False

    # Check if the new_password is valid
    if not check_password_different_and_valid(old_password, new_password):
        return False

    # Update the password
    user_accounts[username] = new_password
    return True