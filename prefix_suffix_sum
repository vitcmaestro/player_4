def prefixsum(i):
    add = 0
    for j in range(i+1):
        add = add+a[j]
    z = n-i+1
    for k in range(-1,-z,-1):
        add = add+a[k]
    return add
n = int(input(""))
a = list(map(int,input().split()))
for i in range(n):
    if(i == 0):
        print(prefixsum(i),end =" ")
    else:
        print(prefixsum(i),end = "")
    
