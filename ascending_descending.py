n = int(input())
res = list(map(int,input().split()))
mid = n//2
x = sorted(res[:mid])
y = sorted(res[mid:],reverse = True)
s = ' '.join(map(str,x))
t = ' '.join(map(str,y))
print(s,t)
