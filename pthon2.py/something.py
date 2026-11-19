n=int(input("Enter the number of values:"))
largest=int(input("Enter number 1:"))
for i in range(2,n+1):
    num=int(input("Enter  number"+str(i)+":"))
    if num>largest:
        largest=num
print("largest number=",largest)
