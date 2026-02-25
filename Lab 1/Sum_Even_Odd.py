# Problem 3: Sum of Even and Odd Numbers Separately
N = int(input("Enter How many numbers you want to input :"))
i = 0
e_sum = 0
o_sum = 0
while i < N:
    num = int(input("Enter an number : "))
    if num % 2 == 0:
        e_sum += num
    else:
        o_sum += num
    i += 1
print("Even numbers sum = ",e_sum,",","Odd numbers sum = ",o_sum)
