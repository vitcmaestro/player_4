n = int(input(""))
lis = list(map(int,input().split()))
c = 0
prod = 1
ten = 0
for i in lis:
    if(i%2 != 0):
        c+=1
        prod = prod * i
    if(i%10 == 0):
        ten +=1
if((prod%2 == 0 or ten>0)  and c>0):
    print("even")
elif(c == 0):
    print("even")
else:
    print("odd")
