num1= int(input("Enter the first number: "))
num2= int(input("Enter the secon number: "))
operator=(input("Enter the operator +,-,*,/: "))
if operator=="+":
    print(f"Addition of {num1} and {num2} is: ",num1+num2)
elif operator=="-":
    print(f"subration of {num1} by {num2} is: ",num1-num2)
elif operator=="*":
    print(f"Multiplication of {num1} and {num2} is: ",num1*num2)
elif operator=="/":
    print(f"Division of {num1} by {num2} is: ",num1/num2 )
else:
    print("please enter a valid input.")