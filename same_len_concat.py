a,b = map(str,input().split())
if(len(a)>len(b)):
    print(a[:len(b)]+b[:])
elif(len(b)>len(a)):
    print(a+b[:len(a)])
else:
    print(a+b)
