n = int(input())
a = list(map(int,input().split()))
res=[]
for i in range(n):
    add = 0
    for j in range(i+1,n):
        add = add+ a[j]
    res.append(add)
for i in range(n):
    add = 0
    for j in range(i+1):
        add = add+ a[j]
    res.append(add)
print(max(res))
