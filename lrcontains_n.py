l,r,n = map(int,input().split())
test = str(n)
count = 0
for i in range(l,r+1):
    x = str(i)
    if test in x:
        count+=1
print(count)
