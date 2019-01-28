def prefixsum(i):
    add = 0
    z = n-i+1
    for k in range(-1,-z,-1):
        add = add+a[k]
    return add
n = int(input(""))
a = list(map(int,input().split()))
for i in range(n):
    if(i == (n-1)):
        print(prefixsum(i),end ="")
    else:
        print(prefixsum(i),end = " ")
    
