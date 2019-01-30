n = int(input(""))
lis = list(map(int,input().split()))
res=1
for i in range(len(lis)):
    c = 0
    for j in range(len(lis)):
        if(lis[j]%lis[i] == 0):
            c+=1
    if(c == len(lis)):
        print(lis[i])
    
