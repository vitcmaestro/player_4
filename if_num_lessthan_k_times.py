n,k = map(int,input("").split())
lis = list(map(int,input().split()))
lis.sort()
freq = [1]*n
for i in range(n-2):
    if(lis[i] == lis[i+1]):
        lis.remove(lis[i+1])
        freq[i]+=1
c = 0
for i in range(len(lis)):
    if(freq[i]<k):
        if(c == 0):
            print(lis[i],end ="")
            c+=1
        else:
            print("",lis[i],end = "")
