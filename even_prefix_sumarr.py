n = int(input(""))
a = list(map(int,input().split()))
ans = a[0]
print(a[0],end = "")
for i in range(1,n):
    if(a[i]%2 !=0 and i%2 != 0):
        ans += a[i]
        a[i] = ans
    elif(a[i]%2 == 0):
        ans += a[i]
        a[i] = ans
    else:
        ans+=a[i]
    print("",a[i],end="")
