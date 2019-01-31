n,m = map(int,input().split())
res = []
for i in range(n):
    a,b = map(int,input().split())
    for i in range(a,b+1):
        if i not in res:
            res.append(i)
x = len(res)-1
if(res[x]>=m):
    print("yes")
else:
    print("no")
