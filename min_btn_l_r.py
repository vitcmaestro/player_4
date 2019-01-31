n,l,r = map(int,input().split())
res = list(map(int,input().split()))
res = res[l-1:r+1]
print(min(res))
