number=int(input("Enter the number: "))
limit=int(input("Enter the range limit: "))
for i in range(1,limit+1):
    print(f"{number}*{i}=",number*i)