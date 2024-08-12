#get user input of a numerical grae
grade = input("Enter your grade: " )

#case to an int
grade = int(grade)

#test the range of the number and print the appropriate letter grade
if grade >= 90:
    print('A')
elif grade >=80:
    print('B')
elif grade >=70:
    print('C')
elif grade >= 60:
    print('0')
else:
    print('F')