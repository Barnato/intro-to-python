def import_and_create_bank(filename):
    '''
    This function is used to create a bank dictionary. The given argument is the filename to load.
    Every line in the file should be in the following format:
        key: value
    The key is a user's name and the value is an amount to update the user's bank account with. The value should be a
    number; however, it is possible that there is no value or that the value is an invalid number.
    '''
    bank = {}

    # Open file in read mode
    f = open(filename, 'r')

    # Get all lines in file as list
    lines = f.readlines()

    # Iterate over each line in lines
    for line in lines:
        # Strip whitespace from beginning and end of line and split based on colon separator
        lst = line.strip().split(':')

        if len(lst) <= 1:
            continue

        # Get key (name) and value (deposit amount) from line
        key = lst[0].strip()
        value = lst[1].strip()

        try:
            # Try to cast value (deposit amount) to numeric value
            value = float(value)

            # Add new deposit amount to current total balance associated with key (name), or 0 if key doesn't exist
            bank[key] = bank.get(key, 0) + value
        except ValueError:
            # Otherwise, skip this line if value casting fails
            continue

    f.close()

    print(bank)
    return bank

