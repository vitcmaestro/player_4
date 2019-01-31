n,m = map(int,input().split())
d = 0
for i in range(n):
    a,b = map(int,input().split())
    if(b == m):
        d =1
print(d)
