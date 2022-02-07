def triangular(n):
    sum = 0
    for i in range(0,n):
        sum = sum + i
        if sum == n:
            return 1
            break
    if n == i:
        return 0
n = int(input())
k = triangular(n)
if k == 1:
    print("Yes")
else :
    print("no")
