n,k = map(int,input().split())
a = []
co = 0
for i in range(n):
    s = input("")
    a.append(s)
for i in range(n-1):
    if(a[i] == a[i+1]):
        co+=1
    else:
        if(co == k):
            break
        co = 0
if(co == k):
    print("yes")
else:
    print("no")
