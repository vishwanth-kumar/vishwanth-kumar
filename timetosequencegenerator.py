intime = input().split(':')
def decimaltobinary(n):
    return "{0:b}".format(int(n))
def maxsubarraysum(a,size):
    far = - 1000000 -1
    here = 0
    for i in range(0,size):
        here = here + a[i]
        if(far < here):
            far = here
        if here < 0:
            here = 0
    return far
ans = []
for word in intime:
    for letter in word:
        ans.append(decimaltobinary(int(letter)))
for i in range(len(ans)):
    while(len(ans[i]) !=4):
        ans[i] = "0" + ans[i]
matrix = []
for i in range(4):
    tmp = []
    for j in range(6):
        if(ans[j][i] == '0'):
            tmp.append(-1)
        else:
            tmp.append(1)
    matrix.append(tmp)
final = []
for i in matrix:
    gg = maxsubarraysum(i,6)
    if(gg < 0):
        final.append(0)
    else:
        final.append(gg)
for i in range(len(final)):
    try:
        fina[i+1]
        print(final[i],end = ",")
    except:
        print(final[i])
