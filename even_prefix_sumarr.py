n = int(input(""))
a = list(map(int,input().split()))
res = []
for i in range(n):
    ans = 0
    if(a[i]%2 !=0):
        res.append(str(a[i]))
    else:
        for j in range(i+1):
            ans += a[j]
        res.append(str(ans))
print(" ".join(res).strip())
