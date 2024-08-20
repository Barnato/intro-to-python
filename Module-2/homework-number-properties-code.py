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
     


