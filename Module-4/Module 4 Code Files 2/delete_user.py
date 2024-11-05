def delete_account(user_accounts, log_in, bank, username, password):
'''
Completely deletes the user from the online banking system.
If the user exists in the user_accounts dictionary and the password is correct, and the user
is logged in (the username is associated with the value True in the log_in dictionary):
- Deletes the user from the user_accounts dictionary, the log_in dictionary, and the bank dictionary.
- Returns True.
Otherwise:
- Returns False.

For example:
- Calling delete_account(user_accounts, log_in, bank, "BrandonK", "123abcABC") will return False
- Calling delete_account(user_accounts, log_in, bank, "Brandon", "123abcABDC") will return False
- If you first log "Brandon" in, calling delete_account(user_accounts, log_in, bank, "Brandon", "brandon123ABC")
will return True
'''

# your code here

if log_in[username]:
    del user_accounts[username]
    del log_in[username]
    del bank[username]
    return True
return False