**The Assignment**

In this assignment, you will write a program that calculates a dog's age in human years.

The program will prompt the user for an age in dog years and calculate that age in human years.  Allow for int or float values, but check the user's input to make sure it's valid -- it should be numeric and positive.  Otherwise, let the user know their input is not valid.

You can use the following rules to approximately convert a medium-sized dog's age to human years:

For the first year, one dog year is equal to 15 human years
For the first 2 years, each dog year is equal to 12 human years
For the first 3 years, each dog year is equal to 9.3 human years
For the first 4 years, each dog year is equal to 8 human years
For the first 5 years, each dog year is equal to 7.2 human years
After that, each dog year is equal to 7 human years.  (Note: This means the first 5 dog years are equal to 36 human years (5 * 7.2) and the remaining dog years are equal to 7 human years each.)
Print the result in the following format, substituting for <dog_age> and <human_age>: "The given dog age <dog_age> is <human_age> in human years."  Round the result to 2 decimal places.  Note: If there is a 0 in the hundredths place, you can drop it, e.g. 24.00 can be displayed as 24.0. 

For example:

If the user enters 2, the program will print: "The given dog age 2 is 24.0 in human years."
If the user enters 3, the program will print: "The given dog age 3 is 27.9 in human years."
If the user enters 4.5, the program will print: "The given dog age 4.5 is 32.4 in human years."
If the user enters 12.1, the program will print: "The given dog age 12.1 is 85.7 in human years."
Considering invalid inputs:

Your program must ask the user for an age in dog years - hint: use the input() function
We are going to test invalid inputs - make sure that your code can handle negative value inputs and non-numerical inputs!
For invalid inputs, make sure that your printed response adheres to the following:
     - If a text-based input is provided, make sure your response contains the word 'invalid'.  For example, if the user doesn'tinput a number, print "<age> is invalid.", substituting for <age>.

     - If a negative input is provided, make sure your response contains the word 'negative'.  For example, if the user inputs a negative number, print "Age cannot be a negative number."

Submission

Open the Jupyter Notebook directly in Coursera (you will find it in the item following this reading).  To complete the assignment, complete the provided Jupyter Notebook file, following the detailed instructions in each cell. Test your submission before submitting by following the instructions on the assignment page in Coursera. When you're happy with your solutions, click the 'Submit Assignment' button in the top right. 

**My Submission**


**The Assignment**

In this assignment, you will write a program that calculates a dog's age in human years.

The program will prompt the user for an age in dog years and calculate that age in human years.  Allow for int or float values, but check the user's input to make sure it's valid -- it should be numeric and positive.  Otherwise, let the user know their input is not valid.

You can use the following rules to approximately convert a medium-sized dog's age to human years:

For the first year, one dog year is equal to 15 human years
For the first 2 years, each dog year is equal to 12 human years
For the first 3 years, each dog year is equal to 9.3 human years
For the first 4 years, each dog year is equal to 8 human years
For the first 5 years, each dog year is equal to 7.2 human years
After that, each dog year is equal to 7 human years.  (Note: This means the first 5 dog years are equal to 36 human years (5 * 7.2) and the remaining dog years are equal to 7 human years each.)
Print the result in the following format, substituting for <dog_age> and <human_age>: "The given dog age <dog_age> is <human_age> in human years."  Round the result to 2 decimal places.  Note: If there is a 0 in the hundredths place, you can drop it, e.g. 24.00 can be displayed as 24.0. 

For example:

If the user enters 2, the program will print: "The given dog age 2 is 24.0 in human years."
If the user enters 3, the program will print: "The given dog age 3 is 27.9 in human years."
If the user enters 4.5, the program will print: "The given dog age 4.5 is 32.4 in human years."
If the user enters 12.1, the program will print: "The given dog age 12.1 is 85.7 in human years."
Considering invalid inputs:

Your program must ask the user for an age in dog years - hint: use the input() function
We are going to test invalid inputs - make sure that your code can handle negative value inputs and non-numerical inputs!
For invalid inputs, make sure that your printed response adheres to the following:
     - If a text-based input is provided, make sure your response contains the word 'invalid'.  For example, if the user doesn'tinput a number, print "<age> is invalid.", substituting for <age>.

     - If a negative input is provided, make sure your response contains the word 'negative'.  For example, if the user inputs a negative number, print "Age cannot be a negative number."

Submission

Open the Jupyter Notebook directly in Coursera (you will find it in the item following this reading).  To complete the assignment, complete the provided Jupyter Notebook file, following the detailed instructions in each cell. Test your submission before submitting by following the instructions on the assignment page in Coursera. When you're happy with your solutions, click the 'Submit Assignment' button in the top right. 

**My Submission**


import traceback
 
def calculator():
   
    # Get dog age
    age = input("Input dog years: ")
 
    try:
        # Cast to float
        d_age = float(age)
       
        if d_age < 0:
            raise ValueError("Age cannot be a negative number.")
       
        # Predefined human age values for the first five dog years
        dog_year_one = 15
        dog_year_two = dog_year_one + 12
        dog_year_three = dog_year_two + 9.3
        dog_year_four = dog_year_three + 8
        dog_year_five = dog_year_four + 7.2
       
        # Calculate dog's age in human years
        if d_age <= 1:
            human_age = d_age * dog_year_one
        elif d_age <= 2:
            human_age = dog_year_one + (d_age - 1) * 12
        elif d_age <= 3:
            human_age = dog_year_two + (d_age - 2) * 9.3
        elif d_age <= 4:
            human_age = dog_year_three + (d_age - 3) * 8
        elif d_age <= 5:
            human_age = dog_year_four + (d_age - 4) * 7.2
        else:
            human_age = dog_year_five + (d_age - 5) * 7
       
        # Round the result to 2 decimal places
        human_age = round(human_age, 2)
       
        # Format the result
        if human_age * 100 % 10 == 0:
            human_age = f"{human_age:.1f}"
        else:
            human_age = f"{human_age:.2f}"
       
        print(f"The given dog age {age} is {human_age} in human years.")
   
    except ValueError as e:
        if "could not convert string to float" in str(e):
            print(f"{age} is invalid.")
        else:
            print(e)
    except Exception:
        print(f"{age} is an invalid age.")
        print(traceback.format_exc())
   
calculator() # This line calls the calculator function
