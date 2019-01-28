n = int(input())
s = list(map(str,input().split()))
res=[]
c = 0
for i in s:
    if i not in res:
        res.append(i)
        if(c==0):
            print(i,end="")
            c+=1
        else:
            print("",i,end="")
