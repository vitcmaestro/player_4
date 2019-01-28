m,n = map(int,input().split())
s = list(map(int,input().split()))
x=[]
y=[]
for i in range(m):
    x.append(s[i])
for i in range(m,len(s)):
    y.append(s[i])
c = 0
if(m>=n):
    for i in x:
        if i in y:
            if(c == 0):
                print(i,end="")
                c+=1
            else:
                print("",i,end = "")
else:
    for i in y:
        if i in x:
            if(c==0):
                print(i,end="")
                c+=1
            else:
                print("",i,end= "")
