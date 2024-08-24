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

isComposite(x):
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
    
    # Check if the number is less than or equal to 1
    if x <= 1:
        return False
    
    """ Iterate from 2 to x-1 to check for factors"""
    for i in range(2, x):
        # If x is divisible by any number between 2 and x-1, it is composite
        if x % i == 0:
            return True
    
    # If no factors are found, the number is not composite (it is prime)
    return False

# Example usage
print(isComposite(9))   # True
print(isComposite(22))  # True
print(isComposite(3))   # False
print(isComposite(41))  # False

def isPerfect(x):
    """Returns whether or not the given number x is perfect.

    A number is said to be perfect if it is equal to the sum of all its
    factors (for obvious reasons the list of factors being considered does
    not include the number itself).

    Example: 6 = 3 + 2 + 1, hence 6 is perfect.
    Example: 28 is another example since 1 + 2 + 4 + 7 + 14 is 28.
    Note, the number 1 is not a perfect number.
    """
    
    # your code here
    
    
    # Check if the number is less than or equal to 1
    if x <= 1:
        return False
    
    # Initialize the sum of factors
    sum_of_factors = 0
    
    # Iterate over the range from 1 to x-1 to find factors
    for i in range(1, x):
        # Check if i is a factor of x
        if x % i == 0:
            # Add the factor to the sum
            sum_of_factors += i
    
    # Check if the sum of factors equals the number
    return sum_of_factors == x

# Example usage
print(isPerfect(6))   # True
print(isPerfect(28))  # True
print(isPerfect(12))  # False


def isAbundant(x):
    """
    Returns whether or not the given number x is abundant.

    A number is considered to be abundant if the sum of its factors
    (aside from the number) is greater than the number itself.

    Example: 12 is abundant since 1+2+3+4+6 = 16 > 12.
    However, a number like 15, where the sum of the factors
    is 1 + 3 + 5 = 9 is not abundant.
    """
      # your code here
         # Initialize a variable to store the sum of factors
    sum_of_factors = 0
    
    # Iterate over the range from 1 to x-1 to find factors
    for i in range(1, x):
        # Check if i is a factor of x
        if x % i == 0:
            """ Add the factor to the sum """
            sum_of_factors += i
    
    # Check if the sum of factors is greater than x
    return sum_of_factors > x

print(isAbundant(12))  # Should return True
print(isAbundant(15))  # Should return False
    
def isTriangular(x):
    """
    Returns whether or not a given number x is triangular.
    
    The triangular number Tn is a number that can be represented in the form of a triangular 
    grid of points where the first row contains a single element and each subsequent row contains 
    one more element than the previous one.
    
    We can just use the fact that the nth triangular number can be found by using a formula: Tn = n(n + 1) / 2.
    
    Example: 3 is triangular since 3 = 2(3) / 2
    3 --> 2nd position: (2 * 3 / 2)
    
    Example: 15 is triangular since 15 = 5(6) / 2
    15 --> 5th position: (5 * 6 / 2)
    """
    
    # code goes here
    
    # Initialize n to start checking from the first triangular number
    n = 1
    
    """ Iterate while the nth triangular number is less than or equal to x """
    while n * (n + 1) // 2 <= x:
        # Check if the nth triangular number is equal to x
        if n * (n + 1) // 2 == x:
            return True  # x is a triangular number
        n += 1  # Increment n to check the next triangular number
    
    # If no triangular number matches x, return False
    return False

# Example usage
print(isTriangular(3))  # Should return True
print(isTriangular(15))  # Should return True
print(isTriangular(10))  # Should return False

     def isNarcissistic(x):
    """
    Returns whether or not a given number is Narcissistic.

    A positive integer is called a narcissistic number if it
    is equal to the sum of its own digits each raised to the
    power of the number of digits.

    Example: 153 is narcissistic because 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153.
    Note that by this definition all single digit numbers are narcissistic.
    """
    # your code here
    
    # Convert the number to a string to easily iterate over its digits
    num_str = str(x)
    
    # Get the number of digits in the number
    num_digits = len(num_str)
    
    """ Calculate the sum of each digit raised to the power of the number of digits """
    total = sum(int(digit) ** num_digits for digit in num_str)
    
    # Check if the calculated sum is equal to the original number
    return x == total

print(isNarcissistic(153))