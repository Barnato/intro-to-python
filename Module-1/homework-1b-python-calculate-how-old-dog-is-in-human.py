import traceback
 
def calculator():
   
    # Get dog age
    age = input("Input dog years: ")
 
    try:
        # Cast to float
        d_age = float(age)
        h_age = float()
        if d_age > 0:
            
          # If user enters negative number, print message
        # Otherwise, calculate dog's age in human years
    
        # your code here

        # Calculate dog's age in human years
            if d_age <= 1:
                h_age = d_age * 15
                h_age = round(h_age,2)
                print('The given dog age ' +  str(d_age) + ' is ' + str(h_age), 'in human years.')
            elif d_age <= 2:
                h_age = d_age * 12
                h_age = round(h_age,2)
                print('The given dog age ' +  str(d_age) + ' is ' + str(h_age), 'in human years.')
            elif d_age <= 3:
                h_age = d_age * 9.3
                h_age = round(h_age,2)
                print('The given dog age ' +  str(d_age) + ' is ' + str(h_age), 'in human years.')
            elif d_age <= 4:
                h_age = d_age * 8
                h_age = round(h_age,2)
                print('The given dog age ' +  str(d_age) + ' is ' + str(h_age), 'in human years.')
            elif d_age <= 5:
                h_age = d_age * 7.2
                h_age = round(h_age,2)
                print('The given dog age ' +  str(d_age) + ' is ' + str(h_age), 'in human years.')
            else:
                h_age = 36 + (d_age - 5) * 7
                h_age = round(h_age,2)
                print('The given dog age ' +  str(d_age) + ' is ' + str(h_age), 'in human years.')
     
        else:
           print("Age cannot be negative or zero.")

    except:
        print(age, "is an invalid age.")
        print(traceback.format_exc())
    
calculator() # This line calls the calculator function
