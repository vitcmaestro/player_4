n,k = map(int,input().split())
a = []
c = 1
for i in range(n):
    s = input("")
    a.append(s)
for i in range(n-1):
    if(a[i] == a[i+1]):
        c+=1
    else:
        if(c == k):
            break
        c = 1
if(c == k):
    print("yes")
else:
    print("no")
