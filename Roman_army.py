n = int(input(""))
a = list(map(int,input().split()))
c = 0
for k in range(2,n):
    for j in range(1,k):
        for i in range(j):
            if(a[i]>a[j]>a[k]):
                c+=1
print(c)
