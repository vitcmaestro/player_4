s = list(map(str,input().split()))
maxer = len(s[0])
res = s[0]
for i in s:
    if(len(i)> maxer):
        maxer = len(i)
        res = i
print(res)
