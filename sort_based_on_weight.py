n = int(input())
a = list(map(int,input().split()))
weight = list(map(int,input().split()))
for i in range(n):
    for j in range(n):
        if(weight[i]<weight[j]):
            weight[i],weight[j] = weight[j],weight[i]
            a[i],a[j] = a[j],a[i]
print(' '.join(map(str,a)))
