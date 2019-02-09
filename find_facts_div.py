def fact(n):
    prod = 1
    for i in range(2,n+1):
        prod = prod*i
    return prod
a,b = map(int,input().split())
x = fact(a)
y = fact(b)
print(x//y)
