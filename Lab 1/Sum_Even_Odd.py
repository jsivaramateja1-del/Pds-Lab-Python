# Problem 3: Sum of Even and Odd Numbers Separately
N = int(input("Enter How many numbers you want to input :"))
i = 0
e_count = 0
o_count = 0
while i < N:
    num = int(input("Enter an number : "))
    if num % 2 == 0:
        e_count += num
    else:
        o_count += num
    i += 1
print("Even numbers sum = ",e_count,",","Odd numbers sum = ",o_count)