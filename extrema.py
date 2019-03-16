n = int(input(""))
a = list(map(int,input().split()))
extrema = 0
for i in range(n):
    if(i == 0):
        if(a[0] != a[0]):
            extrema+=1
    if(i == n-1 and a[i] != a[i-1]):
        extrema+=1
    else:
        if(a[i]< a[i-1] and a[i]<a[i+1]):
            extrema+=1
        elif(a[i]>a[i-1] and a[i]>a[i+1]):
            extrema+=1
print(extrema)
