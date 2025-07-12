rows=int(input("Enter the number you want rows: "))
for i in range(1,rows+1):
    spaces=" " * (rows-i)
    stars="*" * (3*i-1)
    print(spaces+stars)