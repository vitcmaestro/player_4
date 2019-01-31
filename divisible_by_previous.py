n = int(input())
a = list(map(int,input().split()))
res = []
for i in range(1,n):
    if(a[i]%a[i-1] == 0):
        res.append(a[i])
print(*res)
