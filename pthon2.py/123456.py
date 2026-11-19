num=int(input("enter a number : "))
digits = len(str(num))
sum= 0
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** digits
    temp //= 10
if sum== num:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")
