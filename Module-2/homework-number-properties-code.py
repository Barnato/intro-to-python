def isPrime(x):
    # if the number is bigger than 1 and when divided by 2 leaves a remainder
    if ((x > 1) and (x % 2 != 0)):
        print("True")
    else:
        print("False")

factors = []
    
    #iterate over range from 1 to number x.
    for i in range(1, x + 1):
        
        #check if i divide number's evenly
        if (x % i == 0):
            factors.append(i)
    
    return factors

print(getFactors(21))
     
def isComposite(x):
    if ((x > 1) and (x % 2 == 0)):
        print("True")
    else:
        print("False")
    """Returns whether or not the given number x is composite.

    A composite number has more than 2 factors.
    A natural number greater than 1 that is not prime is called a composite number.
    Note, the number 1 is neither prime nor composite.

    For example:
    - Calling isComposite(9) will return True
    - Calling isComposite(22) will return True
    - Calling isComposite(3) will return False
    - Calling isComposite(41) will return False
    """
    
    # your code here

