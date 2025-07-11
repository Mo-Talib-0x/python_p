num1= int(input("Enter the first number: "))
num2= int(input("Enter the second number: "))
operator=(input("Enter the operator +,-,*,/: ")).strip()
if operator=="+":
    print(f"Addition of {num1} and {num2} is: {num1+num2}")
elif operator=="-":
    print(f"Subtraction of {num1} by {num2} is: {num1-num2}")
elif operator=="*":
    print(f"Multiplication of {num1} and {num2} is: {num1*num2}")
elif operator=="/":
    if num2 !=0:
        print(f"Division of {num1} by {num2} is: {num1/num2}" )
    else:
        print("Error: Division by 0 is not allowed.")
else:
    print("Please enter a valid input.")