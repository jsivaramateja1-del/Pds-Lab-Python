# Problem 1: Strong Number Check
def fact(digit):
    if digit == 0 or digit == 1:
        return 1
    else:
        return digit * fact(digit-1)
num = int(input("Enter the number : "))
temp = num
total = 0
while temp > 0:
    digit = temp % 10
    total += fact(digit)
    temp = temp // 10
if total == num :
    print(f"{num} is a Strong Number.")
else:
    print(f"{num} is not a Strong number")