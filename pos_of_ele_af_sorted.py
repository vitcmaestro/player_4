n = int(input())
s = list(map(str,input().split()))
res= sorted(s)
c = 0
for i in s:
    if(c == 0):
        print(res.index(i)+1,end ="")
        c+=1
    else:
        print("",res.index(i)+1,end="")
