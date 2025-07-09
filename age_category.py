name= input("Enter your name: ")
age= int(input("Enter the age: "))
if age<12:
    print(f"{name}, you are child.")
elif (age>=12 and age<18):
    print(f"{name}, you are teen.")
else:
    print(f"{name}, you are adult.")
