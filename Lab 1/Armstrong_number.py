# Problem 2: Armstrong Numbers in Range 100 to 999
def arm(num):
    temp = num
    digit = 0
    cube = 0
    while temp > 0:
        digit = temp % 10
        cube += digit ** 3
        temp = temp // 10
    if cube == num:
        return 1
    else :
        return 0

for i in range(100,1000):
    if arm(i) == 1:
            print(i,end=' ')
