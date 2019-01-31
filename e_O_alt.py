n = input("")
c=0
i=0
miner = 0
while(i<len(n)-1):
    if(i%2 == 0 and int(n[i])%2 == 0 and int(n[i+1])%2 != 0):
        c+=1
    elif(i%2 != 0  and int(n[i])%2 !=0 and int(n[i+1])%2 == 0):
        c+=1
    if(c>miner):
        miner = c
    if((int(n[i])%2 != 0 and int(n[i+1])%2 != 0) or (int(n[i])%2 ==0 and int(n[i+1])%2 == 0)):
        c = 0
    i+=1

print(miner+1)
