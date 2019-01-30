def isdiv(z):
    for i in lis:
        if(z%i != 0):
            return False
    else:
        return True
n = int(input(""))
lis = list(map(int,input().split()))
res=1
for i in lis:
    res = res*i
for j in range(res-1,0,-1):
    if(isdiv(j) and j<res):
        res = j
print(res)
