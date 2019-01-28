n = int(input())
s = list(map(int,input().split()))
add = 0
for i in range(n-1):
    add = add + s[i]+s[i+1]
print(add)
