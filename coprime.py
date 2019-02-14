n,m = map(int,input().split())
x = min(m,n)
count = 0
for i in range(1,x+1):
    if(n%i == 0 and m%i == 0):
        count+=1
if(count == 1):
    print("yes")
else:
    print("no")
    
