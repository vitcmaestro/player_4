d,m,y = map(int,input().split('/'))
res = True
if(d<=0 or d>31):
    res = False
if(m<1 or m>12):
    res = False
if(y > 9999):
    res = False
if(res == True):
    print("yes")
else:
    print("no")
